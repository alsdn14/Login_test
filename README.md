## 1. AI 도구 활용 과정
* **사용 도구** : Chat GPT-4o  
* **프롬프트 및 AI 응답 원본 전체** : https://chatgpt.com/share/68945fb4-2328-8000-8c2d-3b5f367a4205  
## 2. 자동화 스크립트 작성

* **선택 브라우저**: Chrome (WebDriver 기반)
* **사용 도구 및 언어** ( Python + Selenium )
* **모듈 구조**

Login_test  
├── driver_manager.py  
├── log_config.py  
├── login_executor.py  
├── main.py  
└── xpaths.py

| 파일명 | 역할 및 내용 |
| ------ | ------ |
|main.py|실제 실행되는 파일입니다. 사용자로부터 아이디/비밀번호를 입력받고 login_executor.run_login() 함수를 호출하여 자동화 테스트를 시작합니다.|
|login_executor.py|로그인 자동화의 핵심 로직이 들어있는 모듈입니다. Selenium을 사용해 웹 페이지 접근, 로그인 시도, 성공/실패 상태를 단계별로 처리합니다.|
|xpaths.py|로그인 자동화 과정에서 사용하는 XPath 들을 변수로 모아둔 모듈입니다.|
|driver_manager.py|크롬 드라이버의 초기 설정을 담당하는 모듈입니다. 이곳에서 브라우저 옵션을 조정할 수 있습니다.|
|log_config.py|로깅 설정을 모듈화한 파일입니다. 함수로 로거 객체를 초기화하고, 핸들러(콘솔 및 파일), 로그 포맷 등을 설정합니다.|



## 3. 자동화 실행 결과

* **실행 결과 콘솔 캡쳐**

|유효성 검증|로그인 성공|로그인 실패|
| ------ | ------ |------ |
|<img width="573" height="57" alt="image" src="https://github.com/user-attachments/assets/9cd19cd3-cf67-4b58-b233-84b9fe830745" />||<img width="1104" height="244" alt="image" src="https://github.com/user-attachments/assets/5faa2a9b-97c1-4d03-854b-3fb26a39611c" />|

|유효성 검증|로그인 성공|
| ------ | ------ |
|유효성 검증|<img width="573" height="57" alt="image" src="https://github.com/user-attachments/assets/9cd19cd3-cf67-4b58-b233-84b9fe830745" />|
|로그인 성공||
|로그인 실패|<img width="1104" height="244" alt="image" src="https://github.com/user-attachments/assets/5faa2a9b-97c1-4d03-854b-3fb26a39611c" />|



* **실행 흐름 요약**

1. 로그 실행 시작: main.py에서 사용자 입력을 받고 run_login(...) 호출  
2. 로그 설정 적용: log_config.py를 통해 로거가 초기화되어 각 단계 메시지가 로깅됨  
3. 드라이버 준비: driver_manager.py 로 크롬 브라우저 생성  
4. 자동화 흐름 진행: login_executor.py가 페이지 접속 → 입력 → 로그인 → 결과 확인까지 단계별 실행  
5. XPath 관리: xpaths.py를 통해 코드에 하드코딩 대신 중앙 집중식 XPath 관리  


## 4. 테스트 케이스 도출

<details><summary>테스트케이스 펼쳐 보기</summary>
ㅇㅇ
</details>

## 5. 결과물 검토 및 보완 설명

* AI 출력의 한계 또는 오류    
* 수정/보완한 내용 및 이유   
* 실무 관점에서 필요한 추가 예외 케이스    
