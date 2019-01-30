# -*- coding: utf-8 -*-
import requests

# Api 및 Token 정보
API_HOST = 'https://notify-api.line.me'

url = 'https://notify-api.line.me/api/notify'

token = {'Authorization': 'Bearer cNw9NGs8CKfP0uruW4AB6WTMe6l5oDkTpMR'}
data = {}

message = "API Test"
parameter = {"message": message}
# parameter = {"message": message, "stickerId":2, "stickerPackageId":100}


# Response
response = requests.post(
    url, headers =token, data = parameter)

print(response.text)