# 대학생 키우기(University Strudent Development Game)

> 파이게임(pygame)으로 만든 스토리 선택형 캠퍼스 라이프 게임입니다.
> 플레이어 이름을 입력하고, 선택지(1 or 2)를 골라 진행하며 그에 따른 엔딩까지 이어집니다.

## 🎮 조작 방법

- 시작 화면: space바로 게임 시작 -> 이름 입력 화면으로 이동
- 이름 입력 화면: 키보드로 입력
- 선택지 화면: 1 or 2 선택
- 스토리 진행 화면: space로 장면 넘기기
- 최종 점수: 결과 확인 -> 마우스 클릭

---

## 🕹️ 학습 목표 및 적용 개념 (CT 관점)

| 개념 | 프로젝트에서의 예시 |
|---|---|
| 변수 | 플레이어 이름(player_name), 체력(energy), 학점(final_score), 게임 상태(state) |
| 조건문 | if data.state == "ending": (상태별 화면 전환), 선택지 분기(choice_1 vs choice_2) |
| 반복문 | while running: (메인 게임 루프), for event in pygame.event.get(): (입력 감지) |
| 함수 | render() (화면 그리기), process_choice() (선택지 로직), resource_path() (경로 설정) |
| 자료 구조 | 딕셔너리를 활용한 엔딩 데이터 관리(ending_data), 리스트를 활용한 스토리 라인 관리 |
| 이벤트 처리 | pygame.KEYDOWN (키보드 입력), pygame.MOUSEBUTTONDOWN (버튼 클릭) |
| 모듈화 | 로직(game_logic.py)과 화면(game_view.py), 데이터(game_data.py)의 파일 분리 |

---

## 📂 프로젝트 구조 

<img width="639" height="483" alt="image" src="https://github.com/user-attachments/assets/27d58aad-07f5-48cf-9762-80dd3e553742" />
