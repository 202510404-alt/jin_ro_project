# 🏗️ AI-OPTIMIZED ULTRA COMPACT CODEBASE MAP (DIRECT SOURCE SCAN)

> **[AI 프로토콜 매뉴얼]** 이 문서는 JSON 장부에 의존하지 않고, 하드디스크의 `main.py` 및 `src/` 내 모든 파이썬 소스코드를 직접 뒤져서 실시간 징집한 100% 무결점 인터페이스 지도입니다.

```markdown
project_root/
│   │   ├── __init__.py
│   │   │   ├── __init__.py
│   │   │   ├── dummy_main.py [🧬 class DummyEnemy | └─ def __init__(self, x, y) -> Any | └─ def load_images(self) -> Any | └─ def check_player_attack(self, player_obj) -> Any | └─ def update(self, player_obj) -> Any | └─ def draw(self, screen) -> Any]
│   │   │   ├── variables.py [🧬 class DummyVariables | └─ def __init__(self, x, y) -> Any]
│   ├── main.py [🎯 def main() -> Any]
│   │   ├── __init__.py
│   │   ├── map_main.py [🧬 class GameMap | └─ def __init__(self, map_id=1) -> Any | └─ def load_map_from_json(self) -> Any | └─ def load_map_assets(self) -> Any | └─ def build_map(self) -> Any | └─ def update(self) -> Any | └─ def draw(self, screen) -> Any]
│   │   ├── map_settings.py
│   │   ├── variables.py [🧬 class MapVariables | └─ def __init__(self, map_id=1, width=DEFAULT_MAP_WIDTH, height=DEFAULT_MAP_HEIGHT) -> Any]
│   │   ├── __init__.py
│   │   ├── platform_main.py [🧬 class Platform | └─ def __init__(self, x, y, width=200, height=30, **kwargs) -> Any | └─ def load_image(self) -> Any | └─ def update(self) -> Any | └─ def draw(self, screen) -> Any]
│   │   ├── platform_settings.py
│   │   ├── variables.py [🧬 class PlatformVariables | └─ def __init__(self, x, y, width=DEFAULT_PLATFORM_WIDTH, height=DEFAULT_PLATFORM_HEIGHT, is_solid=DEFAULT_IS_SOLID, is_visible=DEFAULT_IS_VISIBLE, passable_from_bottom=DEFAULT_PASSABLE_FROM_BOTTOM, platform_type='NORMAL', **kwargs) -> Any]
│   │   ├── __init__.py
│   │   ├── asset_loader.py [🧬 class PlayerAssetLoader | └─ def __init__(self, vars_obj) -> Any | └─ def load_all_assets(self, vars_obj) -> Any | └─ def _load_series(self, directory, file_list, target_w, target_h) -> Any]
│   │   ├── combat_processor.py [🧬 class PlayerCombatProcessor | └─ def process(self, vars_obj) -> Any]
│   │   ├── input_handler.py [🧬 class PlayerInputHandler | └─ def __init__(self) -> Any | └─ def update(self, vars_obj) -> Any | └─ def trigger_attack(self, vars_obj) -> Any]
│   │   │   ├── __init__.py
│   │   │   ├── air_motions.py [🧬 class AirMotions(MotionBase) | └─ def handle_state(self, vars_obj) -> Any]
│   │   │   ├── attack_motions.py [🧬 class AttackMotions(MotionBase) | └─ def handle_state(self, vars_obj) -> Any]
│   │   │   ├── ground_motions.py [🧬 class GroundMotions(MotionBase) | └─ def handle_state(self, vars_obj) -> Any]
│   │   │   ├── motion_base.py [🧬 class MotionBase | └─ def __init__(self) -> Any | └─ def handle_state(self, vars_obj) -> Any]
│   │   ├── physics_processor.py [🧬 class PlayerPhysicsProcessor | └─ def process(self, vars_obj, platforms) -> Any]
│   │   ├── player_main.py [🧬 class Player | └─ def __init__(self, x, y) -> Any | └─ def update_animation_state(self) -> Any | └─ def update(self, platforms) -> Any | └─ def draw(self, screen) -> Any]
│   │   ├── variables.py [🧬 class PlayerVariables | └─ def __init__(self, x, y) -> Any]
│   ├── settings.py
```
