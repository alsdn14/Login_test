# 크롬 브라우저 드라이버를 자동 설치 및 실행하는 모듈
# Selenium WebDriverWait 객체도 함께 반환하여, 요소가 나타날 때까지 대기 가능하게 함

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config import WAIT_TIMEOUT
from selenium.webdriver.support.ui import WebDriverWait

def get_driver():
    options = Options()
    options.add_argument("--start-maximized") # 브라우저 최대화 실행
    options.add_experimental_option("detach", True)  # 실행 후 브라우저 자동 종료 방지

    service = Service(ChromeDriverManager().install()) # 크롬 드라이버 자동 설치
    driver = webdriver.Chrome(service=service, options=options) 
    wait = WebDriverWait(driver, WAIT_TIMEOUT) # 기본 대기 객체 생성
    return driver, wait
