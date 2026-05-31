# player/physics_processor.py
import pygame
from settings import SCREEN_WIDTH, GROUND_Y

class PlayerPhysicsProcessor:
    def process(self, vars_obj, platforms):
        # 중력 적용 및 이동
        vars_obj.vertical_velocity += vars_obj.gravity
        vars_obj.y += vars_obj.vertical_velocity

        player_rect = pygame.Rect(vars_obj.x, vars_obj.y, vars_obj.width, vars_obj.height)
        on_sub_platform = False

        # 플랫폼 충돌 검사
        for platform in platforms:
            if not platform.vars.is_solid:
                continue
            plat_rect = pygame.Rect(platform.vars.x, platform.vars.y, platform.vars.width, platform.vars.height)
            if player_rect.colliderect(plat_rect):
                if vars_obj.vertical_velocity > 0:
                    if (vars_obj.y + vars_obj.height - vars_obj.vertical_velocity) <= platform.vars.y + 10:
                        vars_obj.y = platform.vars.y - vars_obj.height
                        vars_obj.vertical_velocity = 0
                        vars_obj.is_jumping = False
                        on_sub_platform = True
                        break

        # 메인 바닥 착지 검사
        if not on_sub_platform:
            if vars_obj.y + vars_obj.height >= GROUND_Y:
                vars_obj.y = GROUND_Y - vars_obj.height
                vars_obj.vertical_velocity = 0
                vars_obj.is_jumping = False

        # 화면 좌우 밖 이탈 방지
        if vars_obj.x < 0: 
            vars_obj.x = 0
        elif vars_obj.x + vars_obj.width > SCREEN_WIDTH: 
            vars_obj.x = SCREEN_WIDTH - vars_obj.width