from flask import Flask, render_template, request
from pyspark.sql import SparkSession

app = Flask(__name__)

# Initialize Spark
spark = SparkSession.builder.appName("IPL_RDD").master("local[*]").getOrCreate()

# Load Data as DataFrames first (needed for schema)
matches_df = spark.read.csv("archive/matches.csv", header=True, inferSchema=True)
deliveries_df = spark.read.csv("archive/deliveries.csv", header=True, inferSchema=True)

# Convert to RDD
matches_rdd = matches_df.rdd
deliveries_rdd = deliveries_df.rdd

# Get column indexes
match_cols = matches_df.columns
delivery_cols = deliveries_df.columns

def row_to_dict(row, cols):
    return {col: row[i] for i, col in enumerate(cols)}

@app.route('/')
def index():
    page = request.args.get('page', default=1, type=int)
    page_size = 10
    offset_value = (page - 1) * page_size

    # Convert RDD to dict
    matches_dict_rdd = matches_rdd.map(lambda row: row_to_dict(row, match_cols))

    # Sort by date (descending)
    sorted_rdd = matches_dict_rdd.sortBy(lambda x: x['date'], ascending=False)

    # Pagination
    paged = sorted_rdd.zipWithIndex() \
                      .filter(lambda x: offset_value <= x[1] < offset_value + page_size) \
                      .map(lambda x: x[0]) \
                      .collect()

    # Select required fields
    rm_list = [
        {
            "id": m["id"],
            "team1": m["team1"],
            "team2": m["team2"],
            "date": m["date"]
        }
        for m in paged
    ]

    return render_template('index.html', matches=rm_list, page=page)


@app.route('/match/<int:match_id>')
def match_details(match_id):

    matches_dict_rdd = matches_rdd.map(lambda row: row_to_dict(row, match_cols))

    # Get match info
    info = matches_dict_rdd.filter(lambda x: int(x["id"]) == match_id).collect()[0]

    # Convert deliveries
    deliveries_dict_rdd = deliveries_rdd.map(lambda row: row_to_dict(row, delivery_cols))

    # Filter wickets
    wickets_rdd = deliveries_dict_rdd.filter(
        lambda x: int(x["match_id"]) == match_id and int(x["is_wicket"]) == 1
    )

    wicket = wickets_rdd.map(lambda x: {
        "batter": x["batter"],
        "bowler": x["bowler"],
        "player_dismissed": x["player_dismissed"],
        "dismissal_kind": x["dismissal_kind"],
        "batting_team": x["batting_team"]
    }).collect()

    return render_template('match.html', info=info, wickets=wicket)


if __name__ == '__main__':
    app.run(debug=True)