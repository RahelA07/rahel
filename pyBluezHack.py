

#this script that advertises a bluetooth low energy beacon for 15 seconds

#class library
import time #<--- 1st party class module

from bluetooth.ble import BeaconService #<--- 3rd party module 

#create an instanve of the object from the 3rf party class 

service = BeaconService()

#looking a connection 
service.start_advertising("11111111-2222-3333-4444-555555555555",1 , 1, 1, 200)

#take a break every 15 min
time . sleep(15)

service.stop_advertisizing ()

#print done
print("Done.")