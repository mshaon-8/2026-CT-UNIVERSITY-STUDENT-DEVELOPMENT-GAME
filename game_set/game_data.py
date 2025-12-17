from setting import story_loader
from setting.settings import SCREEN_WIDTH, SCREEN_HEIGHT


class GameData:
    def __init__(self):
        self.reset_data()
        self.full_story = story_loader.load_all_stories()
        self.ending_data = story_loader.load_endings()

        self.base_width = SCREEN_WIDTH
        self.base_height = SCREEN_HEIGHT
        self.current_width = SCREEN_WIDTH
        self.current_height = SCREEN_HEIGHT

    def reset_data(self):
        self.state = "start"
        self.player_name = ""
        self.current_step = 1
        self.max_step = 15

        self.gpa = 3.0
        self.energy = 80
        self.final_score = 0

        self.opening_text = ""
        self.result_text = ""

        self.last_choice = 0
        self.result_lines = []
        self.result_index = 0