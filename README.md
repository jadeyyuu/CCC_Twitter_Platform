# CCC Project Twitter Platform Team 30

## Team Member
* [Xinyu Zeng- 1234798](https://github.com/jadeyyuu)
* [Yuxuan Liu - 743365](https://github.com/PatrickLiuyx)
* [Jing Yang - 1250442](https://github.com/ChelseaYang1130)
* [Yilin Yu - 965720](https://github.com/Hieler)
* [Chen Zhou - 987776](https://github.com/CZZHO)

## Demonstration Video links
 - Ansible: https://youtu.be/2rKPK4ZUcn4
 - CouchDB: https://youtu.be/9TnfqdsxSR8 
 - Web Platform: https://youtu.be/gCVeuToZgzY


## Project Structure

### Deployment Operation 
1. Ansible creates 4 hosts with one click
2. Docker runs 3 CouchDB instances
3. Ansible controls Docker-compose with services on each instances 

### Websever
1. Front-end deployed by bootstrap5 and jQuery
2. Back-end deployed by Django
3. CouchDB related interface
3. Object Storage interface
4. Data query interface
5. Interface joint debugging

### Historical Data Analysis
1. Pyspark DataFrame API
   - Pyspark SQL for statistical analysis
   - Pyspark MLib for Latent Dirichlet Allocation topic modelling
   - Textblob for NLP sentiment analysis
2. tweepy for steaming tweet collection
3. Plotly for interative data visulization
4. Interate with CouchDB:
   - Retrieve historical tweets data
   - Save and retrieve streaming tweets data
   - Save visualization indexes in json format

### Couchdb
Store and retrieve data from the couchdb


### Server Arrangement
Server1: 172.26.130.42
<br />Docker/
<br />CouchDB/ 
<br />Frontend/
<br />    
Server2: 172.26.131.236
<br />CouchDB/
    <br />Spark/
    <br />Backend/
    <br />Twitter API/
 <br />   
Server3: 172.26.134.19
   <br /> CouchDB/ couchdb:2.3.0
    <br />Backend/
    <br />Straming API/
 <br />  
    
Server4: 172.26.129.75
    <br />Aurin/
    <br />Investing/
