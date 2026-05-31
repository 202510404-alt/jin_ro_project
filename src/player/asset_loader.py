# src/player/asset_loader.py
import pygame
import sys
import os

class PlayerAssetLoader:
    def __init__(self, vars_obj):
        self.images = {}
        self.effect_images = {}
        self.load_all_assets(vars_obj)

    def load_all_assets(self, vars_obj):
        # 🌟 현재 파일(src/player/asset_loader.py) 위치 기준 상위의 src/ 폴더 절대 경로 추출
        src_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # 정확히 src/assets/images/player 경로 조립
        base_dir = os.path.join(src_dir, "assets", "images", "player")
        move_dir = os.path.join(base_dir, "player_move")
        effect_dir = os.path.join(base_dir, "attack_effect")
        
        try:
            # 1. 캐릭터 모션 이미지 로드
            self.images = {
                "IDLE": pygame.image.load(os.path.join(move_dir, "player_idle.png")).convert_alpha(),
                "WALK": pygame.image.load(os.path.join(move_dir, "player_walk.png")).convert_alpha(),
                "RUN": pygame.image.load(os.path.join(move_dir, "player_run.png")).convert_alpha(),
                "JUMP_UP": pygame.image.load(os.path.join(move_dir, "player_jump_up.png")).convert_alpha(),
                "FALL": pygame.image.load(os.path.join(move_dir, "player_fall.png")).convert_alpha(),
                "ATTACK_1": pygame.image.load(os.path.join(move_dir, "player_attack1.png")).convert_alpha(),
                "ATTACK_2": pygame.image.load(os.path.join(move_dir, "player_attack2.png")).convert_alpha(),
                "ATTACK_3": pygame.image.load(os.path.join(move_dir, "player_attack3.png")).convert_alpha()
            }
            for state in self.images:
                self.images[state] = pygame.transform.scale(self.images[state], (vars_obj.width, vars_obj.height))

            # 2. 공격 콤보 이펙트 이미지 로드
            self.effect_images = {
                1: pygame.image.load(os.path.join(effect_dir, "effect_hit1.png")).convert_alpha(),
                2: pygame.image.load(os.path.join(effect_dir, "effect_hit2.png")).convert_alpha(),
                3: pygame.image.load(os.path.join(effect_dir, "effect_hit3.png")).convert_alpha()
            }
            for step in self.effect_images:
                # 🌟 원본 누락 코드 복구 및 규격 자동화 (이펙트 크기를 플레이어 크기에 비례하여 맞춤)
                self.effect_images[step] = pygame.transform.scale(
                    self.effect_images[step], (vars_obj.width * 2, vars_obj.height)
                )

        except pygame.error as e:
            print(f"\n❌ 에러: 플레이어 또는 이펙트 에셋 로드 실패! ({e})")
            print(f"참조 실패한 디렉터리: {base_dir}")
            pygame.quit()
            sys.exit()