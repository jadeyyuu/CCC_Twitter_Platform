import couchdb
import json
from json import JSONEncoder
import pandas as pd
import ijson
import datetime
import time
import tweepy
import nltk
import wordcloud
import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import sys
import numpy as np
from PIL import Image
import plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import os
from SentimentAnalysis import *
from TextAnalytics import *
from ccc_backend.ccc_backend.settings import *


couch = couchdb.Server("http://admin:password@172.26.130.42:5984/")
#couch = couchdb.Server("http://admin:1a2s3d4f5g@localhost:5984/")

try:
    couch.create("test_json")
except couchdb.http.PreconditionFailed:
    pass
db = couch["test_json"]
try:
    couch.create("sa_json")
except couchdb.http.PreconditionFailed:
    pass
db1 = couch["sa_json"]
#try:
    #couch.create("lc_json")
#except couchdb.http.PreconditionFailed:
    #pass
#db2 = couch["lc_json"]

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#sys.path.append(r'C:\Users\ylin1\Documents\GitHub\ccc_group30_django\ccc_backend\ccc_backend')

consumer_key = "7PC3L2O8ywCONU4ZuJ5h757mv"
consumer_secret = "MMhJhIIolKU3ONdXpLC6oGzOwYGYwYgzMILc3etxZ0yjuNtdze"
access_key = "1115405592372187136-19lxDiitrBBDSdSaLdyqgK3fJzJxWT"
access_secret = "w2FsaXLITsGDy1PsRvqkdUdr78sKa6HYGcekcrB1p0xbM"

