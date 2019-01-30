import requests
import csv
import re
from bs4 import BeautifulSoup

url = 'http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf'

headers = {'User-Agent': 'Mozilla/5.0'}
 
req = requests.get(url, headers=headers) # connection
html = req.text # 소스 가져오기
soup = BeautifulSoup(html,'html.parser')

# csvFile = open("book.csv", "w")
# writer = csv.writer(csvFile)
# # 첫 줄에 헤더 작성
# writer.writerow(["BookName", "URL"])

book_list = soup.select('#main_contents > ul > li')
book_link = [x.select_one('div.detail > div.title > a').text for x in book_list]
book_title = [x.select_one('div.detail > div.title > a > strong').text for x in book_list]
book_price = [x.select_one('div.detail > div.price > strong').text for x in book_list]
book_eprice = [x.select_one('div.detail > div.price > a ').text for x in book_list]
print("☆ ☆ ☆ ☆ ☆ 이번주 베스트셀러 순위 ☆ ☆ ☆ ☆ ☆")

data = {}

for i in range (0,20):
    a = print(i+1,"위",book_title[i] , " => 도서 : ['" ,book_price[i], "'] ebook : ", book_eprice[i].split())
# try:
#     for book in range(0,20):
#         link = 'http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf'
#         title = book_title[book]
#         writer.writerow([title,link])
# finally:
#     csvFile.close()

# Api 및 Token 정보
API_HOST = 'https://notify-api.line.me'

url = 'https://notify-api.line.me/api/notify'

token = {'Authorization': 'Bearer wpRFnajjEO4opdWimvXXuxLoKjY7kKhRJFifjgUgjHN'}

message = []
parameter = {"message": message}
# parameter = {"message": message, "stickerId":2, "stickerPackageId":100}


# Response
response = requests.post(
    url, headers =token, data = parameter)

# print(response.text)