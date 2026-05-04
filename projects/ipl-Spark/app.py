from flask import Flask, render_template, request
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,desc

app = Flask(__name__)

# Initialize Spark
spark = SparkSession.builder.appName("IPL_Local").master("local[*]").getOrCreate()

# Load Data
matches_df = spark.read.csv("archive/matches.csv", header=True, inferSchema=True).sort(col("date").desc())
deliveries_df = spark.read.csv("archive/deliveries.csv", header=True, inferSchema=True)

@app.route('/')
def index():  
    
    page = request.args.get('page', default=1, type=int)
    page_size = 10
    offset_value = (page - 1) * page_size
    paged_df = matches_df.offset(offset_value).limit(10)
    rm_list = [x.asDict() for x in paged_df.select("id", "team1", "team2", "date").collect()]
    
    return render_template('index.html', matches=rm_list, page=page)

@app.route('/match/<int:match_id>')
def match_details(match_id):    
    info = matches_df.filter(col("id") == match_id).toPandas().to_dict(orient='records')[0]
    print(info)
    print(matches_df.filter(col("id") == match_id).toPandas().to_dict(orient='records'))
    
    wickets = deliveries_df.filter((col("match_id") == match_id) & (col("is_wicket") == 1)) \
                           .select("batter", "bowler", "player_dismissed", "dismissal_kind","batting_team") 
    
    wicket=[x.asDict() for x in wickets.collect() ]
    
    return render_template('match.html', info=info, wickets=wicket)

if __name__ == '__main__':
    app.run(debug=True)