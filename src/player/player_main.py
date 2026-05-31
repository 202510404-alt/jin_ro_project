# src/player/player_main.py
import pygame
from player.variables import PlayerVariables
from player.input_handler import PlayerInputHandler
from player.asset_loader import PlayerAssetLoader          # 🌟 절대경로 추적 로더 연동
from player.physics_processor import PlayerPhysicsProcessor # 🌟 물리 엔진 연동
from player.combat_processor import PlayerCombatProcessor   # 🌟 전투 엔진 연동
from player.motions.ground_motions import GroundMotions
from player.motions.air_motions import AirMotions
from player.motions.attack_motions import AttackMotions

class Player:
    def __init__(self, x, y):
        # 데이터 및 입력 핸들러 초기화
        self.vars = PlayerVariables(x, y)
        self.input_handler = PlayerInputHandler()
        
        # 🌟 분리된 컴포넌트 조립 (경로 수정이 완료된 에셋 로더 가동)
        self.assets = PlayerAssetLoader(self.vars)
        self.physics_engine = PlayerPhysicsProcessor()
        self.combat_engine = PlayerCombatProcessor()
        
        # 애니메이션 모션 판독기들 조립
        self.ground_motion_processor = GroundMotions()
        self.air_motion_processor = AirMotions()
        self.attack_motion_processor = AttackMotions()

    def update_animation_state(self):
        """현재 플레이어 변수를 분석해 상태 문자열(애니메이션 키)을 결정합니다."""
        # 1. 공격 상태 모션 우선 검사
        attack_state = self.attack_motion_processor.handle_state(self.vars)
        if attack_state:
            self.vars.current_state = attack_state
            return

        # 2. 공중 상태 모션 검사
        air_state = self.air_motion_processor.handle_state(self.vars)
        if air_state:
            self.vars.current_state = air_state
            return

        # 3. 지상 상태 모션 검사
        ground_state = self.ground_motion_processor.handle_state(self.vars)
        if ground_state:
            self.vars.current_state = ground_state

    def update(self, platforms):
        """매 프레임 플레이어의 입력, 물리, 전투, 애니메이션 상태를 업데이트합니다."""
        # 키보드 및 마우스 입력 처리
        self.input_handler.update(self.vars)
        
        # 발판 충돌을 포함한 물리 연산 처리
        if hasattr(self.physics_engine, 'process'):
            self.physics_engine.process(self.vars, platforms)
            
        # ⚔️ 콤보 공격 타이머 및 히트박스 생성 연산 처리
        if hasattr(self.combat_engine, 'process'):
            self.combat_engine.process(self.vars)
            
        # 모든 연산이 끝난 후 최종 애니메이션 상태 판정
        self.update_animation_state()

    def draw(self, screen):
        """플레이어 본체 이미지와 공격 시 콤보 이펙트를 화면에 렌더링합니다."""
        # 1. 캐릭터 본체 그리기
        player_image = self.assets.images[self.vars.current_state]
        
        # 왼쪽을 바라보고 있다면 이미지 좌우 반전
        if not self.vars.facing_right:
            player_image = pygame.transform.flip(player_image, True, False)
            
        screen.blit(player_image, (self.vars.x, self.vars.y))
        
        # 2. ⚔️ 공격 애니메이션 중일 때 콤보 검기 이펙트 출력
        if self.vars.is_attacking and self.vars.combo_step in self.assets.effect_images:
            effect_img = self.assets.effect_images[self.vars.combo_step]
            
            # 플레이어가 바라보는 방향에 맞춰 이펙트도 반전 및 위치 정렬
            if self.vars.facing_right:
                # 플레이어 오른쪽에 이펙트 배치
                effect_x = self.vars.x + self.vars.width
                screen.blit(effect_img, (effect_x, self.vars.y))
            else:
                # 이펙트 이미지를 반전시켜 플레이어 왼쪽에 배치
                effect_img = pygame.transform.flip(effect_img, True, False)
                effect_x = self.vars.x - (self.vars.width * 2)
                screen.blit(effect_img, (effect_x, self.vars.y))