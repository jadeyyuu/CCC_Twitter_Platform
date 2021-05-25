import sys
import glob
import errno,time,os
import couchdb
import json










from pprint import pprint

couch = couchdb.Server() # Assuming localhost:5984
#couch.resource.credentials = (USERNAME, PASSWORD)
# If your CouchDB server is running elsewhere, set it up like this:
couch = couchdb.Server('http://admin:password@172.26.134.19:5984')

db = couch['melb2017']


from datetime import datetime

import time

with open('201710tweet.json') as f:
    btweet = json.load(f)



tweetlst  = btweet['rows']

for tweet in tweetlst:

    try:

        dataDict = {}
        dataDict["id"] = tweet["id"]
        dataDict["user"] = tweet["doc"]["user"]["screen_name"]
        dataDict["text"] = tweet["doc"]["text"]

        if tweet["doc"]["created_at"] != None:
            stringTime = tweet["doc"]["created_at"]
            dataDict["date"] = datetime.strptime(stringTime, '%a %b %d %H:%M:%S %z %Y').strftime(
                '%Y-%m-%d %H:%M:%S%z')



        else:
            dataDict["date"] = ""



        if tweet["doc"]['place'] != None and tweet['doc']['place']['full_name'] != None:
            dataDict['city'] =  tweet['doc']['place']['full_name']
        else:
            dataDict['city'] =[]




        db.save(dataDict)
        print("upload")




    except Exception as e:

        print(e)