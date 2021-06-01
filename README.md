
# Twitter Analysis 

## Team Member
* [Xinyu Zeng- 1234798](https://github.com/jadeyyuu)
* [Yuxuan Liu - 743365](https://github.com/PatrickLiuyx)
* [Jing Yang - 1250442](https://github.com/ChelseaYang1130)
* [Yilin Yu - 965720](https://github.com/Hieler)
* [Chen Zhou - 987776](https://github.com/CZZHO)

## Project Structure

### Deployment Operation 
1. Ansible creates 4 hosts with one click
2. Docker runs 3 CouchDB instances
3. Ansible controls Docker-compose with services on each instances 


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

    
