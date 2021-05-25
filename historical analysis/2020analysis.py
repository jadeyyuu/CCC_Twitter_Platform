from historical_analysis import *

data = read_json("2020historical/*.json")
df = spark_df(data)
SA = Sentiment(df)

melb = SA.sentiment_results().toPandas()
import datetime
def tostring(time):
    return int(time.strftime("%Y"))
def tomonth(time):
    return int(time.strftime("%m"))
melb['year']=melb['time'].apply(tostring)
melb['month']=melb['time'].apply(tomonth)
melb = melb[melb['city']=='Melbourne']
melb = melb[['year','month','text','sentiment_score','sentiment']]
melb.to_json('melb2020.json')

topic_analysis = Topic_analysis(df)
topic_analysis.word_cloud_fall("March")
topic_analysis.word_cloud_fall("April")
topic_analysis.word_cloud_fall("May")
topic_analysis.word_cloud_winter("June")
topic_analysis.word_cloud_winter("July")
topic_analysis.word_cloud_winter("August")
topic_analysis.word_cloud_spring("September")
topic_analysis.word_cloud_spring("October")
topic_analysis.word_cloud_summer("November")
topic_analysis.word_cloud_summer("December")

summary = SA.print_summary()
summary[['covid_content','count']].groupby('covid_content').agg('sum')
sum_covid = summary[['covid_content','sentiment','count']].groupby(['covid_content','sentiment']).agg('sum')

sum_covid['total']=[1065]*3+[29434]*3
sum_covid['percentage'] = sum_covid['count']/sum_covid['total']

sum_sen = summary[['sentiment','count']].groupby('sentiment').agg('sum')
sum_sen['percentage'] = sum_sen['count']/sum_sen['count'].sum()

SA.covid_overall_chart

topic_analysis = Topic_analysis(df)
formatted=topic_analysis.lda()
py_lda_prepared_data = pyLDAvis.prepare(formatted['topic_term_dists'],formatted['doc_topic_dists'],formatted['doc_lengths'],formatted['vocab'],formatted['term_frequency'])
# pyLDAvis.display(py_lda_prepared_data)
pyLDAvis.save_html(py_lda_prepared_data, 'lda.html')

topic_analysis = Topic_analysis(df)
top=topic_analysis.top_react_tweet()
top_df = top.select('time','text','quote_count','reply_count','retweet_count','favorite_count','react_count')
top_df = top_df.select('*',month('time').alias('month'))
top_df = top_df.orderBy(top_df.month,top_df.react_count.desc())
window = Window.partitionBy(top_df['month']).orderBy(top_df['react_count'].desc())
df_pd = top_df.select('*', rank().over(window).alias('rank')).filter(col('rank') <= 5).orderBy('month')
df_pd = df_pd.select('text','quote_count','reply_count','retweet_count','favorite_count','month','rank','react_count').toPandas()
df_pd.to_csv('topTweet.csv')

city_mean_score = SA.by_city()
sentiment_map = map(city_mean_score)
sentiment_map.map_with_city()

city_mean_score = SA.by_city()
sentiment_map = map(city_mean_score)
sentiment_map.payroll("Hume")
sentiment_map.payroll("Loddon Mallee")
sentiment_map.payroll("Grampians")
sentiment_map.payroll("Barwon South West")
sentiment_map.payroll("Gippsland")
sentiment_map.payroll("Greater Melbourne")

sentiment_map = map(city_mean_score)
sentiment_map.age_distrubion("Hume",px.colors.sequential.Burgyl)
sentiment_map.age_distrubion("Loddon Mallee",px.colors.sequential.Burgyl)
sentiment_map.age_distrubion("Grampians",px.colors.sequential.Burgyl)
sentiment_map.age_distrubion("Barwon South West",px.colors.sequential.Burgyl)
sentiment_map.age_distrubion("Gippsland",px.colors.sequential.Burgyl)
sentiment_map.age_distrubion("Greater Melbourne",px.colors.sequential.Burgyl)

import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyB47aIQkask-naqcK7kCGHZjxtSJsZe-3k')
def age_geo(city):
    try:
        name = city+", AU"
        geocode_result = gmaps.geocode(name)
    #     lng = geocode_result[0]['geometry']['location']['lng']
    #     lat = geocode_result[0]['geometry']['location']['lat']
        return geocode_result
    except:
        return

results['geo'] = results['sa4_name16'].apply(age_geo)

ef get_Point(row):
    lat = 0
    lng = 0
    for i in row:
        lat = i['geometry']['location']['lat']
        lng = i['geometry']['location']['lng']
    return geometry.Point(lng,lat)
results['geoPoint'] = results['geo'].apply(get_Point)

results = results[['sa4_name16','geometry']]
results_gpd = gpd.GeoDataFrame(results,geometry=results.geometry)
results_gpd.to_file('payroll_geo.geojson', driver="GeoJSON")

SA_results = SA.sentiment_results()
sentiment_impact(SA_results).overall()
