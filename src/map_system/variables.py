# map_system/variables.py
import math
from map_system.map_settings import *

class MapVariables:
    def __init__(self, map_id=1, width=DEFAULT_MAP_WIDTH, height=DEFAULT_MAP_HEIGHT):
        """
        맵 전체 크기에 맞춰 배경과 바닥 이미지를 
        몇 개나 이어 붙여야 하는지 계산하고 저장하는 설계도
        """
        self.map_id = map_id
        self.width = width        # 예: 1600
        self.height = height      # 예: 600
        
        # 1. 🖼️ 배경 데이터 및 이어 붙일 개수 계산
        self.background_type = DEFAULT_BACKGROUND_TYPE
        self.bg_width = DEFAULT_BG_WIDTH
        self.bg_height = DEFAULT_BG_HEIGHT
        # 맵 전체를 채우기 위해 가로로 몇 장을 이어 붙여야 하는지 계산 (올림 처리)
        self.bg_repeat_count = math.ceil(self.width / self.bg_width) # 1600 / 800 = 2장
        
        # 2. 🪵 바닥 데이터 및 이어 붙일 개수 계산
        self.ground_type = DEFAULT_GROUND_TYPE
        self.ground_y = DEFAULT_GROUND_Y
        self.ground_tile_width = DEFAULT_GROUND_TILE_WIDTH
        self.ground_tile_height = DEFAULT_GROUND_TILE_HEIGHT
        # 맵 끝까지 바닥 타일을 몇 개나 도장 찍어야 하는지 계산
        self.ground_repeat_count = math.ceil(self.width / self.ground_tile_width) # 1600 / 64 = 25개
        
        # 3. 🧱 구조물 리스트 (기존 유지)
        self.platform_data_list = []
        self.trap_data_list = []