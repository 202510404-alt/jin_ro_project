# src/enemy/dummy/variables.py
from settings import GROUND_Y

class DummyVariables:
    def __init__(self, x, y):
        # 📐 위치 및 크기 (기본 캐릭터보다 살짝 통통하게 설정)
        self.x = x
        self.y = y
        self.width = 50
        self.height = 70
        
        # ❤️ 능력치 상태
        self.hp = 100
        self.max_hp = 100
        
        # 💫 피격(Hit) 관련 상태 변수
        self.is_hit = False          # 현재 플레이어에게 맞아서 경직 상태인가?
        self.hit_timer = 0           # 경직 애니메이션 유지 타이머
        self.hit_duration = 10       # 맞았을 때 경직될 프레임 수 (약 0.16초)
        
        # 🧱 바닥 고정용 y축 계산
        self.ground_y = GROUND_Y - self.height
        self.y = self.ground_y  # 생성 시 자동으로 바닥에 안착