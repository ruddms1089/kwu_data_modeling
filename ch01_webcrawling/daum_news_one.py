# 1. 데이터 수집
#   - 웹 크롤링(Wed Crawling)
#   - OpenAPI (기관에서 제공)
#   - Database & Server
#   - Excel

# 웹 크롤링 : 웹 사이트에 존재하는 데이터를 수집하는 방법
#   - 라이브러리 : BeautifulSoup4, Requests, Selenium

# 웹사이트 : HTMP 언어
# 개발자(HTMP Code) -> 웹 브라우저(Chrome) -> 랜더링 -> 예쁜 웹 사이트 짜잔!

import requests
from bs4 import BeautifulSoup

# requests : 웹 사이트(url) 전체 코드 복사 Get
# BeautifulSoup : 전체 코드에서 수집하고 싶은 정보만 Get

url = "https://v.daum.net/v/20231004104848652" # 데이터를 수집하고 싶은 주소
result = requests.get(url) # requests는 해당 URL의 모든 소스코드를 가져옴
# print(result.text)

# result.taxt(전체코드) => BeautifulSoup 읽고 해석 => doc(전체코드)
doc = BeautifulSoup(result.text, "html.parser")

# 전체코드 중 수집하고 싶은 부분만 select
# HTML
# 1. Tag로 구현함 ex) <html></html>, <div></div>, <p>값</p>
# 2. 선택자
#   - ID 선택자 : 유니크, 1개만 존재
#   - Class 선택자(.) : 복수개 선택

# select() => list type[]
# get_text() => Tag정보 제거, 순수 Text만 추출
title = doc.select("h3.tit_view")[0].get_text()
print(f"제목 : {title}") # f : f sting 표기법
print("제목 : {}".format(title)) # format() 표기법
