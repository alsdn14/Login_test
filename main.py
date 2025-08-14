# 로그인 자동화 메인 파일 ( 여기서 실행 )
# 사용자 입력을 받고, 드라이버와 로그인 모듈을 실행
import re
from driver_manager import get_driver
from login_service import login
from logger import setup_logger

def is_valid_user_id(user_id):
    # 영어 소문자, 숫자만 허용, 6~16자
    return bool(re.fullmatch(r'[a-z0-9]{6,16}', user_id))

def is_valid_password(user_pw):
    # 영어 대소문자, 숫자, 특수문자만 허용, 8~16자
    return bool(re.fullmatch(r'[A-Za-z0-9!@#$%^&*(),.?\":{}|<>]{8,16}', user_pw))

def main():
    logger = setup_logger("login_test") # 로그 생성기 초기화

    # 사용자로부터 로그인 정보 입력받기
    user_id = input("아이디: ").strip()
    user_pw = input("비밀번호: ").strip()

    # 아이디 유효성 검사
    if not user_id:
        logger.error("❌ 아이디 미입력")
        return
    elif not is_valid_user_id(user_id):
        logger.error("❌ 아이디 형식 오류 (영어 소문자, 숫자만 허용, 6~16자만 허용)")
        return

    # 비밀번호 유효성 검사
    if not user_pw:
        logger.error("❌ 비밀번호 미입력")
        return
    elif not is_valid_password(user_pw):
        logger.error("❌ 비밀번호 형식 오류 (영어 대소문자, 숫자, 특수문자만 허용, 8~16자만 허용)")
        return

    driver, wait = get_driver() # 크롬 드라이버와 대기 객체 생성
    success = login(driver, wait, logger, user_id, user_pw) # 로그인 실행

    if success:
        logger.info("테스트 시나리오: 로그인 성공")
    else:
        logger.info("테스트 시나리오: 로그인 실패")

if __name__ == "__main__":
    main()
