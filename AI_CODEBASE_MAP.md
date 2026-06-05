# 🏗️ AI-OPTIMIZED ULTRA COMPACT CODEBASE MAP (INTELLIGENT SCAN)

> **[AI 프로토콜 매뉴얼]** 이 문서는 다른 AI 비서들의 경로 오해를 차단하기 위해 파일마다 **실제 하드디스크 상대 경로 `[📂 실제경로]`**를 강제 명시해 둔 특수 지도입니다.
> AI 비서는 절대 눈치로 경로를 추측하지 말고, 파일명 뒤에 박혀있는 `[📂 실제경로]` 규격을 그대로 복사하여 agent_navigator를 호출하십시오.

```markdown
project_root/
├── src/
│   ├── enemy/
│   │   ├── __init__.py [📂 src/enemy/__init__.py]
│   │   ├── dummy/
│   │   │   ├── __init__.py [📂 src/enemy/dummy/__init__.py]
│   │   │   ├── dummy_main.py [📂 src/enemy/dummy/dummy_main.py] -> [💡 📦 imp: pygame, os, sys, enemy.dummy.variables.DummyVariables | 🧬 class DummyEnemy [L7-80] |   └─ def __init__(self, x, y) -> Any [L8-10] |   └─ def load_images(self) -> Any [L12-32] |   └─ def check_player_attack(self, player_obj) -> Any [L34-49] |   └─ def update(self, player_obj) -> Any [L51-60] |   └─ def draw(self, screen) -> Any [L62-80]]
│   │   │   ├── variables.py [📂 src/enemy/dummy/variables.py] -> [💡 📦 imp: settings.GROUND_Y | 🧬 class DummyVariables [L4-23] |   └─ def __init__(self, x, y) -> Any [L5-23]]
│   ├── main.py [📂 src/main.py] -> [💡 📦 imp: pygame, sys, os, settings.SCREEN_WIDTH... / 💾 var: current_dir | 🎯 def main() -> Any [L19-78]]
│   ├── map_system/
│   │   ├── __init__.py [📂 src/map_system/__init__.py]
│   │   ├── map_main.py [📂 src/map_system/map_main.py] -> [💡 📦 imp: pygame, sys, os, json... | 🧬 class GameMap [L9-109] |   └─ def __init__(self, map_id=1) -> Any [L10-21] |   └─ def load_map_from_json(self) -> Any [L23-54] |   └─ def load_map_assets(self) -> Any [L56-69] |   └─ def build_map(self) -> Any [L71-82] |   └─ def update(self) -> Any [L84-87] |   └─ def draw(self, screen) -> Any [L89-109]]
│   │   ├── map_settings.py [📂 src/map_system/map_settings.py] -> [💡 💾 var: DEFAULT_MAP_WIDTH, DEFAULT_MAP_HEIGHT, DEFAULT_BG_WIDTH, DEFAULT_BG_HEIGHT...]
│   │   ├── variables.py [📂 src/map_system/variables.py] -> [💡 📦 imp: math, src.map_system.map_settings.* | 🧬 class MapVariables [L5-32] |   └─ def __init__(self, map_id=1, width=DEFAULT_MAP_WIDTH, height=DEFAULT_MAP_HEIGHT) -> Any [L6-32]]
│   ├── platform_system/
│   │   ├── __init__.py [📂 src/platform_system/__init__.py]
│   │   ├── platform_main.py [📂 src/platform_system/platform_main.py] -> [💡 📦 imp: pygame, sys, os, platform_system.variables.PlatformVariables | 🧬 class Platform [L7-32] |   └─ def __init__(self, x, y, width=200, height=30, **kwargs) -> Any [L8-10] |   └─ def load_image(self) -> Any [L12-24] |   └─ def update(self) -> Any [L26-27] |   └─ def draw(self, screen) -> Any [L29-32]]
│   │   ├── platform_settings.py [📂 src/platform_system/platform_settings.py] -> [💡 💾 var: DEFAULT_PLATFORM_WIDTH, DEFAULT_PLATFORM_HEIGHT, DEFAULT_IS_SOLID, DEFAULT_IS_VISIBLE...]
│   │   ├── variables.py [📂 src/platform_system/variables.py] -> [💡 📦 imp: platform_system.platform_settings.* | 🧬 class PlatformVariables [L4-33] |   └─ def __init__(self, x, y, width=DEFAULT_PLATFORM_WIDTH, height=DEFAULT_PLATFORM_HEIGHT, is_solid=DEFAULT_IS_SOLID, is_visible=DEFAULT_IS_VISIBLE, passable_from_bottom=DEFAULT_PASSABLE_FROM_BOTTOM, platform_type='NORMAL', **kwargs) -> Any [L5-33]]
│   ├── player/
│   │   ├── __init__.py [📂 src/player/__init__.py]
│   │   ├── asset_loader.py [📂 src/player/asset_loader.py] -> [💡 📦 imp: pygame, sys, os | 🧬 class PlayerAssetLoader [L6-70] |   └─ def __init__(self, vars_obj) -> Any [L7-10] |   └─ def load_all_assets(self, vars_obj) -> Any [L12-60] |   └─ def _load_series(self, directory, file_list, target_w, target_h) -> Any [L62-70]]
│   │   ├── combat_processor.py [📂 src/player/combat_processor.py] -> [💡 📦 imp: pygame | 🧬 class PlayerCombatProcessor [L4-31] |   └─ def process(self, vars_obj) -> Any [L5-31]]
│   │   ├── input_handler.py [📂 src/player/input_handler.py] -> [💡 📦 imp: pygame | 🧬 class PlayerInputHandler [L4-66] |   └─ def __init__(self) -> Any [L5-6] |   └─ def update(self, vars_obj) -> Any [L8-48] |   └─ def trigger_attack(self, vars_obj) -> Any [L50-66]]
│   │   ├── motions/
│   │   │   ├── __init__.py [📂 src/player/motions/__init__.py]
│   │   │   ├── air_motions.py [📂 src/player/motions/air_motions.py] -> [💡 📦 imp: src.player.motions.motion_base.MotionBase | 🧬 class AirMotions(MotionBase) [L4-12] |   └─ def handle_state(self, vars_obj) -> Any [L5-12]]
│   │   │   ├── attack_motions.py [📂 src/player/motions/attack_motions.py] -> [💡 📦 imp: src.player.motions.motion_base.MotionBase | 🧬 class AttackMotions(MotionBase) [L4-14] |   └─ def handle_state(self, vars_obj) -> Any [L5-14]]
│   │   │   ├── ground_motions.py [📂 src/player/motions/ground_motions.py] -> [💡 📦 imp: src.player.motions.motion_base.MotionBase | 🧬 class GroundMotions(MotionBase) [L4-13] |   └─ def handle_state(self, vars_obj) -> Any [L5-13]]
│   │   │   ├── motion_base.py [📂 src/player/motions/motion_base.py] -> [🧬 class MotionBase [L2-8] |   └─ def __init__(self) -> Any [L3-4] |   └─ def handle_state(self, vars_obj) -> Any [L6-8]]
│   │   ├── physics_processor.py [📂 src/player/physics_processor.py] -> [💡 📦 imp: pygame, src.settings.SCREEN_WIDTH, src.settings.GROUND_Y | 🧬 class PlayerPhysicsProcessor [L5-39] |   └─ def process(self, vars_obj, platforms) -> Any [L6-39]]
│   │   ├── player_main.py [📂 src/player/player_main.py] -> [💡 📦 imp: pygame, player.variables.PlayerVariables, player.input_handler.PlayerInputHandler, player.asset_loader.PlayerAssetLoader... | 🧬 class Player [L12-124] |   └─ def __init__(self, x, y) -> Any [L13-26] |   └─ def update_animation_state(self) -> Any [L28-51] |   └─ def update(self, platforms) -> Any [L53-92] |   └─ def draw(self, screen) -> Any [L94-124]]
│   │   ├── variables.py [📂 src/player/variables.py] -> [💡 📦 imp: settings.GROUND_Y | 🧬 class PlayerVariables [L4-44] |   └─ def __init__(self, x, y) -> Any [L5-44]]
│   ├── settings.py [📂 src/settings.py] -> [💡 💾 var: SCREEN_WIDTH, SCREEN_HEIGHT, VIRTUAL_WIDTH, VIRTUAL_HEIGHT...]
```
