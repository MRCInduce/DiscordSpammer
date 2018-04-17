import requests
i = int(input('Enter A Number:'))
webhook = "Your WebHook"
amount_of_messages = 0
message = " "
while amount_of_messages < i:
    amount_of_messages += 1
    message += "Your message" + "\n"
discordInter = {
    "username": "WhatEverName You want",
    "content": message
}

myHeaders = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"
}

Respone = requests.post(webhook, headers=myHeaders, json=discordInter)
