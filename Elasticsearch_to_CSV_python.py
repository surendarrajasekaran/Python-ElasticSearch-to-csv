#AUTHOR SURENDAR RAJASEKARAN


import elasticsearch
import unicodedata
import csv

es = elasticsearch.Elasticsearch(["YOUR ENDPOINT:PORT NUMBER"])
# this returns up to 1000 Rows, adjust to your needs
res = es.search(index="INDEX NAME", body={"query": {"match_all": {}}},size=10000)
sample = res['hits']['hits']

#WRITING LOGS INTO CSV FILE
with open('logs.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    #CHANGE THE LOOP DICT KEY ACCORDING TO YOUR LOGS
    writer.writerow(["MESSAGE","SOURCE"])
    for hit in sample:
        msg=hit['_source']['message']
        status=hit['_source']['source']       
        writer.writerow([msg,status,method,response,response_time,url,date,timestamp,time])
