"""Jjap-Cursor Total Control Launchpad.

[짭커서 통합 기동 사령탑 - 스마트 환경 자동 적응 버전]
가상환경(.venv)이 켜져 있지 않거나 아예 없더라도, 시스템 파이썬을 자동으로 추적하여
필요한 외부 라이브러리(watchdog)를 자동 설치하고 전체 시스템을 원터치로 가동합니다.
"""

import os
import sys
import subprocess
import time
from pathlib import Path

# 🎯 1. 경로 정의 (절대 경로 보장)
ROOT_DIR = Path(__file__).parent.resolve()

# 🔍 현재 가동 가능한 최적의 파이썬 인터프리터 자동 추적
def get_best_python():
    # 1순위: 로컬 가상환경(.venv) 내부의 파이썬
    venv_python_win = ROOT_DIR / ".venv" / "Scripts" / "python.exe"
    venv_python_unix = ROOT_DIR / ".venv" / "bin" / "python"
    
    if venv_python_win.exists():
        return str(venv_python_win)
    elif venv_python_unix.exists():
        return str(venv_python_unix)
    
    # 2순위: 가상환경이 없으면 현재 이 start.py를 실행한 파이썬 엔진 그대로 사용 (전역/현재 환경)
    return sys.executable

TARGET_PYTHON = get_best_python()
WATCHER_SCRIPT = ROOT_DIR / "cline_tools" / "jjap_watcher.py"
NAVIGATOR_SCRIPT = ROOT_DIR / "cline_tools" / "agent_navigator.py"


def auto_install_dependencies():
    """형님이 가상환경을 안 켰을 때를 대비해, watchdog이 없으면 자동으로 설치해주는 안전장치"""
    print("📦 [의존성 검사] 실시간 감시망 필수 라이브러리(watchdog) 상태 점검 중...")
    try:
        # 지정된 파이썬 환경에 watchdog이 깔려있는지 체크
        subprocess.run(
            [TARGET_PYTHON, "-c", "import watchdog"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print("✅ [OK] 'watchdog' 라이브러리가 이미 준비되어 있습니다.")
    except subprocess.CalledProcessError:
        print("💡 [안내] 'watchdog' 라이브러리가 발견되지 않았습니다. 즉시 원격 투입합니다...")
        try:
            subprocess.run(
                [TARGET_PYTHON, "-m", "pip", "install", "watchdog"],
                check=True
            )
            print("✅ [SUCCESS] 'watchdog' 원격 설치 완료!")
        except Exception as e:
            print(f"❌ [에러] 라이브러리 자동 설치 실패: {e}")
            print("💡 해결책: 터미널에 'pip install watchdog'을 직접 입력해 주세요.")


def main():
    print("======================================================================")
    print("🔥 [Jjap-Cursor Launchpad] 짭커서 통합 마스터 사령탑 기동 시작!")
    print(f"📂 프로젝트 루트: {ROOT_DIR}")
    print(f"🤖 매칭된 파이썬 사령관: {TARGET_PYTHON}")
    print("======================================================================")

    # 🛠️ watchdog 자동 검사 및 누락 시 핀포인트 자동 설치
    auto_install_dependencies()
    print("----------------------------------------------------------------------")

    # 📡 1단계: 실시간 백그라운드 워처(jjap_watcher.py) 은밀하게 기동
    print("➡️ 1단계: 실시간 백그라운드 자동 감시망(Watcher) 투입 중...")
    
    watcher_process = subprocess.Popen(
        [TARGET_PYTHON, str(WATCHER_SCRIPT)],
        cwd=str(ROOT_DIR),
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == 'nt' else 0  # 윈도우 안전핀
    )
    
    time.sleep(0.6) # 워처 안착용 시동 대기
    print("✅ [SUCCESS] 감시망이 백그라운드 메모리에 안착했습니다.")

    # 🧠 2단계: 에이전트 네비게이터(agent_navigator.py) GUI 창 띄우기
    print("➡️ 2단계: 세맨틱 네비게이터 검색기(GUI) 전면 배치 중...")
    print("💡 [안내] 검색기 창을 닫으면 백그라운드 감시망도 함께 안전하게 종료됩니다.")
    print("----------------------------------------------------------------------")
    
    try:
        subprocess.run(
            [TARGET_PYTHON, str(NAVIGATOR_SCRIPT)],
            cwd=str(ROOT_DIR),
            check=True
        )
    except KeyboardInterrupt:
        print("\n\n🛑 [사용자 중단] 터미널에서 종료 신호를 수신했습니다.")
    except Exception as e:
        print(f"\n❌ [런타임 사고] 검색기 실행 중 오류 발생: {e}")
    finally:
        # 🧼 3단계: 청소 작전
        print("----------------------------------------------------------------------")
        print("🧼 3단계: 검색기 종료 감지 -> 백그라운드 감시망 자원 회수(종료) 중...")
        try:
            watcher_process.terminate()
            watcher_process.wait(timeout=3)
            print("✅ [CLEANUP] 백그라운드 프로세스가 안전하게 전원 종료되었습니다.")
        except Exception:
            watcher_process.kill()
            print("⚡ [FORCE KILL] 프로세스를 강제 종료 처리했습니다.")
            
    print("======================================================================")
    print("🏁 [Jjap-Cursor] 마스터 사령탑 철수 완료. 깔끔하게 정리되었습니다!")
    print("======================================================================")


if __name__ == "__main__":
    main()