# class StreamListener(tweepy.StreamListener):
#
#     def __init__(self, file_object, file_name, api = None):
#         #         self.config = config
#         #         self.consumer_key = config['consumer_key']
#         #         self.consumer_secret = config['consumer_secret']
#         #         self.access_key = config['access_key']
#         #         self.access_secret = config['access_secret']
#         super(StreamListener, self).__init__(self, file_object, file_name)
#         self.count = 0
#         self.file_object = None
#         self.file_name = None
#
#         self.summary = pd.DataFrame()
#         self.cpercentage = pd.DataFrame()
#         self.file_name_list = []
#
#     def on_status(self, status, file_object, file_name):
#         tweet = {}
#         if not pd.isnull(status.user.location) and status.text.startswith("RT") == False:
#
#             tweet['id'] = status.id
#             tweet['created_at'] = status.created_at.isoformat()
#             tweet['text'] = status.text
#             tweet['user'] = {'location': status.user.location}
#             tweet['geo'] = status.geo
#
#             if self.file_object is None:
#                 self.file_name = str(int(datetime.datetime.now().timestamp()))
#                 self.file_name_list.append(self.file_name)
#                 with open(self.file_name + '.json', "w", encoding="utf-8") as self.file_object:
#                     json.dump({'results': [tweet]}, self.file_object, indent=4)
#                 self.count += 1
#                 # with open("time.txt", "w") as f:
#                 #     dateArray = datetime.datetime.fromtimestamp(int(file_name))
#                 #     f.write(str(dateArray) + '\n')
#                 # f.close()
#                 print(self.file_name)
#
#                 store_tweets = {'id': tweet['id'], 'time': tweet['created_at'], 'text': tweet['text'],
#                                 'location': tweet['user']['location'], 'geo': tweet['geo']}
#
#             elif self.count == 300:
#
#                 self.file_object.close()
#
#                 SentimentAnalysis()
#
#                 WordCloud_plot()
#
#                 Line_plot()
#
#                 Percentage_table()
#
#                 self.count = 1
#                 self.file_name = str(int(datetime.datetime.now().timestamp()))
#                 self.file_name_list.append(self.file_name)
#                 with open(self.file_name + '.json', "w", encoding="utf-8") as self.file_object:
#                     json.dump({'results': [tweet]}, self.file_object, indent=4)
#                 print("New file created")
#
#                 with open("time.txt", "w") as f:
#                     for i in range(len(file_name_list)):
#                         dateArray = datetime.datetime.fromtimestamp(int(file_name_list[i]))
#                         f.write(str(dateArray) + '\n')
#                 f.close()
#
#             else:
#                 with open(self.file_name + '.json', "r", encoding="utf-8") as self.file_object:
#                     results = json.load(self.file_object)['results']
#                     self.file_object.close()
#
#                 results.append(tweet)
#
#                 with open(self.file_name + '.json', "w", encoding="utf-8") as self.file_object:
#                     json.dump({'results': results}, self.file_object)
#                     self.count += 1
#                     # with open("time.txt", "w") as f:
#                     #     dateArray = datetime.datetime.fromtimestamp(int(file_name))
#                     #     f.write(str(dateArray) + '\n')
#                     # f.close()
#                     store_tweets = {'id': tweet['id'], 'time': tweet['created_at'], 'text': tweet['text'],
#                                     'location': tweet['user']['location'], 'geo': tweet['geo']}
#             for t in self.file_object:
#                 if t in results:
#                     db.save(store_tweets)
#                     break
#             print(self.count)
#
#     def on_error(self, status_code):
#         print("Encountered streaming error (", status_code, ")")
#         sys.exit()
#
#     def on_timeout(self):
#         print(sys.stderr, 'Timeout...')
#         return True
#         print("Stream restarted")
#
#     def SentimentAnalysis(self, file_name):
#         with open(self.file_name + '.json') as a:
#             data = json.load(a)
#
#         # print(len(data['results']))
#         SentimentAnalysis_result = []
#
#         for i in range(len(data['results'])):
#             result_dict = {}
#             data_str = remove_features(fix_abbreviation(strip_non_ascii(data["results"][i]["text"])))
#             polarity = sentiment_analysis(data_str)
#             attitude = condition(polarity)
#             result_dict['order'] = str(i)
#             result_dict['polarity'] = float(str(polarity)[:5])
#             result_dict['attitude'] = attitude
#             SentimentAnalysis_result.append(result_dict)
#
#         sentiment_score = {'order': result_dict['order'], 'polarity': result_dict['polarity'],
#                            'attitude': result_dict['attitude']}
#         db1.save(sentiment_score)
#
#         filename_result = 'SA_result' + self.file_name + '.json'
#         with open(filename_result,'w') as file_obj:
#             json.dump(SentimentAnalysis_result, file_obj)
#     def WordCloud_plot(self, file_name):
#         with open(self.file_name + '.json','r') as a:
#             data = json.load(a)
#
#         words = []
#         for i in range(len(data['results'])):
#             data_text = {}
#             data_str = strip_non_ascii(data["results"][i]["text"])
#             if check_blanks(data_str) == 'True':
#                 continue
#             elif check_lang(data_str) == 'en':
#                 data_fix_abbreviation = fix_abbreviation(data_str)
#                 data_remove_features = remove_features(data_fix_abbreviation)
#                 data_remove_stops = remove_stops(data_remove_features)
#                 data_tag_and_remove = tag_and_remove(data_remove_stops)
#                 data_lemmatize = lemmatize(data_tag_and_remove)
#                 data_final = to_word(data_lemmatize)
#                 words.append(data_final)
#         #print(words)
#
#         text = [num for elem in words for num in elem]
#         stopwords = ['love','work','week','way','watch','fuck','use','be','want','good','great',
#                      'thanks','amp','see','go','think','people','today','say','get','time','day',
#                      'look','make','know','need','thank','come','do','new','take','thing','take',
#                      'make','know','need','new','year','many','melbourne','austrilia']
#         text_s = " ".join(text)
#
#         # Generate a word cloud image
#         colosseum_mask = np.array(Image.open('VIC_shape.jpeg'))
#         colors = ImageColorGenerator(colosseum_mask)
#         wordcloud = WordCloud(mask=colosseum_mask,
#                              stopwords=stopwords,
#                              background_color='white',
#                              colormap='tab20')
#         wordcloud.generate_from_text(text_s)
#         wordcloud.to_file('WC' + self.file_name + '.png')
#         plt.figure(figsize=(18,12))
#         #MEDIA_ROOT = os.path.join(BASE_DIR, './ccc_backend/static/media')
#         #MEDIA_URL = '/media/'
#         plt.savefig(os.path.join(os.path.join(MEDIA_ROOT)+'WC_current.png'))
#         plt.imshow(wordcloud)
#         plt.axis("off")
#         current = os.path.join(os.path.join(MEDIA_ROOT)+ '/' + 'WC_current.png')
#         previous = os.path.join(os.path.join(MEDIA_ROOT)+ '/' + 'WC_previous.png')
#         before = os.path.join(os.path.join(MEDIA_ROOT)+ '/' + 'WC_before_the_previous.png')
#         if os.path.exists((MEDIA_ROOT) + '/' +'WC_before_the_previous.png') == True:
#             os.remove(before)
#             os.renames(previous, before)
#             os.renames(current, previous)
#             plt.savefig(os.path.join(os.path.join(MEDIA_ROOT) + '/' + 'WC_current.png'))
#         elif os.path.exists((MEDIA_ROOT) + '/' +'WC_previous.png') == True:
#             os.remove(before)
#             os.renames(previous, before)
#             os.renames(current, previous)
#             plt.savefig(os.path.join(os.path.join(MEDIA_ROOT) + '/' + 'WC_current.png'))
#         elif os.path.exists((MEDIA_ROOT) + '/' +'WC_current.png') == True:
#             os.remove(current)
#             os.rename(previous, current)
#             plt.savefig(os.path.join(os.path.join(MEDIA_ROOT) + '/' + 'WC_current.png'))
#         else:
#             plt.savefig(os.path.join(os.path.join(MEDIA_ROOT) + '/' + 'WC_before_the_previous.png'))
#             # plt.savefig(os.path.join(os.path.join(MEDIA_ROOT)+'/'+'WC_before_the_previous.png'))
#         plt.show()
#
#     def Line_plot(self, summary, file_name):
#         d = pd.read_json('SA_result' + self.file_name + '.json')
#         pcount = d.groupby(by=['attitude']).size()
#         time_plot = str(datetime.datetime.fromtimestamp(int(self.file_name)))
#
#         s = pd.DataFrame()
#         s['time'] = [time_plot,time_plot,time_plot]
#         s['sentiment'] = ['positive', 'neutral', 'negative']
#         s['count'] = [pcount['positive'], pcount['neutral'], pcount['negative']]
#         s['total'] = [len(d), len(d), len(d)]
#         s['percentage'] = s['count'] / s['total']
#
#         self.summary = self.summary.append(s,ignore_index=True)
#
#         print(self.summary)
#         fig1 = px.line(self.summary, x="sentiment", y="percentage",color="time")
#         fig1.write_json('line_chart'+ self.file_name + '.json')
#         fig1.write_image('line2.png', engine="kaleido")
#         fig1.show()
#
#     def Percentage_table(self, cpercentage, file_name):
#         vacc_filter = ['vaccine', 'vaccination', 'vaccinate', 'injection', 'inject',
#                        'rna', 'inactivated', 'Pfizer', 'BioNTech', 'AstraZeneca', 'Oxford']
#         cov_filter = ['covid', 'covid-19', 'coronavirus', 'coronavid19']
#
#         with open(self.file_name + '.json', 'r') as a:
#             data = json.load(a)
#
#         vacfilter_count = 0
#         covfilter_count = 0
#         words = []
#         for i in range(len(data['results'])):
#             data_text = {}
#             data_str = strip_non_ascii(data["results"][i]["text"])
#             if check_blanks(data_str) == 'True':
#                 continue
#             elif check_lang(data_str) == 'en':
#                 data_fix_abbreviation = fix_abbreviation(data_str)
#                 data_remove_features = remove_features(data_fix_abbreviation)
#                 data_remove_stops = remove_stops(data_remove_features)
#                 data_tag_and_remove = tag_and_remove(data_remove_stops)
#                 data_lemmatize = lemmatize(data_tag_and_remove)
#                 data_final = to_word(data_lemmatize)
#                 words.append(data_final)
#                 for j in vacc_filter:
#                     if j in data_final:
#                         vacfilter_count += 1
#                         break
#                 for k in cov_filter:
#                     if k in data_final:
#                         covfilter_count += 1
#                         break
#         f = pd.read_json(self.file_name + '.json')
#         time_plot = str(datetime.datetime.fromtimestamp(int(self.file_name)))
#         c = pd.DataFrame()
#         c['time'] = [time_plot, time_plot]
#         c['keyword'] = ['Vaccine related', 'Covid related']
#         c['count'] = [vacfilter_count, covfilter_count]
#         c['total'] = [len(f), len(f)]
#         c['percentage'] = c['count'] / c['total']
#         self.cpercentage = self.cpercentage.append(c, ignore_index=True)
#         print(self.cpercentage)

