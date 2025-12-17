import pygame 
import sys
from setting.settings import *
from setting import assets
from game_set.game_data import GameData
from game_set import game_view, game_logic

# 1. 파이게임 초기화
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("대학생 키우기: Real Campus Life")
clock = pygame.time.Clock()

pygame.key.start_text_input()

# 2. 게임 데이터 객체 생성
data = GameData()

# 3. 메인 루프
running = True
while running:
    # --- 이벤트 처리 ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.TEXTINPUT:
            if data.state == "input_name":
                # 글자 수 제한 (10자)
                if len(data.player_name) < 10:
                    data.player_name += event.text


        elif event.type == pygame.KEYDOWN:

            # 1. 이름 입력 화면 (백스페이스, 엔터)
            if data.state == "input_name":
                if event.key == pygame.K_BACKSPACE:
                    data.player_name = data.player_name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(data.player_name) > 0:
                        data.state = "check_name"

            # 0. 시작 화면
            elif data.state == "start":
                if event.key == pygame.K_SPACE:
                    data.state = "input_name"

            # 2. 이름 확인
            elif data.state == "check_name":
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    data.state = "how_to_play"
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    data.player_name = ""; data.state = "input_name"

            # 3. 오프닝 (신발 선택)
            elif data.state == "opening":
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    game_logic.process_opening_choice(1, data)
                    data.state = "opening_result"
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    game_logic.process_opening_choice(2, data)
                    data.state = "opening_result"

            # 4. 스토리 진행
            elif data.state == "story":
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    game_logic.process_choice(1, data)
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    game_logic.process_choice(2, data)

            # 5. 단순 넘기기
            elif data.state in ["how_to_play", "game_start_scene"]:
                if event.key in [pygame.K_RETURN, pygame.K_SPACE]:
                    if data.state == "how_to_play":
                        data.state = "game_start_scene"
                    elif data.state == "game_start_scene":
                        data.state = "opening"

            # 6. 오프닝 결과
            elif data.state == "opening_result":
                if event.key in [pygame.K_RETURN, pygame.K_SPACE]:
                    if hasattr(data, "opening_lines") and data.opening_index < len(data.opening_lines) - 1:
                        data.opening_index += 1
                    else:
                        data.state = "story"

            # 7. 결과 화면
            elif data.state == "result":
                if event.key in [pygame.K_RETURN, pygame.K_SPACE]:
                    if data.result_index < len(data.result_lines) - 1:
                        data.result_index += 1
                    else:
                        game_logic.go_next_step(data)

            # 8. 엔딩 화면
            elif data.state == "ending":
                if event.key in [pygame.K_RETURN, pygame.K_SPACE]:
                    if hasattr(data, "ending_lines") and data.ending_index < len(data.ending_lines) - 1:
                        data.ending_index += 1
                    else:
                        running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if data.state in ["check_name", "opening"]:
                pass

            elif data.state == "opening_result":
                if assets.result_next_btn.collidepoint(pos):
                    if hasattr(data, "opening_lines") and data.opening_index < len(data.opening_lines) - 1:
                        data.opening_index += 1
                    else:
                        data.state = "story"

            elif data.state == "ending":
                if assets.result_next_btn.collidepoint(pos):
                    if hasattr(data, "ending_lines") and data.ending_index < len(data.ending_lines) - 1:
                        data.ending_index += 1
                    else:
                        running = False

            elif data.state == "result":
                if assets.result_next_btn.collidepoint(pos):
                    if data.result_index < len(data.result_lines) - 1:
                        data.result_index += 1
                    else:
                        game_logic.go_next_step(data)

            else:
                game_logic.process_click(pos, data)

    # --- 화면 그리기 ---
    game_view.render(screen, data)

    # --- 업데이트 ---
    pygame.display.flip()
    clock.tick(60)

# 종료
pygame.quit()
sys.exit()