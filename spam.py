import requests
from time import sleep


def Spam():
    webhook = "YoUR WEBHOOK GOES HERE"

    message = " "
    message += "TYPE MESSSAGE HERE" + "\n"
    discordData = {
        "username": "NAME",
        "content": message
    }

    myHeaders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"
    }

    discordResponse = requests.post(webhook, headers=myHeaders, json=discordData)


def loopSpam():
    destroy = 0
    loop = 1
    while destroy < loop:
        destroy = 0
        sleep(1.0)
        Spam()


def limitSpam():
    amount = int(input("Number:"))
    limiter = 0
    while limiter < amount:
        Spam()
        limiter += 1


print("Do You Want To Have A Infinite Spam Or A Certain Amount")
print("Type Spam or Limit(with caps!)")
choice = str(input())
if choice == "Spam":
    loopSpam()
if choice == 'Limit':
    limitSpam()
