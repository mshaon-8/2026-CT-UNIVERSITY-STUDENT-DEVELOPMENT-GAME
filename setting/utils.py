import pygame
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def init_fonts():
    """images 폴더 내의 DungGeunMo.ttf 폰트를 로드"""
    pygame.font.init()

    # 1. 폰트 경로 설정
    font_path = resource_path(os.path.join("images", "DungGeunMo.ttf"))

    # 2. 폰트 파일이 존재하는지 확인 및 로드
    if os.path.exists(font_path):
        try:
            return {
                'title': pygame.font.Font(font_path, 40),  # 제목
                'name': pygame.font.Font(font_path, 35),  # 이름 입력
                'text': pygame.font.Font(font_path, 22),  # 본문
                'ui': pygame.font.Font(font_path, 20)  # 버튼
            }
        except Exception as e:
            print(f"[오류] 폰트 로드 실패: {e}")

    # 3. 파일이 없을 경우 시스템 한글 폰트로 대체
    print(f"[알림] '{font_path}'를 찾을 수 없어 시스템 폰트를 사용합니다.")
    sys_font_path = None

    if os.name == 'nt':  # 윈도우
        paths = ["C:/Windows/Fonts/malgun.ttf", "C:/Windows/Fonts/gulim.ttf"]
        for p in paths:
            if os.path.exists(p):
                sys_font_path = p
                break
    elif os.name == 'posix':  # 맥/리눅스
        paths = ["/System/Library/Fonts/AppleGothic.ttf", "/Library/Fonts/NanumGothic.ttf"]
        for p in paths:
            if os.path.exists(p):
                sys_font_path = p
                break

    if sys_font_path:
        return {
            'title': pygame.font.Font(sys_font_path, 40),
            'name': pygame.font.Font(sys_font_path, 35),
            'text': pygame.font.Font(sys_font_path, 22),
            'ui': pygame.font.Font(sys_font_path, 20)
        }
    else:
        return {
            'title': pygame.font.SysFont("arial", 40),
            'name': pygame.font.SysFont("arial", 35),
            'text': pygame.font.SysFont("arial", 22),
            'ui': pygame.font.SysFont("arial", 20)
        }


def draw_multiline_text(surface, text, pos, font, color, max_width=None):
    """줄바꿈 문자가 포함된 텍스트를 화면에 그립니다."""
    if isinstance(text, list):
        text = "\n".join(text)

    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]

    line_spacing = 8

    x, y = pos

    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()

            # 가로 길이 넘어가면 줄바꿈
            if max_width and x + word_width >= max_width + pos[0]:
                x = pos[0]
                y += word_height + line_spacing

            surface.blit(word_surface, (x, y))
            x += word_width + space

        # 강제 줄바꿈 (\n) 시
        x = pos[0]
        y += font.get_height() + line_spacing


def draw_stat_box(surface, gpa, energy, x, y):
    pass