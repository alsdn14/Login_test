# 콘솔과 파일에 동시에 로그를 남기는 로거(Logger) 생성
# 로그에는 시간, 로그 등급(INFO, ERROR 등), 메시지가 포함됨

import logging
from datetime import datetime
import os
from config import LOG_DIR

def setup_logger(name: str):
    os.makedirs(LOG_DIR, exist_ok=True)
    log_filename = os.path.join(LOG_DIR, f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_filename, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(name)
