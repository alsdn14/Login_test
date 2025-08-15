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

### AI 출력의 한계 또는 오류  
**1. 설계 부재, 유지보수 난이도 상승**  
- 기능 확장 시 코드가 얽혀 있어 코드가 엉킬 수 있음  
- 재사용성, 확장성, 모듈화가 고려되지 않아 변경 시 전체를 수정해야 하는 경우 발생
- 프롬프트 엔지니어링에 신경을 쓰고 최초 설계 시 이부분을 고려 해야 함  

**2. 환경 호환성 문제**
- AI는 로컬 환경 (운영체제, 라이브러리·드라이버 버전)을 알 수 없으므로 호환성 오류 발생 가능성 있음  
- 잘못된 API 호출, deprecated 메서드 사용, 보안 취약 코드 포함 가능성    
  예) 이번 코드 작성 중 `WebDriverWait.until()`에 존재하지 않는 인자를 사용하여 실행 오류 발생

**3. 예외 처리 부족**
- AI가 생성한 코드는 정상 시나리오 위주로 작성되는 경우가 많아, 네트워크 지연, 팝업/배너 노출, 화면 로딩 실패 등 비정상 상황에 대한 처리 로직이 부족할 수 있음
- 실무 환경에서는 이러한 예외 케이스가 빈번하게 발생하므로, 추가적인 보완 작업이 필요

**4. 서비스 변경 대응의 어려움**
- 웹사이트 구조나 정책이 변경되면 코드 수정이 필요
- AI가 생성한 초기 코드는 이러한 변경에 자동 대응하지 못하며, 이를 반영하려면 최소한의 코드 구조 이해와 도메인 지식이 필수입니다.  
- 즉, 유지보수 지식이 부족하면 서비스 변경 시 대응이 어려울 수 있습니다.  

* 수정/보완한 내용 및 이유   
* 실무 관점에서 필요한 추가 예외 케이스    
