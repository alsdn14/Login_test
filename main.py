from login_executor import run_login

# 로그인자동화 메인 파일
# 사용자에게 아이디/비밀번호 입력 받아서 저장하기
user_id = input("아이디를 입력하세요: ").strip()
user_pw = input("비밀번호를 입력하세요: ").strip()
run_login(user_id, user_pw)
