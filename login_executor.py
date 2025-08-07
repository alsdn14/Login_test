from log_config import get_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import xpaths
from driver_manager import get_driver

logger = get_logger(__name__) # 분리된 설정에서 로거 받기

#유효성 검증
def run_login(user_id: str, user_pw: str):
    if not user_id or not user_pw:
        logger.warning("❗ 아이디 또는 비밀번호가 입력되지 않았습니다.")
        return

    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    
    try:
        # 1. 웹 페이지 열기
        driver.get("https://m.albamon.com/")
        logger.info("✅ 웹 페이지에 진입했습니다.")
    except Exception:
        logger.exception("❌ 웹 페이지 로딩 중 오류 발생")
        return
    
    try:
        # 2. 마이페이지 버튼이 보일 때까지 대기 후 클릭
        wait.until(EC.element_to_be_clickable((By.XPATH, xpaths.MYPAGE_BUTTON_XPATH))).click()
        logger.info("✅ 마이페이지 버튼 클릭")
    except Exception:
        logger.exception("❌ 마이페이지 버튼 클릭 실패") # 마이페이지 버튼 클릭 실패 시 로그
        return

    try:
        # 3. 아이디/비밀번호 입력창이 로드될 때까지 대기 후 입력
        wait.until(EC.presence_of_element_located((By.XPATH, xpaths.ID_INPUT_XPATH))).send_keys(user_id)
        logger.info("✅ 아이디 입력")
        wait.until(EC.presence_of_element_located((By.XPATH, xpaths.PW_INPUT_XPATH))).send_keys(user_pw)
        logger.info("✅ 비밀번호 입력")
    except Exception:
        logger.exception("❌ 아이디 또는 비밀번호 입력창이 노출되지 않음") # 아이디/비밀번호 입력창 노출되지 않을 때 로그
        return

    try:
        # 4. 로그인 버튼이 클릭 가능할 때까지 대기 후 클릭
        wait.until(EC.element_to_be_clickable((By.XPATH, xpaths.LOGIN_BUTTON_XPATH))).click()
        logger.info("✅ 로그인 버튼 클릭")
    except Exception:
        logger.exception("❌ 로그인 버튼 클릭 실패") # 로그인 버튼 클릭에 실패 시 로그
        return

    try:
        # 5. Alert 여부 확인 및 로그인 결과 처리, Alert 가 뜰 때까지 최대 3초 대기
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        # Alert 감지 후 처리
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        logger.error(f"❌ 로그인 실패: {alert_text}")
        return
    except TimeoutException:
        # Alert이 없으면 → 로그인 성공 or 마이페이지 이동 실패 
        current_url = driver.current_url
        if "/personal/mypage" in current_url:
            logger.info("✅ 로그인 성공! 마이페이지 진입")
        else:
            logger.error(f"❌ 로그인은 되었지만 마이페이지 이동 실패: {current_url}") # 로그인은 성공되었으나 마이페이지 이동이 안될 때
        return
    except Exception as e:
        logger.exception(f"❗ Alert 처리 중 예외 발생: {e}")
        return
