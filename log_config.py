import logging

def get_logger(name=None):
    # 이미 설정된 로거가 있으면 그대로 반환
    if logging.getLogger().hasHandlers():
        return logging.getLogger(name)

    # 로깅 기본 설정
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("login_debug.log", encoding="utf-8"), # login_debug.log 라는 로그 남기기
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(name)
