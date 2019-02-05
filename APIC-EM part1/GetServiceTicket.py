import json
import requests
import urllib3
urllib3.disable_warnings() 
ControllerIP = "devnetapi.cisco.com/sandbox/apic_em"

def GetServiceTicket():
    ControllerIP = "devnetapi.cisco.com/sandbox/apic_em"
    payload = {"username":"devnetuser","password":"Cisco123!"}
    url = "https://"+ControllerIP+"/api/v1/ticket"
    response = requests.post(url,data=json.dumps(payload),headers = {"content-type":"application/json"}, verify=False)
    response_json=response.json()
    ticket=response_json ["response"] ["serviceTicket"]
    print ("ticket: ", ticket)
    return ticket
