from gpiozero import LED
from time import sleep
import requests
import json

userVerificationUrl = "http://ldap.makerspace.local:1880/cometcard?cometcard={user}"
someId = ""

def unlock():
    print("We unlocked")

def lock():
    print("We locked")

while True:
    cardId = input()
    requestUrl = userVerificationUrl.replace("{user}",cardId)
    response = requests.get(requests)

    responseJson = json.loads(response.content)

    if response == responseJson["success"] :
        unlock()
        sleep(2)
        lock()

