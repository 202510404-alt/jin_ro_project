# 🏗️ 짭커서 프로젝트 CODEBASE MAP

현재 인덱싱된 총 파일 수: **30개**

## 🗂️ [Module Index]
- `src/enemy/__init__.py`
- `src/enemy/enemy_base/__init__.py`
- `src/enemy/enemy_base/base_enemy.py`
- `src/enemy/enemy_base/base_vars.py`
- `src/enemy/enemys/__init__.py`
- `src/enemy/enemys/dummy/__init__.py`
- `src/enemy/enemys/dummy/dummy_main.py`
- `src/enemy/enemys/dummy/variables.py`
- `src/main.py`
- `src/map_system/__init__.py`
- `src/map_system/map_main.py`
- `src/map_system/map_settings.py`
- `src/map_system/variables.py`
- `src/platform_system/__init__.py`
- `src/platform_system/platform_main.py`
- `src/platform_system/platform_settings.py`
- `src/platform_system/variables.py`
- `src/player/__init__.py`
- `src/player/asset_loader.py`
- `src/player/combat_processor.py`
- `src/player/input_handler.py`
- `src/player/motions/__init__.py`
- `src/player/motions/air_motions.py`
- `src/player/motions/attack_motions.py`
- `src/player/motions/ground_motions.py`
- `src/player/motions/motion_base.py`
- `src/player/physics_processor.py`
- `src/player/player_main.py`
- `src/player/variables.py`
- `src/settings.py`

## 💀 [Skeleton & Dependency 명세서]
### 📄 src/enemy/__init__.py
*선언된 클래스나 함수가 없는 파일이거나 모듈입니다.*

--------------------------------------------------

### 📄 src/enemy/enemy_base/__init__.py
*선언된 클래스나 함수가 없는 파일이거나 모듈입니다.*

--------------------------------------------------

### 📄 src/enemy/enemy_base/base_enemy.py
*선언된 클래스나 함수가 없는 파일이거나 모듈입니다.*

--------------------------------------------------

### 📄 src/enemy/enemy_base/base_vars.py
*선언된 클래스나 함수가 없는 파일이거나 모듈입니다.*

--------------------------------------------------

### 📄 src/enemy/enemys/__init__.py
*선언된 클래스나 함수가 없는 파일이거나 모듈입니다.*

--------------------------------------------------

### 📄 src/enemy/enemys/dummy/__init__.py
*선언된 클래스나 함수가 없는 파일이거나 모듈입니다.*

--------------------------------------------------

### 📄 src/enemy/enemys/dummy/dummy_main.py
#### 🔍 내부 심볼 및 의존성 관계:
- **[CLASS]** `DummyEnemy` (Line: 7~80)
  - 🎯 *Used By (나를 부르는 곳)*: `src/main.py::main`
- **[METHOD]** `DummyEnemy.__init__` (Line: 8~10)
  - 🔗 *Calls (호출하는 것)*: `DummyVariables, load_images`
- **[METHOD]** `DummyEnemy.load_images` (Line: 12~32)
  - 🔗 *Calls (호출하는 것)*: `abspath, convert_alpha, dirname, exit, join, load, print, quit, scale`
  - 🎯 *Used By (나를 부르는 곳)*: `src/enemy/enemys/dummy/dummy_main.py::DummyEnemy.__init__`
- **[METHOD]** `DummyEnemy.check_player_attack` (Line: 34~49)
  - 🔗 *Calls (호출하는 것)*: `Rect, colliderect, print`
  - 🎯 *Used By (나를 부르는 곳)*: `src/enemy/enemys/dummy/dummy_main.py::DummyEnemy.update`
- **[METHOD]** `DummyEnemy.update` (Line: 51~60)
  - 🔗 *Calls (호출하는 것)*: `check_player_attack`
  - 🎯 *Used By (나를 부르는 곳)*: `src/main.py::main, src/map_system/map_main.py::GameMap.update, src/player/player_main.py::Player.update`
