# src/player/variables.py
from settings import GROUND_Y # 🌟 src. 제거하여 경로 에러 방지

class PlayerVariables:
    def __init__(self, x, y):
        # 🧍 기본 물리 변수
        self.x = x
        self.y = y
        self.width = 40
        self.height = 60
        self.walk_speed = 4
        self.run_speed = 8
        self.jump_power = 16
        self.gravity = 0.8
        self.vertical_velocity = 0
        self.is_jumping = False
        self.current_state = "IDLE"
        self.facing_right = True
        self.is_moving = False
        self.move_state = "WALK"
        
        # ⚔️ 공격 및 콤보 관련 변수
        self.is_attacking = False       # 현재 공격 애니메이션/모션이 재생 중인가?
        self.combo_step = 0             # 0: 공격안함, 1: 1타, 2: 2타, 3: 3타
        self.attack_timer = 0           # 공격 모션이 유지되는 프레임 수
        self.attack_duration = 15       # 공격 모션 1회당 유지 시간
        self.has_hit_enemy = False      # 이번 공격 타수에서 적을 맞췄는가?
        
        # ⏱️ [콤보 유효 타이머] 변수 모음집에서 집중 관리하도록 설계
        # 60 FPS 기준 1.5초 = 90프레임 동안 다음 연타 입력을 기다립니다.
        self.combo_expire_time = 90     
        self.combo_timer = 0            # 실시간으로 줄어들 스케줄러 타이머
        
        # 📐 공격 범위(히트박스) 크기 설정
        self.attack_range_width = 80
        self.attack_range_height = 50
        self.attack_rect = None         # 실시간 공격 범위 사각형 (pygame.Rect)