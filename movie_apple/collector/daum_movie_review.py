# Web Crawler
#  1.기본(requests:정적 페이지 + bs4)
#  2.심화(selenium:정적, 동적 페이지 + bs4)

# requests는 현재 URL의 정적인 페이지 소스코드만 수집 가능
#  → 더보기 등 버튼을 눌러야 나오는 동적인 정보는 수집 불가

# selenium은 URL의 정적, 동적 소스코드 모두 수집 가능
#  → 자기자신만의 브라우저를 사용해서 동작하기 때문에 모두 수집 가능
#  → 따라서, chromedriver와 같은 브라우저 설정 반드시 필요!

# pip install beautifulsoup4
# pip install selenium
# pip install webdriver_manager

# TO DO: 다음 영화 리뷰 수집
#          제목, 리뷰, 작성자, 평점, 작성일자
# 데이터베이스(MySQL) → 저장
# 데이터베이스 → 로드 → 분석 → 인공지능(감성분석: 긍정, 부정 분류기) → 그래프
import time
import re
import math

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

# 1.Selenium을 위한 ChromDriver 설치
#   1-1.직접 다운로드
#     - https://sites.google.com/chromium.org/driver/
#   1-2.실시간 다운로드 후 사용
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

# 2.URL 접속
url = "https://movie.daum.net/moviedb/grade?movieId=165591"
driver.get(url)
time.sleep(1)

# 3.페이지 전체 소스 가져오기(리뷰: 최초 10개)
doc_html = driver.page_source

# 4.Selenium(전체 코드) → Beautifulsoup4 전달
doc = BeautifulSoup(doc_html, "html.parser")

# 5.원하는 데이터 수집(Select)
#  5-1.영화 제목
title = doc.select("span.txt_tit")[0].get_text()

#  5-2. "평점 더보기" Click → 전체 영화 리뷰(동적)
# 정답: 5번
# 계산식 = "평접 더보기" 몇 번 Click??
# 전체리뷰: 140개, 최초: 10개, Click 1번 30개

total_review_cnt = doc.select("span.txt_netizen")[0].get_text()  # 해당 영화 전체 리뷰 수
# 1.문자열 슬라이싱
# print(total_review_cnt[1:-2])  # 140개 정답
# 2.정규식(010-1234-1245)
num_review = int(re.sub(r"[^~0-9]", "", total_review_cnt))

# math.ceil() 올림:  4.33333 → 5.0
click_cnt = math.ceil((num_review - 10) / 30)  # 올림

# 반복문
#  1.for(반복횟수 아는 경우)
#  2.while(반복횟수 모르는 경우)
for i in range(click_cnt):
    # "평점 더보기" Click
    driver.find_element(By.CLASS_NAME, "link_fold").click()
    time.sleep(1)
time.sleep(5)

#  5-3.전체 소스코드 가져오기(리뷰: 모드 Open)
doc_html = driver.page_source
doc = BeautifulSoup(doc_html, "html.parser")
review_list = doc.select("ul.list_comment > li")

for tag in review_list:
    # 5-4. 리뷰(댓글, 작성자, 평점, 날짜) 수집
    print("="*100)
    review_score = tag.select("div.ratings")[0].get_text() # 평점
    print(f" - 평점: {review_score}")

    review_writer = tag.select("a.link_nick > span")[1].get_text().strip() # 작성자
    print(f" - 작성자: {review_writer}")

    review_reply = tag.select("p.desc_txt")[0].get_text().strip()  # 리뷰
    print(f" - 리뷰: {review_reply}")

    original_date = tag.select("span.txt_date")[0].get_text()  #날짜
    idx = original_date.rfind(".") # rfind : 뒤에서부터 찾아라~
    review_date = original_date[:idx]
    review_date = re.sub(r"[^~0-9]", "", review_date)
    if len(review_date) <= 2: #3시간 전, 23시간 전
        today = datetime.today() # 현재 날짜시간
        review_date = str(today.year) + str(today.month) + str(today.day)

    print(f" - 날짜: {review_date}")

    # print(len(review_list)) : 전체 갯수 확인