- **[METHOD]** `DummyEnemy.draw` (Line: 62~80)
  - 🔗 *Calls (호출하는 것)*: `blit, int, max, rect`
  - 🎯 *Used By (나를 부르는 곳)*: `src/main.py::main, src/map_system/map_main.py::GameMap.draw`

#### 🧱 Code Skeleton:
```python
class DummyEnemy:
    def __init__(...):
        ...
    def load_images(...):
        ...
    def check_player_attack(...):
        ...
    def update(...):
        ...
    def draw(...):
        ...
```

--------------------------------------------------

### 📄 src/enemy/enemys/dummy/variables.py
#### 🔍 내부 심볼 및 의존성 관계:
- **[CLASS]** `DummyVariables` (Line: 4~23)
  - 🎯 *Used By (나를 부르는 곳)*: `src/enemy/enemys/dummy/dummy_main.py::DummyEnemy.__init__`
- **[METHOD]** `DummyVariables.__init__` (Line: 5~23)

#### 🧱 Code Skeleton:
```python
class DummyVariables:
    def __init__(...):
        ...
```

--------------------------------------------------

### 📄 src/main.py
#### 🔍 내부 심볼 및 의존성 관계:
- **[FUNCTION]** `main` (Line: 19~78)
  - 🔗 *Calls (호출하는 것)*: `Clock, DummyEnemy, GameMap, Player, Surface, blit, draw, exit, fill, flip, get, init, quit, set_caption, set_mode, smoothscale, tick, update`

#### 🧱 Code Skeleton:
```python
def main(...):
    ...
```

--------------------------------------------------

### 📄 src/map_system/__init__.py
*선언된 클래스나 함수가 없는 파일이거나 모듈입니다.*

--------------------------------------------------

### 📄 src/map_system/map_main.py
#### 🔍 내부 심볼 및 의존성 관계:
- **[CLASS]** `GameMap` (Line: 9~109)
  - 🎯 *Used By (나를 부르는 곳)*: `src/main.py::main`
- **[METHOD]** `GameMap.__init__` (Line: 10~21)
  - 🔗 *Calls (호출하는 것)*: `build_map, load_map_assets, load_map_from_json`
- **[METHOD]** `GameMap.load_map_from_json` (Line: 23~54)
  - 🔗 *Calls (호출하는 것)*: `MapVariables, abspath, dirname, exit, join, load, open, print, quit`
  - 🎯 *Used By (나를 부르는 곳)*: `src/map_system/map_main.py::GameMap.__init__`
- **[METHOD]** `GameMap.load_map_assets` (Line: 56~69)
  - 🔗 *Calls (호출하는 것)*: `abspath, convert_alpha, dirname, exit, join, load, print, quit`
  - 🎯 *Used By (나를 부르는 곳)*: `src/map_system/map_main.py::GameMap.__init__`
- **[METHOD]** `GameMap.build_map` (Line: 71~82)
  - 🔗 *Calls (호출하는 것)*: `Platform, append, get`
  - 🎯 *Used By (나를 부르는 곳)*: `src/map_system/map_main.py::GameMap.__init__`
- **[METHOD]** `GameMap.update` (Line: 84~87)
  - 🔗 *Calls (호출하는 것)*: `update`
  - 🎯 *Used By (나를 부르는 곳)*: `src/main.py::main, src/player/player_main.py::Player.update`
- **[METHOD]** `GameMap.draw` (Line: 89~109)
  - 🔗 *Calls (호출하는 것)*: `blit, draw, get_height, get_width, range, scale`
  - 🎯 *Used By (나를 부르는 곳)*: `src/main.py::main`

#### 🧱 Code Skeleton:
```python
class GameMap:
    def __init__(...):
        ...
    def load_map_from_json(...):
        ...
    def load_map_assets(...):
        ...
    def build_map(...):
        ...
    def update(...):
        ...
    def draw(...):
        ...
```

--------------------------------------------------

### 📄 src/map_system/map_settings.py
*선언된 클래스나 함수가 없는 파일이거나 모듈입니다.*

