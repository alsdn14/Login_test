## 웹 로그인 자동화

## 1. AI 도구 활용 과정
* **사용 도구** : Chat GPT5 + Cursor
* **프롬프트 및 AI 응답 원본 전체** : [Chat GPT 응답 원본 전체 링크](https://chatgpt.com/share/689df4fc-1438-8000-be2b-627eb8dc7fd0)  
* **선택 브라우저**: Chrome (WebDriver 기반)
* **사용 도구 및 언어** ( Python + Selenium )

## 2. 자동화 스크립트 작성
* **모듈 구조**

Login_test  
├── driver_manager.py  
├── logger.py  
├── login_service.py  
├── main.py 
├── config.py
└── logs

| 파일명 | 역할 및 내용 |
| ------ | ------ |
|main.py|메인 실행 파일 (유효성 검사 + 로그인 실행)|
|config.py |사이트 URL, XPath, 대기 시간, 로그 경로 설정|
|driver_manager.py|크롬 드라이버 및 WebDriverWait 생성|
|login_service.py|콘솔+파일 로그 기록 설정|
|logger.py|로깅 설정을 모듈화한 파일입니다.   함수로 로거 객체를 초기화하고, 핸들러(콘솔 및 파일), 로그 포맷 등을 설정합니다.|
|logs|실행 시 생성되는 로그 파일 저장 폴더|


## 3. 자동화 실행 결과

* **실행 흐름 요약**
```
[사용자 입력]
    ↓
[main.py]
  1. 로거(Logger) 생성 → logs 폴더에 파일 저장 준비
  2. 아이디/비밀번호 입력 받음
  3. 유효성 검증 수행
     ├─ 아이디: 영어 소문자 + 숫자, 6~16자
     ├─ 비밀번호: 영어 대소문자 + 숫자 + 특수문자, 8~16자
     └─ 미입력/형식 오류 시 프로그램 종료
    ↓
[driver_manager.py]
  4. ChromeDriver 자동 설치 및 실행
  5. WebDriverWait 객체 생성
    ↓
[login_service.py]
  6. BASE_URL 접속
  7. 마이페이지 버튼 클릭
  8. 아이디/비밀번호 입력
  9. 로그인 버튼 클릭
 10. 로그인 성공/실패 판별
     ├─ 경고 창 발생 → 실패 처리
     ├─ URL에 "/personal/mypage" 포함 → 성공 처리
     └─ 기타 → 실패 처리
    ↓
[logger.py]
 11. 각 단계별 결과를 콘솔 + 로그 파일에 기록
    ↓
[종료]
```


* **실행 결과 콘솔 캡쳐**

|동작|캡쳐 스크린샷|
| ------ | ------ |
|유효성 검증|<img width="765" height="243" alt="image" src="https://github.com/user-attachments/assets/bd4e5091-3f6f-4a05-864f-45df67926985" />|
|로그인 성공|<img width="511" height="120" alt="image" src="https://github.com/user-attachments/assets/a421ac0f-8012-432b-8966-dce5cd8dd2bb" />|
|로그인 실패|<img width="897" height="119" alt="image" src="https://github.com/user-attachments/assets/246e8904-dcc4-446d-8d58-07ea028db5ff" />|



</details>


## 4. 테스트 케이스 도출

* [테스트 케이스 Google Sheets 링크](https://docs.google.com/spreadsheets/d/1gex_49dmtCSYjZ25_9sFOxttJ206sqEgJQkgpPU2cKg/edit?gid=1803579238#gid=1803579238)  
  
<details><summary>테스트케이스 사진 펼쳐 보기</summary>
<img width="2161" height="621" alt="image" src="https://github.com/user-attachments/assets/a64f8efc-6311-4534-b418-79ea71362c35" />
</details>

## 5. 결과물 검토 및 보완 설명

* AI 출력의 한계 또는 오류    
* 수정/보완한 내용 및 이유   
* 실무 관점에서 필요한 추가 예외 케이스    
