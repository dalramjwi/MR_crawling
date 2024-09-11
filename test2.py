from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# 브라우저 드라이버 경로 설정
chrome_options = Options()
chrome_options.add_argument("--headless")  # 브라우저 UI를 숨깁니다
service = Service(r'C:\Users\Administrator\Downloads\asasdasdasd\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹 페이지 열기
url = 'https://novel.naver.com/webnovel/weekday'
driver.get(url)

# 자바스크립트 실행 대기 (필요 시)
time.sleep(5)  # 5초 대기

# 페이지 소스 가져오기
html_content = driver.page_source

# BeautifulSoup으로 HTML 파싱
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# 데이터 추출
page_source = driver.page_source
print("Page Title:", page_source)

# 브라우저 닫기
driver.quit()