--------------------------------------------------

### 📄 src/map_system/variables.py
#### 🔍 내부 심볼 및 의존성 관계:
- **[CLASS]** `MapVariables` (Line: 5~32)
  - 🎯 *Used By (나를 부르는 곳)*: `src/map_system/map_main.py::GameMap.load_map_from_json`
- **[METHOD]** `MapVariables.__init__` (Line: 6~32)
  - 🔗 *Calls (호출하는 것)*: `ceil`

#### 🧱 Code Skeleton:
```python
class MapVariables:
    def __init__(...):
        ...
```

--------------------------------------------------

### 📄 src/platform_system/__init__.py
*선언된 클래스나 함수가 없는 파일이거나 모듈입니다.*

--------------------------------------------------

### 📄 src/platform_system/platform_main.py
#### 🔍 내부 심볼 및 의존성 관계:
- **[CLASS]** `Platform` (Line: 7~32)
  - 🎯 *Used By (나를 부르는 곳)*: `src/map_system/map_main.py::GameMap.build_map`
- **[METHOD]** `Platform.__init__` (Line: 8~10)
  - 🔗 *Calls (호출하는 것)*: `PlatformVariables, load_image`
- **[METHOD]** `Platform.load_image` (Line: 12~24)
  - 🔗 *Calls (호출하는 것)*: `abspath, convert_alpha, dirname, exit, join, load, print, quit, scale`
  - 🎯 *Used By (나를 부르는 곳)*: `src/platform_system/platform_main.py::Platform.__init__`
- **[METHOD]** `Platform.update` (Line: 26~27)
  - 🎯 *Used By (나를 부르는 곳)*: `src/main.py::main, src/map_system/map_main.py::GameMap.update, src/player/player_main.py::Player.update`
- **[METHOD]** `Platform.draw` (Line: 29~32)
  - 🔗 *Calls (호출하는 것)*: `blit`
  - 🎯 *Used By (나를 부르는 곳)*: `src/main.py::main, src/map_system/map_main.py::GameMap.draw`

#### 🧱 Code Skeleton:
```python
class Platform:
    def __init__(...):
        ...
    def load_image(...):
        ...
    def update(...):
        ...
    def draw(...):
        ...
```

--------------------------------------------------

### 📄 src/platform_system/platform_settings.py
*선언된 클래스나 함수가 없는 파일이거나 모듈입니다.*

--------------------------------------------------

### 📄 src/platform_system/variables.py
#### 🔍 내부 심볼 및 의존성 관계:
- **[CLASS]** `PlatformVariables` (Line: 4~33)
  - 🎯 *Used By (나를 부르는 곳)*: `src/platform_system/platform_main.py::Platform.__init__`
- **[METHOD]** `PlatformVariables.__init__` (Line: 5~33)

#### 🧱 Code Skeleton:
```python
class PlatformVariables:
    def __init__(...):
        ...
```

--------------------------------------------------

### 📄 src/player/__init__.py
*선언된 클래스나 함수가 없는 파일이거나 모듈입니다.*

--------------------------------------------------

### 📄 src/player/asset_loader.py
#### 🔍 내부 심볼 및 의존성 관계:
- **[CLASS]** `PlayerAssetLoader` (Line: 6~70)
  - 🎯 *Used By (나를 부르는 곳)*: `src/player/player_main.py::Player.__init__`
- **[METHOD]** `PlayerAssetLoader.__init__` (Line: 7~10)
  - 🔗 *Calls (호출하는 것)*: `load_all_assets`
- **[METHOD]** `PlayerAssetLoader.load_all_assets` (Line: 12~60)
  - 🔗 *Calls (호출하는 것)*: `_load_series, abspath, convert_alpha, dirname, exit, join, load, print, quit, scale`
  - 🎯 *Used By (나를 부르는 곳)*: `src/player/asset_loader.py::PlayerAssetLoader.__init__`
