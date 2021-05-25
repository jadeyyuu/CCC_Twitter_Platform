# Web_server

## 1.Prepare ENV
Django==3.2.3  
CouchDB==1.2  
plotly==4.14.3  
tweepy  
  
  
## 2.Run HARVERST module to get live tweets
`nohup python3  harvestest.py > python.log 2>&1 &`
  
  
## 3.Run Django Server
`Python3 manage.py runserver <ip>:8000`
