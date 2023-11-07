# 1.데이터 수집
#  - 웹 크롤링(Web Crawling)
#  - OpenAPI(기관에서 제공)
#  - Database & Server
#  - Excel

#  웹 크롤링: 웹 사이트에 존재하는 데이터를 수집하는 방법
#    - 라이브러리: BeautifulSoup4, Requests, Selenium

# 웹사이트: HTML 언어
# 개발자(HTML Code) -> 웹 브라우저(Chrome) -> 랜더링 -> 예쁜 웹 사이트 짜짠!

import requests
from bs4 import BeautifulSoup


# 기능(함수) 1. daum news에서 기사(제목+본문) 수집기
#   - 입력(parameter): url
#   - 출력: 기사(제목+본문)
def collect_news(url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    title = doc.select("h3.tit_view")[0].get_text()
    print(f"제목: {title}")
    contents = doc.select("section > p")
    content = ""
    for i, p in enumerate(contents):
        content = content + p.get_text()
    print(f"본문: {content}")