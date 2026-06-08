# src/enemy/dummy/dummy_main.py
import pygame
import os
import sys
from jin_ro_project.src.enemy.enemys.dummy.variables import DummyVariables

class DummyEnemy:
    def __init__(self, x, y):
        self.vars = DummyVariables(x, y)
        self.load_images()

    def load_images(self):
        """🌟 트리 구조에 맞춰 src/assets/images/enemy/dummy 경로를 정밀 타격합니다."""
        # 현재 dummy_main.py의 위치(src/enemy/dummy)에서 부모의 부모인 src/ 폴더를 찾습니다.
        current_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
        # 정확히 src/assets/images/enemy/dummy 경로로 매칭
        dummy_dir = os.path.join(current_dir, "assets", "images", "enemy", "dummy")
        
        try:
            self.images = {
                "IDLE": pygame.image.load(os.path.join(dummy_dir, "dummy_idle.png")).convert_alpha(),
                "HIT": pygame.image.load(os.path.join(dummy_dir, "dummy_hit.png")).convert_alpha(),
                "DEAD": pygame.image.load(os.path.join(dummy_dir, "dummy_dead.png")).convert_alpha()
            }
            for state in self.images:
                self.images[state] = pygame.transform.scale(self.images[state], (self.vars.width, self.vars.height))
        except pygame.error as e:
            print(f"\n❌ 에러: 더미 에셋 로드 실패! ({e})")
            print(f"참조하려던 절대 경로: {dummy_dir}")
            pygame.quit()
            sys.exit()

    def check_player_attack(self, player_obj):
        """플레이어의 실시간 공격 히트박스 충돌 감지"""
        if not player_obj.vars.is_attacking or not player_obj.vars.attack_rect:
            return

        dummy_rect = pygame.Rect(self.vars.x, self.vars.y, self.vars.width, self.vars.height)

        if dummy_rect.colliderect(player_obj.vars.attack_rect):
            if not self.vars.is_hit:
                self.vars.is_hit = True
                self.vars.hit_timer = self.vars.hit_duration
                self.vars.hp -= 10
                
                # 플레이어의 콤보 카운트 트리거 작동 유도
                player_obj.vars.has_hit_enemy = True
                print(f"💥 더미 피격 성공! 남은 HP: {self.vars.hp}/100")

    def update(self, player_obj):
        if self.vars.hp <= 0:
            return

        self.check_player_attack(player_obj)

        if self.vars.is_hit:
            self.vars.hit_timer -= 1
            if self.vars.hit_timer <= 0:
                self.vars.is_hit = False

    def draw(self, screen):
        if self.vars.hp <= 0:
            current_img = self.images["DEAD"]
        elif self.vars.is_hit:
            current_img = self.images["HIT"]
        else:
            current_img = self.images["IDLE"]

        screen.blit(current_img, (self.vars.x, self.vars.y))
        
        # ❤️ HP Bar UI 출력
        if self.vars.hp > 0:
            bar_width = self.vars.width
            bar_height = 6
            bar_x = self.vars.x
            bar_y = self.vars.y - 12
            pygame.draw.rect(screen, (50, 50, 50), (bar_x, bar_y, bar_width, bar_height))
            hp_ratio = max(0, self.vars.hp / self.vars.max_hp)
            pygame.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, int(bar_width * hp_ratio), bar_height))