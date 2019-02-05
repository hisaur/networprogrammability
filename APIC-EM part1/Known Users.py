from GetServiceTicket import *
def GetUserList(aTicket,url,aData=None):
    header = {"X-Auth-Token":aTicket,"content-type":"application/json"}
    requestuser = requests.get (url,data=None,headers=header,verify=False)
    requestuser_json= requestuser.json()
    print (requestuser_json)
def main():
    ticket=GetServiceTicket()
    GetUserList(ticket, "https://" + ControllerIP + "/api/v1/user")
    
main()
