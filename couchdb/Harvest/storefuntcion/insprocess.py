import sys
import glob
import errno,time,os
import couchdb
import json



import time






from pprint import pprint

couch = couchdb.Server() # Assuming localhost:5984
#couch.resource.credentials = (USERNAME, PASSWORD)
# If your CouchDB server is running elsewhere, set it up like this:
couch = couchdb.Server('http://admin:password@172.26.134.19:5984')

db = couch['melb2017']


from datetime import datetime

import time

with open('201712nyins.json') as f:
    btweet = json.load(f)



tweetlst  = btweet['rows']

for tweet in tweetlst:

    try:

        dataDict = {}
        dataDict["id"] = tweet['doc']["user"]["id"]
        dataDict["user"] = tweet["doc"]["user"]["full_name"]

        if tweet['doc']['caption'] != None:

            dataDict["text"] = tweet["doc"]["caption"]['text']
        else:
            dataDict['text'] = ''

        if tweet["doc"]["created_time"] != None:
            stringTime = int(tweet["doc"]["created_time"])
            dataDict["date"] = time.strftime("%Y-%m-%d %H:%M:%S%z", time.localtime(stringTime))



        else:
            dataDict["date"] = ""





        if tweet['doc']['location'] != None:
            dataDict['city'] = tweet['doc']['location']
        else:
            dataDict['city'] = ''


        db.save(dataDict)


        print('o')


    except Exception as e:

        print(e)