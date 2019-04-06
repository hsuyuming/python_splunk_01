import requests as r 
import time
import datetime
import random


URL='https://localhost:8088/services/collector/event'
HEADER = {'Authorization': 'Splunk {}'.format('bf70d86a-1138-4e0a-a372-6e7e6ee4775e')}
data_dict={}
data_dict["table_name"]="event_msg"


for t in range(1554490629,1554990629):
    data_dict["row_count"]= random.randint(8000,15000)
    payload = {
        "time": t,
        "host": "0.0.0.0",
        "source": "demo",
        "event": data_dict
    }
    response = r.post(URL, headers=HEADER, json=payload, verify=False)
    print(response)






