import requests as r 

url='https://localhost:8088/services/collector/event'
authHeader = {'Authorization': 'Splunk {}'.format('ab059b45-4fe9-44e0-8812-0df21e403d20')}
payload = {
    "time": 1505501013.000,
    "event": "metric",
    "source": "disk",
    "host": "host_99",
    "fields": {
        "region": "us-west-1",
        "datacenter": "us-west-1a",
        "rack": "63",
        "os": "Ubuntu16.10",
        "arch": "x64",
        "team": "LON",
        "service": "6",
        "service_version": "0",
        "service_environment": "test",
        "path": "/dev/sda1",
        "fstype": "ext3",
        "_value": 999311222774,
        "metric_name": "total"
    }
}
result = r.post(url, headers=authHeader, json=payload, verify=False)
print (result.text)

