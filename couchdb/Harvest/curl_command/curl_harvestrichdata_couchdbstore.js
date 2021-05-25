curl -XGET "http://admin:password@172.26.131.236:5984/"

curl -XPOST "http://admin:password@172.26.131.236:5984/_cluster_setup"\
    --header "Content-Type: application/json" --data "{\"action\": \"finish_cluster\"}"


GET http://admin:password@172.26.131.236:5984/img
Content-Type: application/json
Accept: application/json

curl -X GET http://admin:password@172.26.131.236:5984/img

cd couchdb
curl -XPOST "http://admin:password@172.26.131.236:5984/harvest " --header "Content-Type: application/json" \
  --data @./bar15_17.json











curl -XPOST "http://admin:password@172.26.131.236:5984/img  " --header "Content-Type: application/json" \
  --data @./age_pie_Hume.json

curl -XPOST "http://admin:password@172.26.131.236:5984/melb201511/_bulk_docs  " --header "Content-Type: application/json" \
  --data @./test.json


cd couchdb
curl -XPOST "http://${user}:${pass}@${masternode}:5984/twitter/_bulk_docs " --header "Content-Type: application/json" \
  --data @./twitter/data.json

http://172.26.131.236:5984/_utils

curl -G "http://couchdb.socmedia.bigtwitter.cloud.edu.au/twitter/_design/twitter/_view/summary"\
  --data-urlencode reduce=false\
  --data-urlencode include_docs=true\
  --data-urlencode 'start_key=["melbourne", 2015, 1, 01]’\
  --data-urlencode 'end_key=["melbourne", 2015, 1, 31]’\
  --user "readonly: cainaimeeshaLu4Lejoo9ooW4jiopeid”\
-o /twitter201501.json



curl -G "${EP}/twitter/_design/twitter/_view/summary"\
  --data-urlencode reduce=false\
  --data-urlencode include_docs=true\
  --data-urlencode 'start_key=["melbourne", 2015, 10, 1] '\
  --data-urlencode 'end_key=["melbourne", 2015, 10, 31] '\
  --user "readonly:${READONLY_PASSWORD}"\
|jq . > 201510melb.json