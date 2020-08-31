import os
import sys
#show saved network
saved_profile=os.popen('netsh wlan show profiles').read()
print(saved_profile)

#show available networks now at present out of all the saved network
avail_profiles=os.popen('netsh wlan show networks').read()
print(avail_profiles)

#enter the netwrk u want to connect now
preffered_ssid=input("enter preffered network: ")

#disconnect the network
response=os.popen("netsh wlan disconnect").read()
print(response)

#check if preffered netwrk is saved or not
if preffered_ssid not in saved_profile:
	print("Profile for" +preffered_ssid+ "is not available")
	print("Sorry cant establish connection")
	#code execution will stop
	sys.exit()


else:
	print("Profile for" +preffered_ssid+ "is available")

#check if saved netwrk is available or not....like is hotspot is switched on or not
while True:
	avail=os.popen('netsh wlan show networks').read()
	if preffered_ssid in avail:
		print("found")
#loop is infinite(user may swich on wifi later )
# so break is useds

		break
#for connecting to wifi/build connection
print("------Connecting--------")
resp=os.popen('netsh wlan connect name='+'"'+preffered_ssid+'"').read()
print(resp)