- **[METHOD]** `PlayerAssetLoader._load_series` (Line: 62~70)
  - 🔗 *Calls (호출하는 것)*: `append, convert_alpha, join, load, scale`
  - 🎯 *Used By (나를 부르는 곳)*: `src/player/asset_loader.py::PlayerAssetLoader.load_all_assets`

#### 🧱 Code Skeleton:
```python
class PlayerAssetLoader:
    def __init__(...):
        ...
    def load_all_assets(...):
        ...
    def _load_series(...):
        ...
```

--------------------------------------------------

### 📄 src/player/combat_processor.py
#### 🔍 내부 심볼 및 의존성 관계:
- **[CLASS]** `PlayerCombatProcessor` (Line: 4~31)
  - 🎯 *Used By (나를 부르는 곳)*: `src/player/player_main.py::Player.__init__`
- **[METHOD]** `PlayerCombatProcessor.process` (Line: 5~31)
  - 🔗 *Calls (호출하는 것)*: `Rect`
  - 🎯 *Used By (나를 부르는 곳)*: `src/player/player_main.py::Player.update`

#### 🧱 Code Skeleton:
```python
class PlayerCombatProcessor:
    def process(...):
        ...
```

--------------------------------------------------

### 📄 src/player/input_handler.py
#### 🔍 내부 심볼 및 의존성 관계:
- **[CLASS]** `PlayerInputHandler` (Line: 4~66)
  - 🎯 *Used By (나를 부르는 곳)*: `src/player/player_main.py::Player.__init__`
- **[METHOD]** `PlayerInputHandler.__init__` (Line: 5~6)
- **[METHOD]** `PlayerInputHandler.update` (Line: 8~48)
  - 🔗 *Calls (호출하는 것)*: `get_pressed, trigger_attack`
  - 🎯 *Used By (나를 부르는 곳)*: `src/main.py::main, src/map_system/map_main.py::GameMap.update, src/player/player_main.py::Player.update`
- **[METHOD]** `PlayerInputHandler.trigger_attack` (Line: 50~66)
  - 🎯 *Used By (나를 부르는 곳)*: `src/player/input_handler.py::PlayerInputHandler.update`

#### 🧱 Code Skeleton:
```python
class PlayerInputHandler:
    def __init__(...):
        ...
    def update(...):
        ...
    def trigger_attack(...):
        ...
```

--------------------------------------------------

### 📄 src/player/motions/__init__.py
*선언된 클래스나 함수가 없는 파일이거나 모듈입니다.*

--------------------------------------------------

### 📄 src/player/motions/air_motions.py
#### 🔍 내부 심볼 및 의존성 관계:
- **[CLASS]** `AirMotions` (Line: 4~12)
  - 🎯 *Used By (나를 부르는 곳)*: `src/player/player_main.py::Player.__init__`
- **[METHOD]** `AirMotions.handle_state` (Line: 5~12)
  - 🎯 *Used By (나를 부르는 곳)*: `src/player/player_main.py::Player.update_animation_state`

#### 🧱 Code Skeleton:
```python
class AirMotions:
    def handle_state(...):
        ...
```

--------------------------------------------------

### 📄 src/player/motions/attack_motions.py
#### 🔍 내부 심볼 및 의존성 관계:
- **[CLASS]** `AttackMotions` (Line: 4~14)
  - 🎯 *Used By (나를 부르는 곳)*: `src/player/player_main.py::Player.__init__`
- **[METHOD]** `AttackMotions.handle_state` (Line: 5~14)
  - 🎯 *Used By (나를 부르는 곳)*: `src/player/player_main.py::Player.update_animation_state`

#### 🧱 Code Skeleton:
```python
class AttackMotions:
    def handle_state(...):
        ...
```

--------------------------------------------------

### 📄 src/player/motions/ground_motions.py
#### 🔍 내부 심볼 및 의존성 관계:
- **[CLASS]** `GroundMotions` (Line: 4~13)
  - 🎯 *Used By (나를 부르는 곳)*: `src/player/player_main.py::Player.__init__`
