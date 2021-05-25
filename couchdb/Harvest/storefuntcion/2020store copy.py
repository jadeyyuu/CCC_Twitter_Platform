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

db = couch['harvest']


from datetime import datetime

import time

with open('03.json') as f:
    btweet = json.load(f)



tweetlst  = btweet['results']

for i in range(len(tweetlst)):
    for j in range(len(tweetlst[i])):


            dataDict = {}
            dataDict["id"] = tweetlst[i][j]["id"]
            dataDict["user"] = tweetlst[i][j]["user"]["screen_name"]

            dataDict['text'] = tweetlst[i][j]['text']

            if tweetlst[i][j]["created_at"] != None:
                stringTime = tweetlst[i][j]["created_at"]
                dataDict["date"] = datetime.strptime(stringTime, '%a %b %d %H:%M:%S %z %Y').strftime(
                    '%Y-%m-%d %H:%M:%S%z')



            else:
                dataDict["date"] = ""





            if tweetlst[i][j]['place'] != None:
                dataDict['city'] =tweetlst[i][j]['place']['full_name']
            else:
                dataDict['city'] = ''


            db.save(dataDict)


            print('tweets upload')


