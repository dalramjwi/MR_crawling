import requests
url = "https://series.naver.com/novel/home.series"
response = requests.get(url)
html_content = response.text
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_content, 'html.parser')

# 제목 추출하기
title = soup.title.string
print("Page Title:", title)

# 첫 번째 <h1> 요소 추출하기
h1_text = soup.h1.string
print("H1 Text:", h1_text)

# 링크 추출하기
links = soup.find_all('a')
for link in links:
    print("Link Text:", link.text, "| URL:", link.get('href'))
    import csv

data = [
    {'title': title, 'h1_text': h1_text}
]

with open('data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'h1_text'])
    writer.writeheader()
    writer.writerows(data)