def SentimentAnalysis():
    with open(file_name + '.json') as a:
        data = json.load(a)

    # print(len(data['results']))
    SentimentAnalysis_result = []

    for i in range(len(data['results'])):
        result_dict = {}
        data_str = remove_features(fix_abbreviation(strip_non_ascii(data["results"][i]["text"])))
        polarity = sentiment_analysis(data_str)
        attitude = condition(polarity)
        result_dict['order'] = str(i)
        result_dict['polarity'] = float(str(polarity)[:5])
        result_dict['attitude'] = attitude
        SentimentAnalysis_result.append(result_dict)

        sentiment_score = {'order': result_dict['order'], 'polarity': result_dict['polarity'],
                           'attitude': result_dict['attitude']}
        db1.save(sentiment_score)


    filename_result = 'SA_result' + file_name + '.json'
    with open(filename_result,'w') as file_obj:
        json.dump(SentimentAnalysis_result, file_obj)

def WordCloud_plot():
    with open(file_name + '.json','r') as a:
        data = json.load(a)

    words = []
    for i in range(len(data['results'])):
        data_text = {}
        data_str = strip_non_ascii(data["results"][i]["text"])
        if check_blanks(data_str) == 'True':
            continue
        elif check_lang(data_str) == 'en':
            data_fix_abbreviation = fix_abbreviation(data_str)
            data_remove_features = remove_features(data_fix_abbreviation)
            data_remove_stops = remove_stops(data_remove_features)
            data_tag_and_remove = tag_and_remove(data_remove_stops)
            data_lemmatize = lemmatize(data_tag_and_remove)
            data_final = to_word(data_lemmatize)
            words.append(data_final)
    #print(words)

    text = [num for elem in words for num in elem]
    stopwords = ['love','work','week','way','watch','fuck','use','be','want','good','great',
                 'thanks','amp','see','go','think','people','today','say','get','time','day',
                 'look','make','know','need','thank','come','do','new','take','thing','take',
                 'make','know','need','new','year','many','melbourne','austrilia']
    text_s = " ".join(text)

    # Generate a word cloud image
    colosseum_mask = np.array(Image.open('VIC_shape.jpeg'))
    colors = ImageColorGenerator(colosseum_mask)
    wordcloud = WordCloud(mask=colosseum_mask,
                         stopwords=stopwords,
                         background_color='white',
                         colormap='tab20')
    wordcloud.generate_from_text(text_s)
    wordcloud.to_file('WC' + file_name + '.png')
    plt.figure(figsize=(18,12))
    #MEDIA_ROOT = os.path.join(BASE_DIR, './ccc_backend/static/media')
    #MEDIA_URL = '/media/'
    plt.imshow(wordcloud)
    plt.axis("off")

    current = os.path.join(os.path.join(MEDIA_ROOT)+ '/' + 'WC_current.png')
    previous = os.path.join(os.path.join(MEDIA_ROOT)+ '/' + 'WC_previous.png')
    before = os.path.join(os.path.join(MEDIA_ROOT)+ '/' + 'WC_before_the_previous.png')
    if os.path.exists((MEDIA_ROOT) + '/' +'WC_before_the_previous.png') == True:
        os.remove(before)
        os.renames(previous, before)
        os.renames(current, previous)
        plt.savefig(os.path.join(os.path.join(MEDIA_ROOT) + '/' + 'WC_current.png'))
    elif os.path.exists((MEDIA_ROOT) + '/' +'WC_previous.png') == True:
        os.remove(before)
        os.renames(previous, before)
        os.renames(current, previous)
        plt.savefig(os.path.join(os.path.join(MEDIA_ROOT) + '/' + 'WC_current.png'))
    elif os.path.exists((MEDIA_ROOT) + '/' +'WC_current.png') == True:
        os.remove(current)
        os.rename(previous, current)
        plt.savefig(os.path.join(os.path.join(MEDIA_ROOT) + '/' + 'WC_current.png'))
    else:
        plt.savefig(os.path.join(os.path.join(MEDIA_ROOT) + '/' + 'WC_before_the_previous.png'))
        # plt.savefig(os.path.join(os.path.join(MEDIA_ROOT)+'/'+'WC_before_the_previous.png'))
        plt.show()

