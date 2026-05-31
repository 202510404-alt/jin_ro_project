# 🚀 Jjap-Cursor Codebase Tools (Roo Code Context Surgeon V2)

형님(AI Agent 및 개발자)의 개발 생산성을 극대화하고, LLM(Gemini/Claude 등)의 토큰 낭비를 0%로 수렴시키기 위해 설계된 **실시간 코드베이스 인덱싱 및 정밀 컨텍스트 추출 시스템**입니다.

이 시스템은 코드 변경 사항을 백그라운드에서 실시간으로 감시하고, 클래스 및 함수의 의존성 관계(Skeleton, Calls, Used By)를 자동으로 정립하며, AI 프롬프트에 불필요한 설명 주석을 검열하여 최적의 영양가 있는 컨텍스트만 보따리에 싸서 전달합니다.

---

## 🛠️ 시스템 요구 사항 (System Requirements)

- **Python 버전**: `Python 3.10` 이상 권장 (최소 3.8 이상 필요)
  - `ast` 모듈 구조 분석 및 최신 타입 힌팅(`dict[str, Any]`, `list[str]`) 문법 준수를 위해 **3.10+** 환경을 강력히 추천합니다.
- **운영체제**: Windows, macOS, Linux 공용

---

## 📦 필수 외부 라이브러리 및 설치 (Dependencies)

대부분의 핵심 모듈(`ast`, `json`, `hashlib`, `pathlib`, `argparse`, `sys`, `re`)은 파이썬 표준 라이브러리(Standard Library)를 사용하여 별도 설치가 필요 없습니다. 단, **실시간 백그라운드 감시망(Watcher)** 및 **데스크톱 내비게이터 GUI** 구동을 위해 아래의 외부 패키지가 필요합니다.

### 1. 주요 외부 패키지 명세
- **`watchdog`**: 하드디스크의 파일 수정([Ctrl + S]) 이벤트를 실시간으로 정밀 포착하기 위한 폴링 오버저버 라이브러리입니다. (`jjap_watcher.py`에서 사용)

> 💡 **참고 (Tkinter)**: `agent_navigator.py`에서 가로채기 UI 구현을 위해 `tkinter`를 사용합니다. Linux 환경에서는 기본적으로 포함되어 있지 않을 수 있으므로, 아래와 같이 운영체제 패키지 관리자로 설치해야 할 수 있습니다.
> - Ubuntu/Debian: `sudo apt-get install python3-tk`
> - macOS/Windows: Python 설치 시 기본 내장됨

### 2. 한 방 설치 명령어
프로젝트 루트 디렉토리에서 가상환경(`.venv`)을 활성화한 후, 아래 명령어를 실행하십시오.

```bash
# pip 최신화 후 의존성 설치
pip install --upgrade pip
pip install watchdog