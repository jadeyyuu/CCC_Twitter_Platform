Bearer 
AAAAAAAAAAAAAAAAAAAAAKriOwEAAAAAklsKZE9KcXC0u7i5NnEyJ1RiQAo%3DertqyvHpDngap6aoujTiTswHsnpzR7fF6O7c69RcB91eJOxNLL

 curl --request POST \
  --url https://api.twitter.com/1.1/tweets/search/fullarchive/CCCno3.json \
  --header 'authorization: Bearer AAAAAAAAAAAAAAAAAAAAAKjKPAEAAAAAX4o9OMNC4jl4%2Bvi%2F%2FtaKoK%2Bi%2BmA%3DKGKxqerSgC4wELOGbCz85jALMYOghUzh8IpAPEYqZ2h3MIS4PH' \
  --header 'content-type: application/json' \
  --data '{

                
                "query":"lang:en place_country:AU place:Victoria",

                "fromDate":"202003010000",
                "toDate":"202012310720"
                }' \
| jq . > 12312.json
30 days3.30- 4.28


 curl --request POST \
  --url https://api.twitter.com/1.1/tweets/search/30day/APP30.json \
  --header 'authorization: Bearer AAAAAAAAAAAAAAAAAAAAABKaPAEAAAAAOnrccm6HXLXIS3QETlupYjwhvD4%3D0mTHWWiOe6Mlr8NywbMTcKcouhpORRaVJx8XEB1TFhUUaWUYKa' \
  --header 'content-type: application/json' \
  --data '{
                "query":"lang:en place_country:AU place:Victoria",
                "fromDate":"202104021800",
                "toDate":"202104282010"
                }' \
| jq . > 042820.json




 curl "http://45.113.232.90/couchdbro/twitter/_design/twitter/_view/summary" \
-G \
--data-urlencode 'start_key=["melbourne",2017,1,1]’ \
--data-urlencode 'end_key=["melbourne",2017,1,31]' \
--data-urlencode 'reduce=false' \
--data-urlencode 'include_docs=true' \
--user "readonly:ween7ighai9gahR6" \
-o twitter.json\
|jq . > 201701.json

 curl "http://45.113.232.90/couchdbro/twitter/_design/instagram/_view/summary" \
-G \
--data-urlencode 'start_key=["melbourne",2015,1,1]’ \
--data-urlencode 'end_key=["melbourne",2015,1,31]' \
--data-urlencode 'reduce=false' \
--data-urlencode 'include_docs=true' \
--user "readonly:ween7ighai9gahR6" \
-o /cccass2/20152016/2015melb01.json\


curl "http://45.113.232.90/couchdbro/twitter/_design/twitter/_view/summary" \
 -G \
 --data-urlencode 'start_key=["melbourne",2015,1,1]’ \
 --data-urlencode 'end_key=["melbourne",2015,1,31]' \
> --data-urlencode 'reduce=false' \
> --data-urlencode 'include_docs=true' \
> --user "readonly:ween7ighai9gahR6" \
-o 2015melb01.json

export READONLY_PASSWORD='cainaimeeshaLu4Lejoo9ooW4jiopeid'
export EP='http://couchdb.socmedia.bigtwitter.cloud.edu.au'
curl -G "${EP}/instagram/_design/instagram/_view/summary"\
  --data-urlencode reduce=false\
  --data-urlencode include_docs=true\
  --data-urlencode 'start_key=["melbourne", 2017, 3, 1]  '\
  --data-urlencode 'end_key=["melbourne", 2017, 7, 7]  '\
  --user "readonly:${READONLY_PASSWORD}"\
|jq . > insmelb201703_07.json


curl -G "${EP}/twitter/_design/twitter/_view/summary"\
  --data-urlencode group_level=4\
  --user "readonly:${READONLY_PASSWORD}"
curl -G "${EP}/instagram/_design/instagram/_view/summary"\
  --data-urlencode group_level=4\
  --user "readonly:${READONLY_PASSWORD}" 

export READONLY_PASSWORD='cainaimeeshaLu4Lejoo9ooW4jiopeid'
export EP='http://couchdb.socmedia.bigtwitter.cloud.edu.au'
curl -G "${EP}/instagram/_design/instagram/_view/summary"\
  --data-urlencode reduce=false\
  --data-urlencode include_docs=true\
  --data-urlencode 'start_key=["melbourne", 2015, 3, 1] '\
  --data-urlencode 'end_key=["melbourne", 2015, 8, 3] '\
  --user "readonly:${READONLY_PASSWORD}"\
|jq . > melb201531_83ins.json

export READONLY_PASSWORD='cainaimeeshaLu4Lejoo9ooW4jiopeid'
export EP='http://couchdb.socmedia.bigtwitter.cloud.edu.au'
curl -G "${EP}/instagram/_design/instagram/_view/summary"\
  --data-urlencode reduce=false\
  --data-urlencode include_docs=true\
  --data-urlencode 'start_key=["melbourne", 2017, 7, 1] '\
  --data-urlencode 'end_key=["melbourne", 2017, 7, 1] '\
  --user "readonly:${READONLY_PASSWORD}"\
|jq . > 20171.json
curl -G "${EP}/twitter/_design/twitter/_view/summary"\
--data-urlencode reduce=false\
--data-urlencode in
clude_docs=true\
--data-urlencode 'start_key=["melbourne", 2015, 2, 01]"\
--data-urlencode 'end_key=["melbourne", 2015, 2, 28]"\
--user "readonly:${READONLY_PASSWORD}"
-o 2015melb01.json



Json combine
jq -s '{ results: map(.results) }' 2020*.json>2020all.json


