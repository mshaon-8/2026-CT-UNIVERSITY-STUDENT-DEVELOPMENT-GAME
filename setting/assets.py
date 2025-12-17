import pygame
import os
import sys
from setting.settings import *

pygame.init()

def resource_path(relative_path):
    try:
        # PyInstaller로 만들어진 exe는 sys._MEIPASS에 압축 해제 경로가 저장됨
        base_path = sys._MEIPASS
    except Exception:
        # 일반 파이썬 실행 시 현재 경로 사용
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def load_image(filename, width=SCREEN_WIDTH, height=SCREEN_HEIGHT):
    path = resource_path(os.path.join("images", filename))

    # 파일 확장자 자동 확인 (.png <-> .jpg)
    if not os.path.exists(path):
        if filename.endswith(".png"):
            alt = filename.replace(".png", ".jpg")
            if os.path.exists(os.path.join("images", alt)): path = os.path.join("images", alt)
        elif filename.endswith(".jpg"):
            alt = filename.replace(".jpg", ".png")
            if os.path.exists(os.path.join("images", alt)): path = os.path.join("images", alt)

    try:
        img = pygame.image.load(path)
        return pygame.transform.scale(img, (width, height))
    except:
        print(f"[오류] 이미지 로드 실패: {path}")
        return None


# --- 이미지 자원 ---
start_bg_img = load_image("title_bg.png")
how_to_play_img = load_image("how_to_play.png")
game_start_scene_img = load_image("start.png")
opening_img = load_image("shoes.png")
final_score_bg_img = load_image("final_score.png")

# 이름 입력창 배경
input_name_bg_img = load_image("input_name_bg.png")

# [월요일]
monday_1_img = load_image("monday_1.png")
monday_1_1_img = load_image("monday_1_1.png")
monday_1_2_img = load_image("monday_1_2.png")
monday_2_img = load_image("monday_2.png")
monday_2_1_img = load_image("monday_2_1.png")
monday_2_2_img = load_image("monday_2_2.png")
monday_3_img = load_image("monday_3.png")
monday_3_1_img = load_image("monday_3_1.png")
monday_3_2_img = load_image("monday_3_2.png")
monday_4_img = load_image("monday_4.png")
monday_4_1_img = load_image("monday_4_1.png")
monday_4_2_img = load_image("monday_4_2.png")

# [화요일]
tuesday_1_img = load_image("tuesday_1.png")
tuesday_1_1_img = load_image("tuesday_1_1.png")
tuesday_1_2_img = load_image("tuesday_1_2.png")
tuesday_2_img = load_image("tuesday_2.png")
tuesday_2_1_img = load_image("tuesday_2_1.png")
tuesday_2_2_img = load_image("tuesday_2_2.png")
tuesday_3_img = load_image("tuesday_3.png")
tuesday_3_1_img = load_image("tuesday_3_1.png")
tuesday_3_2_img = load_image("tuesday_3_2.png")
tuesday_4_img = load_image("tuesday_4.png")
tuesday_4_1_img = load_image("tuesday_4_1.png")
tuesday_4_2_img = load_image("tuesday_4_2.png")

# [수요일]
wednesday_1_img = load_image("wednesday_1.png")
wednesday_1_1_img = load_image("wednesday_1_1.png")
wednesday_1_2_img = load_image("wednesday_1_2.png")
wednesday_2_img = load_image("wednesday_2.png")
wednesday_2_1_img = load_image("wednesday_2_1.png")
wednesday_2_2_img = load_image("wednesday_2_2.png")
wednesday_3_img = load_image("wednesday_3.png")
wednesday_3_1_img = load_image("wednesday_3_1.png")
wednesday_3_2_img = load_image("wednesday_3_2.png")

# [목요일]
thursday_1_img = load_image("thursday_1.png")
thursday_1_1_img = load_image("thursday_1.png")
thursday_1_2_img = load_image("thursday_1.png")
thursday_2_img = load_image("thursday_2.png")
thursday_2_1_img = load_image("thursday_2.png")
thursday_2_2_img = load_image("thursday_2.png")
thursday_3_img = load_image("thursday_3.png")
thursday_3_1_img = load_image("thursday_3.png")
thursday_3_2_img = load_image("thursday_3.png")
thursday_4_img = load_image("thursday_4.png")

thursday_4_1_img = load_image("thursday_4.png")
thursday_4_2_img = load_image("thursday_4.png")

# 엔딩 이미지
IMG_H = int(SCREEN_HEIGHT * 0.6)
ending_imgs = {
    "bad": load_image("f.png", SCREEN_WIDTH, IMG_H),
    "normal_bad": load_image("c.png", SCREEN_WIDTH, IMG_H),
    "normal_good": load_image("b.png", SCREEN_WIDTH, IMG_H),
    "perfect": load_image("a.png", SCREEN_WIDTH, IMG_H)
}

# --- 버튼 위치 설정 ---
start_btn = pygame.Rect(START_BUTTON_RECT)
next_btn = pygame.Rect(NEXT_BUTTON_RECT)
shoes_on_btn = pygame.Rect(BTN_SHOES_ON_RECT)
shoes_off_btn = pygame.Rect(BTN_SHOES_OFF_RECT)

result_next_btn = pygame.Rect(580, 370, 200, 45)

check_result_btn = pygame.Rect(BTN_CHECK_RESULT_RECT)
restart_btn = pygame.Rect(BTN_RESTART_RECT)