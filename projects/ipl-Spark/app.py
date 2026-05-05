from flask import Flask, render_template, request
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,desc,lower

app = Flask(__name__)


spark = SparkSession.builder.appName("IPL_Local").master("local[*]").getOrCreate()


matches_df = spark.read.csv("archive/matches.csv", header=True, inferSchema=True).sort(col("date").desc())
deliveries_df = spark.read.csv("archive/deliveries.csv", header=True, inferSchema=True)

@app.route('/')
def index():
    
    query = request.args.get('q', default='')
    filter_type = request.args.get('filter_type', default='all') # New parameter
    page = request.args.get('page', default=1, type=int)
    page_size = 10
    offset_value = (page - 1) * page_size

    filtered_df = matches_df

    
    if query:
        search_lower = query.lower()
        
        if filter_type == 'team':
            
            filtered_df = filtered_df.filter(
                (lower(col("team1")).contains(search_lower)) | 
                (lower(col("team2")).contains(search_lower))
            )
        elif filter_type == 'city':
            
            filtered_df = filtered_df.filter(lower(col("city")).contains(search_lower))
        else:
            
            filtered_df = filtered_df.filter(
                (lower(col("team1")).contains(search_lower)) |
                (lower(col("team2")).contains(search_lower)) |
                (lower(col("city")).contains(search_lower))
            )
    paged_df = filtered_df.offset(offset_value).limit(page_size)
    rm_list = [x.asDict() for x in paged_df.select("id", "team1", "team2", "date", "city").collect()]
    
    return render_template('index.html', 
                           matches=rm_list, 
                           page=page, 
                           query=query, 
                           filter_type=filter_type)
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