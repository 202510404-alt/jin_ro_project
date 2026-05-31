# src/map_system/map_main.py
import pygame
import sys
import os
import json  # 🌟 JSON 파일을 읽기 위해 내장 모듈 추가
from map_system.variables import MapVariables
from platform_system.platform_main import Platform

class GameMap:
    def __init__(self, map_id=1):
        self.map_id = map_id
        self.platforms = []
        
        # 🌟 1. JSON 파일로부터 데이터 로드 및 변수 초기화
        self.load_map_from_json()
        
        # 2. 이미지 에셋 로드
        self.load_map_assets()
        
        # 3. 로드된 데이터를 바탕으로 실제 플랫폼 객체들 조립 생성
        self.build_map()

    def load_map_from_json(self):
        """🌟 maps 폴더 안의 json 파일을 읽어 맵 데이터를 세팅합니다."""
        # 🌟 현재 파일 위치(src/map_system)를 기준으로 명확한 절대 경로 조립
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(current_dir, "maps", f"map{self.map_id}.json")
        
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                map_data = json.load(f)
                
            # JSON에 적힌 데이터를 기반으로 MapVariables 객체 생성
            self.vars = MapVariables(
                map_id=map_data["map_id"],
                width=map_data["map_width"],
                height=map_data["map_height"]
            )
            # JSON 파일에 적힌 세부 값들로 오버라이딩(덮어쓰기)
            self.vars.background_type = map_data["background_type"]
            self.vars.ground_type = map_data["ground_type"]
            self.vars.ground_y = map_data["ground_y"]
            
            # 🧱 임시 리스트에 플랫폼 데이터 저장
            self.raw_platform_data = map_data["platforms"]
            
        except FileNotFoundError:
            print(f"\n❌ 에러: 맵 데이터 파일({json_path})을 찾을 수 없습니다!")
            pygame.quit()
            sys.exit()
        except json.JSONDecodeError:
            print(f"\n❌ 에러: {json_path} 파일의 JSON 문법이 올바르지 않습니다.")
            pygame.quit()
            sys.exit()

    def load_map_assets(self):
        # 🌟 현재 파일 위치에서 부모인 src/ 폴더 위치를 구한 후 assets 경로 조립
        src_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        bg_dir = os.path.join(src_dir, "assets", "images", "map", "background")
        ground_dir = os.path.join(src_dir, "assets", "images", "map", "ground")
        
        try:
            self.bg_image = pygame.image.load(os.path.join(bg_dir, f"{self.vars.background_type}.png")).convert_alpha()
            # 🌟 [보강] 바닥 타일 이미지 로딩부도 안전하게 절대 경로 연동
            self.ground_image = pygame.image.load(os.path.join(ground_dir, f"{self.vars.ground_type}.png")).convert_alpha()
        except pygame.error as e:
            print(f"\n❌ 에러: 맵 이미지 에셋 로드 실패! ({e})")
            pygame.quit()
            sys.exit()

    def build_map(self):
        """🌟 JSON에서 파싱해 둔 원시 데이터를 돌며 실제 가동 가능한 플랫폼 객체를 생성합니다."""
        for p_data in self.raw_platform_data:
            platform_obj = Platform(
                x=p_data["x"],
                y=p_data["y"],
                width=p_data["width"],
                height=p_data["height"],
                is_visible=p_data.get("is_visible", True),
                can_pass_through=p_data.get("can_pass_through", False)
            )
            self.platforms.append(platform_obj)

    def update(self):
        """매 프레임 배치된 모든 플랫폼 지형의 상태를 업데이트합니다."""
        for platform in self.platforms:
            platform.update()

    def draw(self, screen):
        """배경, 바닥 지형, 그리고 공중 플랫폼 지형들을 순서대로 화면에 렌더링합니다."""
        # 1. 배경 하늘 출력 (1600x1200 화면에 꽉 차게 고정)
        scaled_bg = pygame.transform.scale(self.bg_image, (screen.get_width(), screen.get_height()))
        screen.blit(scaled_bg, (0, 0))
        
        # 2. 🧱 공중 발판들 그리기
        for platform in self.platforms:
            platform.draw(screen)

        # 3. 🧱 흙바닥 지형 그리기
        import settings  # settings.py의 동적 GROUND_Y를 가져오기 위함
        
        ground_w = self.ground_image.get_width()
        
        # 🌟 JSON의 낡은 값을 무시하고, settings.py에서 계산된 화면 비례 높이로 강제 동기화
        self.vars.ground_y = settings.GROUND_Y
        
        # 맵의 총 가로 길이만큼 타일을 루프 돌며 이어 붙여서 출력
        for x_pos in range(0, self.vars.width, ground_w):
            screen.blit(self.ground_image, (x_pos, self.vars.ground_y))