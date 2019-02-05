from GetServiceTicket import *
from tabulate import tabulate
def GetNetworkDevices(aTicket,url,aData=None):
    header = {"X-Auth-Token":aTicket,"content-type":"application/json"}
    requestdevices=requests.get(url,data=None,headers=header,verify=False)
    request_json=requestdevices.json()
    devices=request_json["response"]
    device_list=[]
    i=0
    for item in devices:
        i+=1
        device_list.append ([i ,item["hostname"],item["type"],item["managementIpAddress"],item["softwareVersion"]])
        print (tabulate(device_list, headers=["number","hostname","type","ip","softwareVersion"],tablefmt ="rst"))
    return device_list
def ASK_USER_INPUT(aDevice_list):
    user_input=int(input("Введите номер для получения конфигурации: "))
    if user_input in range (1,len(aDevice_list)+1):
        id = aDevice_list[user_input-1]
        return id
def GetConfiguration(aTicket,url,aData=None):
    header = {"X-Auth-Token":aTicket,"content-type":"application/json"}
    requestdevices=requests.get(url,data=None,headers=header,verify=False)
    request_json=requestdevices.json()
    print (request_json["response"].replace("\r\n","\n"))
def main():
    ticket = GetServiceTicket()
    device_list =GetNetworkDevices (ticket, "https://"+ControllerIP+"/api/v1/network-device")
    id = ASK_USER_INPUT(device_list)
    GetConfiguration(ticket,"https://"+ControllerIP+"/api/v1/network-device"+id+"/config")
main()