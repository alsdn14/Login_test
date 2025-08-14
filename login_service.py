# 로그인 절차만 담당하는 모듈
# 주어진 아이디와 비밀번호를 입력하고, 로그인 성공 여부를 판별하며
# 각 단계별 실패 지점을 try-except로 구분하여 로깅

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from config import BASE_URL, XPATHS

def login(driver, wait, logger, user_id, user_pw):

    #1. 웹 페이지 열기
    try:
        driver.get(BASE_URL)
        logger.info("✅ 웹 페이지 접속 성공")
    except Exception as e:
        logger.error(f"❌ 페이지 접속 실패: {e}")
        return False

    #2. 마이페이지 버튼 클릭
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, XPATHS["mypage_btn"]))).click()
        logger.info("✅ 마이페이지 버튼 클릭 성공")
    except TimeoutException:
        logger.error("❌ 마이페이지 버튼 클릭 실패 - 요소를 찾지 못함")
        return False
    except Exception as e:
        logger.error(f"❌ 마이페이지 버튼 클릭 중 오류: {e}")
        return False

    #3. 아이디 입력
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, XPATHS["id_input"]))).send_keys(user_id)
        logger.info("✅ 아이디 입력")
    except TimeoutException:
        logger.error("❌ 아이디 입력창 로드 실패")
        return False
    except Exception as e:
        logger.error(f"❌ 아이디 입력 중 오류: {e}")
        return False

    #4. 비밀번호 입력
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, XPATHS["pw_input"]))).send_keys(user_pw)
        logger.info("✅ 비밀번호 입력")
    except TimeoutException:
        logger.error("❌ 비밀번호 입력창 로드 실패")
        return False
    except Exception as e:
        logger.error(f"❌ 비밀번호 입력 중 오류: {e}")
        return False

    #5. 로그인 버튼 클릭
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, XPATHS["login_btn"]))).click()
        logger.info("✅ 로그인 버튼 클릭")
    except TimeoutException:
        logger.error("❌ 로그인 버튼 클릭 실패 - 요소를 찾지 못함")
        return False
    except Exception as e:
        logger.error(f"❌ 로그인 버튼 클릭 중 오류: {e}")
        return False

    #6.  로그인 성공/실패 판별
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())  # 경고창 대기 (3초)
        alert = driver.switch_to.alert
        logger.warning(f"❌ 로그인 실패: {alert.text}")
        alert.accept()
        return False
    except TimeoutException:
        if "/personal/mypage" in driver.current_url:
            logger.info("✅ 로그인 성공 → 마이페이지 진입 완료")
            return True
        else:
            logger.error("❌ 로그인 후 마이페이지 이동 실패")
            return False
    except Exception as e:
        logger.error(f"❌ 로그인 판별 중 오류: {e}")
        return False
