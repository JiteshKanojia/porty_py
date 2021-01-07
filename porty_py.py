import socket
import subprocess
import datetime 

subprocess.call("clear",shell=True)

print("-"*60)
#take Input ip address from the user 
#global ip
ip = input("Enter an IP-v4 address:  ")
start_time = datetime.datetime.now()
#global s
#s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("scanning for IP: "+str(ip)+"\n"+"-"*60 + "\n")
print("port\tstatus\tservice" +"\n----\t------\t-------")

max_range = 65535

#known_Ports=[7,19,20,21,22]

def portScan(ip):
    
    for port in range(1,max_range): # For scanning ports max range is (2^16 - 1) = 65535 
        try: 
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((ip,port))
            service_name = socket.getservbyport(port,)
            print(str(port) + "\topen\t"+str(service_name))
            s.close()
        except socket.error:pass
            #s.close()
            #print("excepted")
#print("-"*60)
portScan(ip)
print("\n"+"-"*60)

end_time = datetime.datetime.now() - start_time
print("Scanning Finished in "+ str(end_time)+"\n"+"-"*60)

