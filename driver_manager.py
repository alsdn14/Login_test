from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

#드라이버 설정 (webdriver)
def get_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True) # 브라우저 종료 방지 ( 항상 켜 있음 )
    service = Service(ChromeDriverManager().install()) # 크롬 드라이버 자동 설치 및 실행 ( 따로 설치 필요 없음 )
    return webdriver.Chrome(service=service, options=options)
