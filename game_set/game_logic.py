import pygame
from setting import assets
from setting.settings import *


def process_click(pos, data):
    """마우스 클릭 좌표(pos)를 받아 게임 상태(data.state)에 따라 로직을 수행합니다."""

    # 1. 시작 화면
    if data.state == "start":
        if assets.start_btn.collidepoint(pos):
            data.state = "input_name"

    # 3. 게임 방법 설명
    elif data.state == "how_to_play":
        data.state = "game_start_scene"

    # 4. 게임 시작 컷신
    elif data.state == "game_start_scene":
        data.state = "opening"

    # 5. 오프닝 (신발 고르기 전)
    elif data.state == "opening":
        pass

        # 6. 오프닝 결과 확인
    elif data.state == "opening_result":
        pass

    # 7. 스토리 진행 (선택지 고르기)
    elif data.state == "story":
        if pygame.Rect(STORY_V_CHOICE_1_RECT).collidepoint(pos):
            process_choice(1, data)
        elif pygame.Rect(STORY_V_CHOICE_2_RECT).collidepoint(pos):
            process_choice(2, data)

    # 8. 결과 화면
    elif data.state == "result":
        go_next_step(data)

    # 9. 최종 점수 화면
    elif data.state == "score_screen":
        data.state = "ending"
        if hasattr(data, "ending_key_cache"): del data.ending_key_cache

        # 10. 엔딩 화면
    elif data.state == "ending":
        pass

        # 11. 게임 오버
    elif data.state == "game_over":
        if assets.restart_btn.collidepoint(pos):
            data.reset_data()

def process_opening_choice(choice_idx, data):
    """오프닝에서 1번(착용) 또는 2번(미착용) 선택 시 결과 적용"""

    # 페이지 인덱스 초기화
    data.opening_index = 0

    if choice_idx == 1:
        # 1번: 신발 착용 (텍스트 나누기)
        data.opening_lines = [
            "즐거운 학교생활에 대한 힘든 마음으로 강의동을 향해 걸음을 옮겼다.\n바람이 제법 차가웠지만, 신발 덕분에 발은 포근했다.",
            "대학교회를 지나며 공기의 차가움을 느끼자,\n‘역시 신발은 신고 오는 게 정답이지’라는\n아주 당연한 결론이 머릿속에 스쳤다.",
            "‘발도 안 시렵고, 딱히 특별한 일도 없고… 좋네?’\n강의실에 도착해 노트북을 켜고 책을 꺼내면서\n나는 이 아침이 이상할 정도로 무난하다는 걸 새삼 느꼈다.",
            "큰 행운도 없고, 재앙도 없고, 사건도 없이\n그저 평범한 하루의 시작.\n‘음… 따뜻하네. 좋다…’",
            "하지만 그뿐이었다. 정말로.\n신발을 신고 온 덕분에 발이 시렵지 않았다.\n그 외엔 아무 일도 일어나지 않았다."
        ]
        data.energy += 10

    else:
        # 2번: 신발 미착용 (텍스트 나누기)
        data.opening_lines = [
            "맨발로 바닥을 밟는 순간, 차가운 기운이 발바닥에 닿았다.\n그러나 어느순간부터 따스함이\n발끝에서부터 퍼져 오르기 시작했다.",
            "“뭐지… 이거?”\n강의실 문을 열자, 친구들이 놀란 표정으로 나를 바라보았다.\n“어? 너 왜 맨발이야?”",
            "갑자기 어딘가에서 은은한 빛이 내 주변으로 스며들었다.\n바람이 한 번 흔들리더니,\n공기가 잔잔하게 웅울거리며 나를 감쌌다.",
            "발바닥에서 시작된 따뜻한 기운이\n다리, 허리, 어깨까지 올라오더니\n머리 꼭대기에서 작게 퍼졌다.",
            "그리고 나는 생각했다.\n‘아… 이게 바로 원주의 자연이구나.’",
            "머릿속에 어떤 목소리가 선명하게 울렸다.\n“당신은 원주 자연의 가호를 받았습니다.\n이번 학기, 모든 일이 순탄하게 흘러갈 것입니다.”",
            "그렇게 나는 오늘 아침\n원주 자연 버프와 함께\n완벽한 하루를 시작하게 되었다."
        ]
        data.energy += 20
        data.gpa += 0.5

    # 스탯 범위 제한
    if data.energy > 100: data.energy = 100
    if data.gpa < 0: data.gpa = 0.0
    if data.gpa > 4.5: data.gpa = 4.5


def process_choice(choice_idx, data):
    """선택지 선택 시 결과 계산"""
    data.last_choice = choice_idx
    story = data.full_story[data.current_step]

    if choice_idx == 1:
        res = story["result_1"]
    else:
        res = story["result_2"]

    data.gpa += res[0]
    data.energy += res[1]
    data.result_lines = res[2]
    data.result_index = 0

    # 범위 제한
    if data.gpa > 4.5: data.gpa = 4.5
    if data.gpa < 0: data.gpa = 0.0
    if data.energy > 100: data.energy = 100

    data.state = "result"


def go_next_step(data):
    """다음 단계로 이동"""
    if data.energy <= 0:
        data.state = "game_over"
        return

    data.current_step += 1

    if data.current_step > data.max_step:
        data.state = "score_screen"
        data.final_score = int(data.gpa * 20 + data.energy * 0.1)
        if data.final_score > 100: data.final_score = 100
    else:
        data.state = "story"