def Line_plot():
    global summary
    d = pd.read_json('SA_result' + file_name + '.json')
    pcount = d.groupby(by=['attitude']).size()
    time_plot = str(datetime.datetime.fromtimestamp(int(file_name)))

    s = pd.DataFrame()
    s['time'] = [time_plot,time_plot,time_plot]
    s['sentiment'] = ['positive', 'neutral', 'negative']
    s['count'] = [pcount['positive'], pcount['neutral'], pcount['negative']]
    s['total'] = [len(d), len(d), len(d)]
    s['percentage'] = s['count'] / s['total']

    summary = summary.append(s)

    print(summary)

    fig1 = px.line(summary, x="sentiment", y="percentage",color="time")

    fig1.write_json('line_chart'+ file_name + '.json')
    fig1.write_image(os.path.join(os.path.join(MEDIA_ROOT) + '/' + 'line2.png'))
    fig1.show()

def Percentage_table():
    global cpercentage
    vacc_filter = ['vaccine', 'vaccination', 'vaccinate', 'injection', 'inject',
                   'rna', 'inactivated', 'Pfizer', 'BioNTech', 'AstraZeneca', 'Oxford']
    cov_filter = ['covid', 'covid-19', 'coronavirus', 'coronavid19']

    with open(file_name + '.json', 'r') as a:
        data = json.load(a)

    vacfilter_count = 0
    covfilter_count = 0
    words = []
    for i in range(len(data['results'])):
        data_text = {}
        data_str = strip_non_ascii(data["results"][i]["text"])
        if check_blanks(data_str) == 'True':
            continue
        elif check_lang(data_str) == 'en':
            data_fix_abbreviation = fix_abbreviation(data_str)
            data_remove_features = remove_features(data_fix_abbreviation)
            data_remove_stops = remove_stops(data_remove_features)
            data_tag_and_remove = tag_and_remove(data_remove_stops)
            data_lemmatize = lemmatize(data_tag_and_remove)
            data_final = to_word(data_lemmatize)
            words.append(data_final)
            for j in vacc_filter:
                if j in data_final:
                    vacfilter_count += 1
                    break
            for k in cov_filter:
                if k in data_final:
                    covfilter_count += 1
                    break
    f = pd.read_json(file_name + '.json')
    time_plot = str(datetime.datetime.fromtimestamp(int(file_name)))
    c = pd.DataFrame()
    c['time'] = [time_plot, time_plot]
    c['keyword'] = ['Vaccine related', 'Covid related']
    c['count'] = [vacfilter_count, covfilter_count]
    c['total'] = [len(f), len(f)]
    c['percentage'] = c['count'] / c['total']
    cpercentage = cpercentage.append(c)
    print(cpercentage)


