# 로그인 자동화에 필요한 설정값들을 모아두는 파일
# 사이트 URL, 버튼/입력창 위치(XPath), 대기 시간, 로그 저장 경로 등을 정의

BASE_URL = "https://m.albamon.com/" # 로그인할 웹사이트 주소

# 사이트 내 요소들의 XPath를 딕셔너리 형태로 저장
XPATHS = {
    "mypage_btn": '//*[@id="__next"]/main/div[1]/div[3]/div[4]/a[4]/span', # 마이페이지 버튼 위치
    "id_input": '//*[@id="memberId"]', # 아이디 입력창 위치
    "pw_input": '//*[@id="memberPassword"]', # 비밀번호 입력창 위치
    "login_btn": '//*[@id="__next"]/main/div[2]/div/form/div[4]/button' # 로그인 버튼 위치
}

LOG_DIR = "logs/" # 로그 파일 저장 폴더 경로
WAIT_TIMEOUT = 10 # 기본 대기 시간(초)
