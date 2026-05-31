# src/main.py
import pygame
import sys
import os

# 🌟 [보조 툴 및 패키지 경로 꼬임 방지 치트키]
# 어떤 환경에서 실행하든 이 파일이 위치한 src 폴더를 파이썬 모듈 검색 경로 최상단에 주입합니다.
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# 이제 시스템이 src 폴더 내부를 직접 바라보므로 'src.' 경로를 떼고 깔끔하게 임포트합니다.
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, GROUND_Y
from player.player_main import Player
from map_system.map_main import GameMap
from enemy.dummy.dummy_main import DummyEnemy  # 🎯 새롭게 추가된 더미 몹

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("산나비 스타일 - 콤보 액션 및 더미 테스트")
    clock = pygame.time.Clock()

    # 객체 생성 (플레이어 배치 위치 세팅)
    player = Player(100, GROUND_Y - 60)
    game_map = GameMap(map_id=1)
    
    # 🎯 더미 몬스터 소환 (x=500 위치에 배치, y는 더미 변수 내부에서 GROUND_Y 기준으로 안착)
    dummy = DummyEnemy(500, 0)

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 1. 서브 시스템 실시간 업데이트 연산
        # 맵 시스템이 가진 플랫폼 리스트를 플레이어에게 넘겨 바닥 충돌 처리
        player.update(game_map.platforms)
        game_map.update()
        
        # ⚔️ [핵심 상호작용] 더미에게 플레이어 객체를 통째로 넘겨서 공격 범위 충돌 및 콤보 신호 전송 처리
        dummy.update(player)

        # 2. 화면 렌더링 (그리는 순서가 레이어 순서가 됩니다: 배경/맵 -> 몬스터 -> 플레이어)
        screen.fill((0, 0, 0))  # 기본 검은 배경 시야 확보
        
        game_map.draw(screen)   # 배경 및 지형 플랫폼 렌더링
        dummy.draw(screen)      # 🎯 더미 몬스터 및 머리 위 HP 바 UI 렌더링
        player.draw(screen)     # 플레이어 본체 및 콤보 검기 이펙트 렌더링

        # 3. 디버그 타이틀 바 출력
        pygame.display.set_caption(
            f"상태: {player.vars.current_state} | 콤보단계: {player.vars.combo_step} | 더미HP: {dummy.vars.hp}"
        )
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()