class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        global file_object, count, file_name, store_count
        tweet = {}
        if not pd.isnull(status.user.location) and status.text.startswith("RT") == False:

            tweet['id'] = status.id
            tweet['created_at'] = status.created_at.isoformat()
            tweet['text'] = status.text
            tweet['user'] = {'location': status.user.location}
            tweet['geo'] = status.geo

            if file_object is None:
                file_name = str(int(datetime.datetime.now().timestamp()))
                file_name_list.append(file_name)
                with open(file_name + '.json', "w", encoding="utf-8") as file_object:
                    json.dump({'results': [tweet]}, file_object, indent=4)
                count += 1
                # with open("time.txt", "w") as f:
                #     dateArray = datetime.datetime.fromtimestamp(int(file_name))
                #     f.write(str(dateArray) + '\n')
                # f.close()
                print(file_name)

                store_tweets = {'id': tweet['id'], 'time': tweet['created_at'], 'text': tweet['text'],
                                'location': tweet['user']['location'], 'geo': tweet['geo']}
                db.save(store_tweets)

            elif count == 300:

                file_object.close()

                SentimentAnalysis()

                WordCloud_plot()

                Line_plot()

                #Percentage_table()

                count = 1
                store_count = 1
                file_name = str(int(datetime.datetime.now().timestamp()))
                file_name_list.append(file_name)
                with open(file_name + '.json', "w", encoding="utf-8") as file_object:
                    json.dump({'results': [tweet]}, file_object, indent=4)
                print("New file created")

                with open("time.txt", "w") as f:
                    for i in range(len(file_name_list)):
                        dateArray = datetime.datetime.fromtimestamp(int(file_name_list[i]))
                        f.write(str(dateArray) + '\n')
                f.close()


            else:
                with open(file_name + '.json', "r", encoding="utf-8") as file_object:
                    results = json.load(file_object)['results']
                    file_object.close()

                results.append(tweet)

                with open(file_name + '.json', "w", encoding="utf-8") as file_object:
                    json.dump({'results': results}, file_object)
                    count += 1
                    # with open("time.txt", "w") as f:
                    #     dateArray = datetime.datetime.fromtimestamp(int(file_name))
                    #     f.write(str(dateArray) + '\n')
                    # f.close()
                    store_tweets = {'id': tweet['id'], 'time': tweet['created_at'], 'text': tweet['text'],
                                    'location': tweet['user']['location'], 'geo': tweet['geo']}
                    db.save(store_tweets)
            print(count)

    def on_error(self, status_code):
        print("Encountered streaming error (", status_code, ")")
        sys.exit()

    def on_timeout(self):
        print(sys.stderr, 'Timeout...')
        return True
        print("Stream restarted")

