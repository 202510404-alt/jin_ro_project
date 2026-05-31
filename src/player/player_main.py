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
        # 🚀 [커스텀 규칙] 점프 선딜레이 타이머가 돌고 있다면 다른 상태 판정을 전부 무시하고 READY_JUMP 상태 강제 고정
        if hasattr(self.vars, 'ready_jump_timer') and self.vars.ready_jump_timer > 0:
            self.vars.ready_jump_timer -= 1
            self.vars.current_state = "READY_JUMP"
            return

        # 1. 공격 상태 모션 우선 검사
        attack_state = self.attack_motion_processor.handle_state(self.vars)
        if attack_state:
            self.vars.current_state = attack_state
            return

        # 2. 공중 상태 모션 검사 (READY_JUMP가 끝나면 자연스럽게 JUMP_UP 또는 FALL로 이어짐)
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
        # 상태 전환 시 프레임을 0번으로 초기화해주기 위해 이전 프레임의 상태를 기억합니다.
        old_state = self.vars.current_state

        # 키보드 및 마우스 입력 처리
        self.input_handler.update(self.vars)
        
        # 🚀 [트리거] 땅에 있다가 점프 상태(is_jumping)로 진입하는 바로 그 순간 선딜레이 작동
        if self.vars.is_jumping and old_state != "JUMP_UP" and "JUMP" not in old_state and self.vars.vertical_velocity < 0:
            if hasattr(self.vars, 'ready_jump_timer') and self.vars.ready_jump_timer == 0 and old_state != "READY_JUMP":
                self.vars.ready_jump_timer = 5 # 5프레임 동안 player_readyjump.png 유지
        
        # 발판 충돌을 포함한 물리 연산 처리
        if hasattr(self.physics_engine, 'process'):
            self.physics_engine.process(self.vars, platforms)
            
        # ⚔️ 콤보 공격 타이머 및 히트박스 생성 연산 처리
        if hasattr(self.combat_engine, 'process'):
            self.combat_engine.process(self.vars)
            
        # 모든 연산이 끝난 후 최종 애니메이션 상태 판정
        self.update_animation_state()

        # 🎬 [실시간 다중 프레임 애니메이션 스케줄러 엔진]
        if old_state != self.vars.current_state:
            # 상태가 체인지되는 순간 프레임 번호 및 내부 타이머를 정갈하게 0으로 리셋
            self.vars.current_frame_idx = 0
            self.vars.anim_timer = 0
        else:
            # 동일한 움직임 상태를 유지하고 있다면 애니메이션 타이머 누적
            self.vars.anim_timer += 1
            if self.vars.anim_timer >= self.vars.anim_speed:
                self.vars.anim_timer = 0
                
                # 에셋 로더 리스트에서 현재 상태에 대응되는 프레임 갯수 획득
                current_anim_list = self.assets.images.get(self.vars.current_state, [])
                if current_anim_list:
                    # 나머지 연산(%)을 통해 인덱스가 이미지 범위를 벗어나지 않고 1 -> 2 -> 3 무한 루프되도록 제어
                    self.vars.current_frame_idx = (self.vars.current_frame_idx + 1) % len(current_anim_list)

    def draw(self, screen):
        """플레이어 본체 이미지와 공격 시 콤보 이펙트를 화면에 렌더링합니다."""
        # 🎬 1. 캐릭터 본체 스프라이트 시퀀스 추출 및 출력
        anim_list = self.assets.images.get(self.vars.current_state, [])
        if not anim_list:
            return
            
        # 혹시 모를 인덱스 바운드 에러를 막기 위한 최종 안전 필터링
        idx = min(self.vars.current_frame_idx, len(anim_list) - 1)
        player_image = anim_list[idx]
        
        # 왼쪽을 바라보고 있다면 이미지 좌우 반전
        if not self.vars.facing_right:
            player_image = pygame.transform.flip(player_image, True, False)
            
        screen.blit(player_image, (self.vars.x, self.vars.y))
        
        # 2. ⚔️ 공격 애니메이션 중일 때 콤보 검기 이펙트 출력 (원본 로직 완벽 보존)
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