import pygame
from setting.settings import *
from setting import assets
from setting.utils import init_fonts, draw_multiline_text, draw_stat_box

fonts = init_fonts()


def render(real_screen, data):
    virtual_screen = pygame.Surface((data.base_width, data.base_height))
    virtual_screen.fill(WHITE)

    if data.state == "start":
        if assets.start_bg_img:
            virtual_screen.blit(assets.start_bg_img, (0, 0))
        else:
            virtual_screen.fill(GRAY)

    elif data.state == "input_name":
        if assets.input_name_bg_img:
            virtual_screen.blit(assets.input_name_bg_img, (0, 0))
        else:
            virtual_screen.fill(SKY_BLUE)

        prompt = fonts['title'].render("당신의 이름을 입력하세요:", True, BLACK)
        virtual_screen.blit(prompt, (SCREEN_WIDTH // 2 - prompt.get_width() // 2, 200))

        input_rect = (SCREEN_WIDTH // 2 - 250, 300, 500, 100)
        pygame.draw.rect(virtual_screen, WHITE, input_rect)
        pygame.draw.rect(virtual_screen, BLUE, input_rect, 3)

        name_surf = fonts['name'].render(data.player_name, True, BLACK)
        virtual_screen.blit(name_surf, (SCREEN_WIDTH // 2 - name_surf.get_width() // 2, 330))
        virtual_screen.blit(fonts['ui'].render("입력 후 [Enter]", True, DARK_GRAY), (SCREEN_WIDTH // 2 - 70, 420))

    elif data.state == "check_name":
        if assets.input_name_bg_img:
            virtual_screen.blit(assets.input_name_bg_img, (0, 0))
        else:
            virtual_screen.fill(SKY_BLUE)

        pygame.draw.rect(virtual_screen, WHITE, (150, 150, 500, 300))
        pygame.draw.rect(virtual_screen, DARK_GRAY, (150, 150, 500, 300), 2)

        q = fonts['title'].render("이 이름이 맞습니까?", True, BLACK)
        n = fonts['name'].render(f"[{data.player_name}]", True, BLUE)
        virtual_screen.blit(q, (SCREEN_WIDTH // 2 - q.get_width() // 2, 200))
        virtual_screen.blit(n, (SCREEN_WIDTH // 2 - n.get_width() // 2, 280))

        yes_text = fonts['title'].render("1. 예", True, GREEN)
        no_text = fonts['title'].render("2. 아니요", True, RED)
        virtual_screen.blit(yes_text, (250, 380))
        virtual_screen.blit(no_text, (420, 380))

    elif data.state == "how_to_play":
        if assets.how_to_play_img: virtual_screen.blit(assets.how_to_play_img, (0, 0))

    elif data.state == "game_start_scene":
        if assets.game_start_scene_img:
            virtual_screen.blit(assets.game_start_scene_img, (0, 0))
        else:
            virtual_screen.fill(GRAY)

    elif data.state == "opening":
        if assets.opening_img: virtual_screen.blit(assets.opening_img, (0, 0))

    elif data.state == "opening_result":
        virtual_screen.fill(LIGHT_YELLOW)
        pygame.draw.rect(virtual_screen, WHITE, (50, 50, 700, 500))
        pygame.draw.rect(virtual_screen, BLACK, (50, 50, 700, 500), 3)

        if hasattr(data, "opening_lines"):
            current_text = data.opening_lines[data.opening_index]
            draw_multiline_text(virtual_screen, current_text, (80, 180), fonts['text'], BLACK)
        elif data.opening_text:
            draw_multiline_text(virtual_screen, data.opening_text, (80, 180), fonts['text'], BLACK)

        btn_rect = assets.result_next_btn
        pygame.draw.rect(virtual_screen, WHITE, btn_rect, 0, 10)
        pygame.draw.rect(virtual_screen, BLACK, btn_rect, 2, 10)

        if hasattr(data, "opening_lines") and data.opening_index < len(data.opening_lines) - 1:
            btn_txt = "계속 읽기 ▼"
        else:
            btn_txt = "시작하기 ▶"

        ts = fonts['ui'].render(btn_txt, True, BLACK)
        virtual_screen.blit(ts, (btn_rect.centerx - ts.get_width() // 2, btn_rect.centery - ts.get_height() // 2))

    elif data.state == "story":
        story = data.full_story[data.current_step]
        use_custom_bg = False
        bg_img = None

        if data.current_step == 1 and assets.monday_1_img:
            bg_img = assets.monday_1_img; use_custom_bg = True
        elif data.current_step == 2 and assets.monday_2_img:
            bg_img = assets.monday_2_img; use_custom_bg = True
        elif data.current_step == 3 and assets.monday_3_img:
            bg_img = assets.monday_3_img; use_custom_bg = True
        elif data.current_step == 4 and assets.monday_4_img:
            bg_img = assets.monday_4_img; use_custom_bg = True
        elif data.current_step == 5 and assets.tuesday_1_img:
            bg_img = assets.tuesday_1_img; use_custom_bg = True
        elif data.current_step == 6 and assets.tuesday_2_img:
            bg_img = assets.tuesday_2_img; use_custom_bg = True
        elif data.current_step == 7 and assets.tuesday_3_img:
            bg_img = assets.tuesday_3_img; use_custom_bg = True
        elif data.current_step == 8 and assets.tuesday_4_img:
            bg_img = assets.tuesday_4_img; use_custom_bg = True
        elif data.current_step == 9 and assets.wednesday_1_img:
            bg_img = assets.wednesday_1_img; use_custom_bg = True
        elif data.current_step == 10 and assets.wednesday_2_img:
            bg_img = assets.wednesday_2_img; use_custom_bg = True
        elif data.current_step == 11 and assets.wednesday_3_img:
            bg_img = assets.wednesday_3_img; use_custom_bg = True
        elif data.current_step == 12 and assets.thursday_1_img:
            bg_img = assets.thursday_1_img; use_custom_bg = True
        elif data.current_step == 13 and assets.thursday_2_img:
            bg_img = assets.thursday_2_img; use_custom_bg = True
        elif data.current_step == 14 and assets.thursday_3_img:
            bg_img = assets.thursday_3_img; use_custom_bg = True
        elif data.current_step == 15 and assets.thursday_4_img:
            bg_img = assets.thursday_4_img; use_custom_bg = True

        if use_custom_bg:
            virtual_screen.blit(bg_img, (0, 0))

            choice_y_offset = 0
            choice_x_offset = 0

            if data.current_step == 2:
                title_color = BLACK;
                main_text_color = BLACK;
                choice_text_color = WHITE
            elif data.current_step == 3:
                title_color = WHITE;
                main_text_color = BLACK;
                choice_text_color = WHITE
                choice_x_offset = 13
            elif data.current_step == 4:
                title_color = BLACK;
                main_text_color = BLACK;
                choice_text_color = WHITE
            elif data.current_step == 5:
                title_color = BLACK;
                main_text_color = WHITE;
                choice_text_color = WHITE
                choice_x_offset = 50
            elif data.current_step == 6:
                title_color = BLACK;
                main_text_color = WHITE;
                choice_text_color = WHITE
            elif data.current_step == 7:
                title_color = BLACK;
                main_text_color = WHITE;
                choice_text_color = WHITE
            elif data.current_step == 8:
                title_color = BLACK;
                main_text_color = BLACK;
                choice_text_color = WHITE
                choice_x_offset = 40
            elif data.current_step == 9:
                title_color = WHITE;
                main_text_color = WHITE;
                choice_text_color = WHITE
            elif data.current_step == 10:
                title_color = WHITE;
                main_text_color = WHITE;
                choice_text_color = WHITE
            elif data.current_step == 11:
                title_color = BLACK;
                main_text_color = BLACK;
                choice_text_color = WHITE
                choice_x_offset = 60
            elif data.current_step == 12:
                title_color = WHITE;
                main_text_color = BLACK;
                choice_text_color = WHITE
                choice_x_offset = 60
            elif data.current_step == 13:
                title_color = WHITE;
                main_text_color = WHITE;
                choice_text_color = WHITE
                choice_x_offset = 60
            elif data.current_step == 14:
                title_color = BLACK;
                main_text_color = BLACK;
                choice_text_color = WHITE
            elif data.current_step == 15:
                title_color = BLACK;
                main_text_color = BLACK;
                choice_text_color = WHITE
                choice_x_offset = 35
            else:
                title_color = WHITE;
                main_text_color = WHITE;
                choice_text_color = WHITE

            virtual_screen.blit(
                fonts['title'].render(f"[{data.player_name}의 {story['day_display']}]", True, title_color), (30, 20))

            if data.current_step == 5 or data.current_step == 6 or data.current_step == 10:
                box_rect = pygame.Rect(40, 140, SCREEN_WIDTH - 80, 150)
                transparent_surface = pygame.Surface((box_rect.width, box_rect.height), pygame.SRCALPHA)
                transparent_surface.fill((0, 0, 0, 150))
                virtual_screen.blit(transparent_surface, box_rect.topleft)

            draw_multiline_text(virtual_screen, story["text"], (60, 160), fonts['text'], main_text_color)

            c1_rect = pygame.Rect(STORY_V_CHOICE_1_RECT)
            c1_surf = fonts['text'].render(story["choice_1"], True, choice_text_color)
            c1_y = c1_rect.centery - c1_surf.get_height() // 2 + choice_y_offset
            virtual_screen.blit(c1_surf, (c1_rect.x + 20 + choice_x_offset, c1_y))

            c2_rect = pygame.Rect(STORY_V_CHOICE_2_RECT)
            c2_surf = fonts['text'].render(story["choice_2"], True, choice_text_color)
            c2_y = c2_rect.centery - c2_surf.get_height() // 2 + choice_y_offset
            virtual_screen.blit(c2_surf, (c2_rect.x + 20 + choice_x_offset, c2_y))

        else:
            virtual_screen.blit(fonts['title'].render(f"[{data.player_name}의 {story['day_display']}]", True, BLACK),
                                (30, 20))
            virtual_screen.blit(fonts['title'].render(story["title"], True, BLACK), (50, 150))
            pygame.draw.rect(virtual_screen, SKY_BLUE, (40, 210, 720, 180))
            pygame.draw.rect(virtual_screen, BLUE, (40, 210, 720, 180), 2)
            draw_multiline_text(virtual_screen, story["text"], (60, 230), fonts['text'], BLACK)

            pygame.draw.rect(virtual_screen, WHITE, (40, 410, 720, 60))
            pygame.draw.rect(virtual_screen, BLACK, (40, 410, 720, 60), 2)
            c1_surf = fonts['text'].render(story["choice_1"], True, BLACK)
            virtual_screen.blit(c1_surf, (60, 410 + 30 - c1_surf.get_height() // 2))

            pygame.draw.rect(virtual_screen, WHITE, (40, 480, 720, 60))
            pygame.draw.rect(virtual_screen, BLACK, (40, 480, 720, 60), 2)
            c2_surf = fonts['text'].render(story["choice_2"], True, BLACK)
            virtual_screen.blit(c2_surf, (60, 480 + 30 - c2_surf.get_height() // 2))

    elif data.state == "result":
        bg_drawn = False
        res_text_color = BLACK

        if data.current_step == 1:
            if data.last_choice == 1 and assets.monday_1_1_img:
                virtual_screen.blit(assets.monday_1_1_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
            elif data.last_choice == 2 and assets.monday_1_2_img:
                virtual_screen.blit(assets.monday_1_2_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
        elif data.current_step == 2:
            if data.last_choice == 1 and assets.monday_2_1_img:
                virtual_screen.blit(assets.monday_2_1_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
            elif data.last_choice == 2 and assets.monday_2_2_img:
                virtual_screen.blit(assets.monday_2_2_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
        elif data.current_step == 3:
            if data.last_choice == 1 and assets.monday_3_1_img:
                virtual_screen.blit(assets.monday_3_1_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
            elif data.last_choice == 2 and assets.monday_3_2_img:
                virtual_screen.blit(assets.monday_3_2_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
        elif data.current_step == 4:
            if data.last_choice == 1 and assets.monday_4_1_img:
                virtual_screen.blit(assets.monday_4_1_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
            elif data.last_choice == 2 and assets.monday_4_2_img:
                virtual_screen.blit(assets.monday_4_2_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
        elif data.current_step == 5:
            if data.last_choice == 1 and assets.tuesday_1_1_img:
                virtual_screen.blit(assets.tuesday_1_1_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
            elif data.last_choice == 2 and assets.tuesday_1_2_img:
                virtual_screen.blit(assets.tuesday_1_2_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
        elif data.current_step == 6:
            if data.last_choice == 1 and assets.tuesday_2_1_img:
                virtual_screen.blit(assets.tuesday_2_1_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
            elif data.last_choice == 2 and assets.tuesday_2_2_img:
                virtual_screen.blit(assets.tuesday_2_2_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
        elif data.current_step == 7:
            if data.last_choice == 1 and assets.tuesday_3_1_img:
                virtual_screen.blit(assets.tuesday_3_1_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
            elif data.last_choice == 2 and assets.tuesday_3_2_img:
                virtual_screen.blit(assets.tuesday_3_2_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
        elif data.current_step == 8:
            if data.last_choice == 1 and assets.tuesday_4_1_img:
                virtual_screen.blit(assets.tuesday_4_1_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
            elif data.last_choice == 2 and assets.tuesday_4_2_img:
                virtual_screen.blit(assets.tuesday_4_2_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
        elif data.current_step == 9:
            if data.last_choice == 1 and assets.wednesday_1_1_img:
                virtual_screen.blit(assets.wednesday_1_1_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
            elif data.last_choice == 2 and assets.wednesday_1_2_img:
                virtual_screen.blit(assets.wednesday_1_2_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
        elif data.current_step == 10:
            if data.last_choice == 1 and assets.wednesday_2_1_img:
                virtual_screen.blit(assets.wednesday_2_1_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
            elif data.last_choice == 2 and assets.wednesday_2_2_img:
                virtual_screen.blit(assets.wednesday_2_2_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
        elif data.current_step == 11:
            if data.last_choice == 1 and assets.wednesday_3_1_img:
                virtual_screen.blit(assets.wednesday_3_1_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
            elif data.last_choice == 2 and assets.wednesday_3_2_img:
                virtual_screen.blit(assets.wednesday_3_2_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
        elif data.current_step == 12:
            if data.last_choice == 1 and assets.thursday_1_1_img:
                virtual_screen.blit(assets.thursday_1_1_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
            elif data.last_choice == 2 and assets.thursday_1_2_img:
                virtual_screen.blit(assets.thursday_1_2_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
        elif data.current_step == 13:
            if data.last_choice == 1 and assets.thursday_2_1_img:
                virtual_screen.blit(assets.thursday_2_1_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
            elif data.last_choice == 2 and assets.thursday_2_2_img:
                virtual_screen.blit(assets.thursday_2_2_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
        elif data.current_step == 14:
            if data.last_choice == 1 and assets.thursday_3_1_img:
                virtual_screen.blit(assets.thursday_3_1_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
            elif data.last_choice == 2 and assets.thursday_3_2_img:
                virtual_screen.blit(assets.thursday_3_2_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
        elif data.current_step == 15:
            if data.last_choice == 1 and assets.thursday_4_1_img:
                virtual_screen.blit(assets.thursday_4_1_img, (0, 0)); bg_drawn = True; res_text_color = WHITE
            elif data.last_choice == 2 and assets.thursday_4_2_img:
                virtual_screen.blit(assets.thursday_4_2_img, (0, 0)); bg_drawn = True; res_text_color = WHITE

        if bg_drawn:
            current_text = data.result_lines[data.result_index]
            draw_multiline_text(virtual_screen, current_text, (70, 455), fonts['text'], res_text_color, 660)

        else:
            virtual_screen.blit(fonts['title'].render("결과 확인", True, BLACK), (30, 20))
            pygame.draw.rect(virtual_screen, (255, 245, 245), (100, 150, 600, 300))
            pygame.draw.rect(virtual_screen, RED, (100, 150, 600, 300), 2)
            current_text = data.result_lines[data.result_index]
            draw_multiline_text(virtual_screen, current_text, (130, 250), fonts['text'], BLACK, 540)

        btn_text = "다음 수업으로 ▶"
        if data.result_index == len(data.result_lines) - 1:
            if data.current_step in [4, 8, 11]:
                btn_text = "내일로 ▶"
            elif data.current_step == 15:
                btn_text = "최종 점수 확인 ★"
        else:
            btn_text = "계속 읽기 ▼"

        btn_rect = assets.result_next_btn
        pygame.draw.rect(virtual_screen, WHITE, btn_rect, 0, 10)
        pygame.draw.rect(virtual_screen, BLACK, btn_rect, 2, 10)

        ts = fonts['ui'].render(btn_text, True, BLACK)
        virtual_screen.blit(ts, (btn_rect.centerx - ts.get_width() // 2, btn_rect.centery - ts.get_height() // 2))

    elif data.state == "score_screen":
        if assets.final_score_bg_img:
            virtual_screen.blit(assets.final_score_bg_img, (0, 0))
        else:
            virtual_screen.fill(LIGHT_YELLOW)

        virtual_screen.blit(fonts['title'].render(f"{data.final_score} 점", True, BLACK), (SCREEN_WIDTH // 2 - 60, 250))
        virtual_screen.blit(fonts['title'].render(f"HP : {data.energy}", True, RED), (SCREEN_WIDTH // 2 - 60, 350))

    elif data.state == "ending":
        if data.final_score < 25:
            key = "bad"
        elif data.final_score < 50:
            key = "normal_bad"
        elif data.final_score < 75:
            key = "normal_good"
        else:
            key = "perfect"

        e_data = data.ending_data[key]
        e_img = assets.ending_imgs[key]

        if getattr(data, "ending_key_cache", None) != key:
            data.ending_key_cache = key
            full_text = e_data["text"]
            lines = full_text.strip().split('\n')

            data.ending_lines = []
            chunk = []
            for line in lines:
                chunk.append(line)
                if len(chunk) == 3:
                    data.ending_lines.append(chunk)
                    chunk = []
            if chunk:
                data.ending_lines.append(chunk)

            data.ending_index = 0

        if e_img:
            scaled_e_img = pygame.transform.scale(e_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
            virtual_screen.blit(scaled_e_img, (0, 0))

        text_color = BLACK

        box_start_y = SCREEN_HEIGHT - 250
        title_y = box_start_y + 40
        text_y = title_y + 60

        title_surf = fonts['title'].render(e_data["title"], True, WHITE)
        virtual_screen.blit(title_surf, (30, 30))

        # 본문 출력
        if hasattr(data, "ending_lines") and data.ending_lines:
            current_chunk_list = data.ending_lines[data.ending_index]
            current_chunk_str = "\n".join(current_chunk_list)
            # 위치: 하단 텍스트 영역
            draw_multiline_text(virtual_screen, current_chunk_str, (70, text_y), fonts['text'], text_color,
                                SCREEN_WIDTH - 140)

        btn_rect = assets.result_next_btn
        pygame.draw.rect(virtual_screen, WHITE, btn_rect, 0, 10)
        pygame.draw.rect(virtual_screen, BLACK, btn_rect, 2, 10)

        if data.ending_index < len(data.ending_lines) - 1:
            btn_txt = "계속 읽기 ▼"
        else:
            btn_txt = "처음으로 ↻"

        ts = fonts['ui'].render(btn_txt, True, BLACK)
        virtual_screen.blit(ts, (btn_rect.centerx - ts.get_width() // 2, btn_rect.centery - ts.get_height() // 2))

    elif data.state == "game_over":
        virtual_screen.fill(BLACK)
        title = fonts['title'].render("GAME OVER", True, RED)
        virtual_screen.blit(title, (300, 200))
        desc = fonts['text'].render("체력이 다해 쓰러졌습니다.", True, WHITE)
        virtual_screen.blit(desc, (280, 300))

        pygame.draw.rect(virtual_screen, BUTTON_COLOR, assets.restart_btn)
        pygame.draw.rect(virtual_screen, WHITE, assets.restart_btn, 2)
        btn_text = fonts['ui'].render("다시 시작", True, BLACK)
        tx = assets.restart_btn.centerx - btn_text.get_width() // 2
        ty = assets.restart_btn.centery - btn_text.get_height() // 2
        virtual_screen.blit(btn_text, (tx, ty))

    scaled_screen = pygame.transform.scale(virtual_screen, (data.current_width, data.current_height))
    real_screen.blit(scaled_screen, (0, 0))