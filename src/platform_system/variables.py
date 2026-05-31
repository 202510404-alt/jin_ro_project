# src/platform_system/variables.py
from platform_system.platform_settings import * # 🌟 src. 제거하여 경로 인식 해결

class PlatformVariables:
    def __init__(self, x, y, 
                 width=DEFAULT_PLATFORM_WIDTH, 
                 height=DEFAULT_PLATFORM_HEIGHT, 
                 is_solid=DEFAULT_IS_SOLID, 
                 is_visible=DEFAULT_IS_VISIBLE, 
                 passable_from_bottom=DEFAULT_PASSABLE_FROM_BOTTOM, 
                 platform_type="NORMAL",
                 **kwargs): # 🌟 map_main.py에서 던지는 가변 인자들을 안전하게 받아내기 위해 추가
        """
        플랫폼의 속성들을 관리하는 데이터 클래스
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.is_solid = is_solid                     
        
        # 🌟 map_main.py에서 'can_pass_through'라는 이름으로 값이 들어오면 passable_from_bottom에 매핑해 줍니다.
        if "can_pass_through" in kwargs:
            self.passable_from_bottom = kwargs["can_pass_through"]
        else:
            self.passable_from_bottom = passable_from_bottom 
        
        self.is_visible = is_visible                 
        self.platform_type = platform_type           
        
        self.velocity_x = DEFAULT_PLATFORM_SPEED_X
        self.velocity_y = DEFAULT_PLATFORM_SPEED_Y