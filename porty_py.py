import os
import socket
import datetime

os.system("clear||cls")

print("-"*60)

ip = input("Enter an IP-v4 address:  ")
start_time = datetime.datetime.now()

print("scanning for IP: "+str(ip)+"\n"+"-"*60 + "\n")
print("port\tstatus\tservice" +"\n----\t------\t-------")

#Max port number to scan upto
max_range = 2000



def portScan(ip,max_range):
    
    for port in range(1,max_range): # For scanning ports max range is (2^16 - 1) = 65535 
        try: 
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((ip,port))
            service_name = socket.getservbyport(port,'tcp')
            print(str(port) + "\topen\t"+str(service_name))
            s.close()
        except socket.error:
            pass

#For windows connection timeout needs to be declared
#Default set to 1 us
timeout = 0.000001

def portScanWin(ip,max_range,timeout):
    
    for port in range(1,max_range): # For scanning ports max range is (2^16 - 1) = 65535 
        try: 
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.settimeout(timeout)
            s.connect((ip,port))
            service_name = socket.getservbyport(port,'tcp')
            print(str(port) + "\topen\t"+str(service_name))
            s.close()
        except socket.error:
            pass

if(os.name=='nt'):
    portScanWin(ip,max_range,timeout)
else:
    portScan(ip,max_range)

print("\n"+"-"*60)

end_time = datetime.datetime.now() - start_time
print("Scanning Finished in "+ str(end_time)+"\n"+"-"*60)

