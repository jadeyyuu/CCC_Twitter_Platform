#function(doc) {
    if(doc.time && doc.text) {
        emit(doc.time, doc.text);
    }
}


#Map function
#function(doc) { if(doc.date && doc.text) { var created = new Date(doc.date);emit([created.getFullYear(),created.getMonth()+1,created.getDate()],doc.text); }}


curl -X PUT http://admin:password@172.26.131.236:5984/melb201508/_design/my_ddoc\
     -d '{"views":{"my_filter":{"map":
         "function(doc) { if(doc.date && doc.text) { var created = new Date(doc.date);emit([created.getFullYear(),created.getMonth(),created.getDate()],doc.text); }}"}}}'


curl -X PUT http://admin:password@172.26.131.236:5984/melb2017/_design/my_ddoc\
     -d '{"views":{"my_filter":{"map":
         "function(doc){var created = new Date(doc.date);\
emit([created.getFullYear(),created.getMonth()+1,created.getDate(),doc.text],doc);
}"}}}'

curl -X GET http://admin:password@172.26.131.236:5984/test_json/_design/my_ddoc/_view/my_filter


curl -X GET http://admin:password@172.26.131.236:5984/melb201508/_design/my_ddoc/_view/datefilter?startkey=[2015,8,5]&endkey=[2015,8,7]&group_level=0


curl -X GET http://admin:password@172.26.131.236:5984/insmelb201531_84/_design/my_ddoc/_view/my_filter?startkey="2015-03-01 08:06:53"&endkey="2015-05-01 00:00:00"


curl -X GET http://admin:password@172.26.131.236:5984/melb201508/_design/my_ddoc/_view/datefilter
