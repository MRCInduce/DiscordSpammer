import requests


def Spam():
    i = int(input('Enter A Number:'))
    webhook = "YOUR WEBHOOK HERE"
    amount_of_messages = 0
    message = " "
    while amount_of_messages < i:
        amount_of_messages += 1
        message += "PLEASE INPUT UR MESSAGE HERE" + "\n"
    discordData = {
        "username": "",
        "content": message
    }

    myHeaders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"
    }

    discordResponse = requests.post(webhook, headers=myHeaders, json=discordData)


print("Input How Many Times You Wanna Loop")
loop = int(input('Enter A Number Smaller Then 5'))
destroy = 0
while destroy < loop:
    Spam()
