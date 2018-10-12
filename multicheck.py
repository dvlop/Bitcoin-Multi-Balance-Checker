__author__ = 'xcbtrader'
# -*- coding: utf-8 -*-
# Changed To English 'BronxPhoneix'

import requests
import json
import time

def open_file():
	global addresses
	f = input('Enter Txt File Name:? ')
	try:
		fit = open(f, 'r')
		addresses = []
		a = fit.readline()
		while a != "":
			a = a[0 :-1]
			addresses.append(a)
			a = fit.readline()
		fit.close()
		print ('>> Total ' + str(len(addresses)) + ' Adress')
	except:
		print ('### Non-Existing File Error ###')

def b1(addr):
	try:
		request = 'https://blockchain.info/q/addressbalance/' + addr
		response = requests.get(request, timeout=10)
		content = int(response.json())
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1
			
def b2(addr):
	try:
		request = 'https://www.bitgo.com/api/v1/address/' + addr
		response = requests.get(request, timeout=10)
		content = response.json()
		content = int(content['confirmedBalance'])
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1
	
def b3(addr):
	try:
		request = 'https://api.blocktrail.com/v1/btc/address/' + addr + '?api_key=MY_APIKEY'
		response = requests.get(request, timeout=10)
		content = response.json()
		content = int(content['balance'])
		return content
	except KeyboardInterrupt:
		exit()
	except Exception:
		return -1
			
global addresses

n = 1
naddr = 0
pause = 0.2
nerror = 0
open_file()

while naddr<= len(addresses):
	if n == 1:
		balans = b1(addresses[naddr])
		if balans != -1:
			print (addresses[naddr] + ' = ' + str(balans/100000000))
			time.sleep(pause)
			n = 2
			naddr +=1
			nerror = 0
		else:
			n = 2
			nerror += 1
	elif n == 2:
		balans = b2(addresses[naddr])
		if balans != -1:
			print (addresses[naddr] + ' = ' + str(balans/100000000))
			time.sleep(pause)
			n = 3
			naddr +=1
			nerror = 0
		else:
			n = 3
			nerror += 1
	elif n == 3:
		balans = b3(addresses[naddr])
		if balans != -1:
			print (addresses[naddr] + ' = ' + str(balans/100000000))
			time.sleep(pause)
			n = 1
			naddr +=1
			nerror = 0
		else:
			n = 1
			nerror += 1
	if nerror > 3:
		exit()
