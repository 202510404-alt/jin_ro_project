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
# 🌟 [보강] settings에서 가상 크기와 실제 윈도우 창 크기를 모두 가져옵니다.
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, VIRTUAL_WIDTH, VIRTUAL_HEIGHT, FPS, GROUND_Y
from player.player_main import Player
from map_system.map_main import GameMap
from jin_ro_project.src.enemy.enemys.dummy.dummy_main import DummyEnemy  # 🎯 새롭게 추가된 더미 몹

def main():
    pygame.init()
    
    # 🖥️ 1. 내 모니터 화면 밖으로 탈출하지 않는 '실제 윈도우 창 크기'의 화면 생성
    window_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("산나비 스타일 - 콤보 액션 및 더미 테스트")
    
    # 🎮 2. 내부 연산 및 그리기가 이루어질 '거대한 가상 스크린 도화지' 생성
    # 모든 물리 연산과 좌표는 이 가상 스크린 크기를 기준으로 작동하며, 숫자가 클수록 줌아웃 효과가 생깁니다.
    virtual_screen = pygame.Surface((VIRTUAL_WIDTH, VIRTUAL_HEIGHT))
    
    clock = pygame.time.Clock()

    # 객체 생성 (플레이어 배치 위치 세팅 - 가상 스크린의 GROUND_Y에 맞춰 안착)
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

        # 1. 서브 시스템 실시간 업데이트 연산 (가상 해상도 좌표계 기준)
        # 맵 시스템이 가진 플랫폼 리스트를 플레이어에게 넘겨 바닥 충돌 처리
        player.update(game_map.platforms)
        game_map.update()
        
        # ⚔️ [핵심 상호작용] 더미에게 플레이어 객체를 통째로 넘겨서 공격 범위 충돌 및 콤보 신호 전송 처리
        dummy.update(player)

        # 2. 🎨 [핵심 변경] 모든 그리기 연산은 모니터 창이 아니라 '가상 스크린 도화지'에 처리합니다.
        virtual_screen.fill((0, 0, 0))   # 기본 검은 배경 시야 확보
        
        game_map.draw(virtual_screen)   # 배경 및 지형 플랫폼 렌더링
        dummy.draw(virtual_screen)      # 🎯 더미 몬스터 및 머리 위 HP 바 UI 렌더링
        player.draw(virtual_screen)     # 플레이어 본체 및 콤보 검기 이펙트 렌더링

        # 3. 🔍 [줌아웃 압축 엔진] 거대한 가상 스크린을 실제 창 크기(SCREEN_WIDTH/HEIGHT)로 완벽히 압축 스케일링
        scaled_surface = pygame.transform.smoothscale(
            virtual_screen, 
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )
        
        # 실제 내 모니터 화면(window_screen)에 최종 압축된 도화지를 얹어서 출력
        window_screen.blit(scaled_surface, (0, 0))

        # 4. 디버그 타이틀 바 출력
        pygame.display.set_caption(
            f"상태: {player.vars.current_state} | 콤보단계: {player.vars.combo_step} | 더미HP: {dummy.vars.hp}"
        )
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()