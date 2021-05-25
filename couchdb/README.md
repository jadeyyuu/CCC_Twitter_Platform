# couchdb


Couchdb Instruction


1. Apache Couchdb website

Using the Apache Couchdb website with the url http://172.26.131.236:5984/_utils/#

we could use this website page to operate our couchdb system.


2. Create file in couchdb

In the Apache Couchdb page we could directly create the database through the webpage.
like the figure shows
![create](https://user-images.githubusercontent.com/70568760/119521063-64056880-bdad-11eb-9189-6785b4b55d3c.jpg)

Also,we could write the python script to achieve this.

>>>import couchdb

>>>couch = couchdb.Server('http://admin:password@172.26.134.19:5984')

>>db = couch.create("file")

3.Upload the data to the exist file in couchdb

We could use the curl command to straightly upload the json format file to the exist file.

curl -XPOST "http://admin:password@172.26.131.236:5984/file " \
--header "Content-Type: application/json" \
  --data @./image.json
  
If the file too large, we need to process the file and use _bulks_doc to store.
Or we could write python script to process the content and split the json to each piece of small dictionary to store.

4. Retrieve the data
 
If we uploaded the json file successfully, there would be a pair of _id and _rev.
Then we could use this pair of _id and _rev to obtain our data.
In python script

>>>data = db["%_id"]
 
Otherwise, we could straightly see the data content in Apache coughdb file page.
 
5. Delete the file

In python

>>> db.delete(doc)
>>> couch.delete('file')

6.Map and reduce

We could use map funtion to filter the data. that we needed in each document and use the reduced view to witness the amount value of the filtered data. 
For instance

Map function looks like:

function(doc) { if(doc.date && doc.text)

{ var created = new Date(doc.date);

emit([created.getFullYear(),created.getMonth()+1,created.getDate()],doc.text); }}

Using the curl command to put it in the design "my_ddoc" and views "my_filter"

curl -X PUT http://admin:password@172.26.131.236:5984/melb201508/_design/my_ddoc\
     -d '{"views":{"my_filter":{"map":
         "function(doc) { if(doc.date && doc.text) 
         { var created = newDate(doc.date);
         emit([created.getFullYear(),created.getMonth(),created.getDate()],doc.text); }}"}}}'

Also, in the Apache couchdb we coudld directly edit in the figure below, which is quite convenient.

![reduce](https://user-images.githubusercontent.com/70568760/119520267-babe7280-bdac-11eb-903c-9ccf162242b3.jpg)