# def Fun_start(consumer_key, consumer_secret, access_key, access_secret):
#     auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_key, access_secret)
#     api = tweepy.API(auth)
#     streamListener = StreamListener()
#     stream = tweepy.Stream(auth=api.auth, listener=streamListener, tweet_mode='extended')
#     stream.filter(languages = ['en'],locations = [144.9,-37.8,145,-37.7])
#     #stream.filter(languages=['en'], track=['vaccine'], locations=[144.9, -37.8, 145, -37.7])

def Fun_start():
    consumer_key = "7PC3L2O8ywCONU4ZuJ5h757mv"
    consumer_secret = "MMhJhIIolKU3ONdXpLC6oGzOwYGYwYgzMILc3etxZ0yjuNtdze"
    access_key = "1115405592372187136-19lxDiitrBBDSdSaLdyqgK3fJzJxWT"
    access_secret = "w2FsaXLITsGDy1PsRvqkdUdr78sKa6HYGcekcrB1p0xbM"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    streamListener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=streamListener, tweet_mode='extended')
    #stream.filter(languages = ['en'],locations = [144.9,-37.8,145,-37.7])
    stream.filter(languages=['en'], track=['vaccine'], locations=[144.9, -37.8, 145, -37.7])


if __name__ == "__main__":
    count = 0
    file_object = None
    file_name = None
    summary = pd.DataFrame()
    cpercentage = pd.DataFrame()

    file_name_list = []
    Fun_start()


