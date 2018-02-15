
import urllib2
import json
import os.path
import datetime

 
balResponse = urllib2.urlopen("https://prohashing.com/explorerJson/getAddress?address=DLMHGfLPdpaJarFBiynqnmwRRAcooG1AmH&coin_id=146")
balData = json.load(balResponse)

newBalance = balData['balance']

	
bal = open("yourPath/blah/existingBalance.txt","r") 
balance = float(bal.readline())
bal.close()

if newBalance != balance:
    #replace old balance with new balance
    bal=open("yourPath/blah/existingBalance.txt", "w")
    bal.write(str(newBalance))
    bal.close()

    #Get coinmarketcap api data for verge
    cmcResponse = urllib2.urlopen("https://api.coinmarketcap.com/v1/ticker/verge/")
    cmcData = json.load(cmcResponse)
    priceUSD = float(cmcData[0]['price_usd'])

    tempPayout = float(newBalance-balance)
    totalUSDPayout = float(tempPayout*priceUSD)

    pool = open("yourPath/blah/poolPayouts.txt", "a")
    pool.write(datetime.datetime.now().strftime("%m/%d/%y, %H:%M") + "\t\t" +str(newBalance-balance)+", \t"+ str(priceUSD) + ",\t"+ str(totalUSDPayout) + "\n")
    pool.close()