- **[METHOD]** `GroundMotions.handle_state` (Line: 5~13)
  - 🎯 *Used By (나를 부르는 곳)*: `src/player/player_main.py::Player.update_animation_state`

#### 🧱 Code Skeleton:
```python
class GroundMotions:
    def handle_state(...):
        ...
```

--------------------------------------------------

### 📄 src/player/motions/motion_base.py
#### 🔍 내부 심볼 및 의존성 관계:
- **[CLASS]** `MotionBase` (Line: 2~8)
- **[METHOD]** `MotionBase.__init__` (Line: 3~4)
- **[METHOD]** `MotionBase.handle_state` (Line: 6~8)
  - 🎯 *Used By (나를 부르는 곳)*: `src/player/player_main.py::Player.update_animation_state`

#### 🧱 Code Skeleton:
```python
class MotionBase:
    def __init__(...):
        ...
    def handle_state(...):
        ...
```

--------------------------------------------------

### 📄 src/player/physics_processor.py
#### 🔍 내부 심볼 및 의존성 관계:
- **[CLASS]** `PlayerPhysicsProcessor` (Line: 5~39)
  - 🎯 *Used By (나를 부르는 곳)*: `src/player/player_main.py::Player.__init__`
- **[METHOD]** `PlayerPhysicsProcessor.process` (Line: 6~39)
  - 🔗 *Calls (호출하는 것)*: `Rect, colliderect`
  - 🎯 *Used By (나를 부르는 곳)*: `src/player/player_main.py::Player.update`

#### 🧱 Code Skeleton:
```python
class PlayerPhysicsProcessor:
    def process(...):
        ...
```

--------------------------------------------------

### 📄 src/player/player_main.py
#### 🔍 내부 심볼 및 의존성 관계:
- **[CLASS]** `Player` (Line: 12~124)
  - 🎯 *Used By (나를 부르는 곳)*: `src/main.py::main`
- **[METHOD]** `Player.__init__` (Line: 13~26)
  - 🔗 *Calls (호출하는 것)*: `AirMotions, AttackMotions, GroundMotions, PlayerAssetLoader, PlayerCombatProcessor, PlayerInputHandler, PlayerPhysicsProcessor, PlayerVariables`
- **[METHOD]** `Player.update_animation_state` (Line: 28~51)
  - 🔗 *Calls (호출하는 것)*: `handle_state, hasattr`
  - 🎯 *Used By (나를 부르는 곳)*: `src/player/player_main.py::Player.update`
- **[METHOD]** `Player.update` (Line: 53~92)
  - 🔗 *Calls (호출하는 것)*: `get, hasattr, len, process, update, update_animation_state`
  - 🎯 *Used By (나를 부르는 곳)*: `src/main.py::main, src/map_system/map_main.py::GameMap.update`
- **[METHOD]** `Player.draw` (Line: 94~124)
  - 🔗 *Calls (호출하는 것)*: `blit, flip, get, len, min`
  - 🎯 *Used By (나를 부르는 곳)*: `src/main.py::main, src/map_system/map_main.py::GameMap.draw`

#### 🧱 Code Skeleton:
```python
class Player:
    def __init__(...):
        ...
    def update_animation_state(...):
        ...
    def update(...):
        ...
    def draw(...):
        ...
```

--------------------------------------------------

### 📄 src/player/variables.py
#### 🔍 내부 심볼 및 의존성 관계:
- **[CLASS]** `PlayerVariables` (Line: 4~44)
  - 🎯 *Used By (나를 부르는 곳)*: `src/player/player_main.py::Player.__init__`
- **[METHOD]** `PlayerVariables.__init__` (Line: 5~44)

#### 🧱 Code Skeleton:
```python
class PlayerVariables:
    def __init__(...):
        ...
```

--------------------------------------------------

### 📄 src/settings.py
*선언된 클래스나 함수가 없는 파일이거나 모듈입니다.*

--------------------------------------------------

