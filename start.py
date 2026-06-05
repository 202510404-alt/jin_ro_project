"""Jjap-Cursor Total Control Launchpad.

[짭커서 통합 기동 사령탑 - 실시간 입출력 파이프 스트림 결합 버전]
서브 프로세스(Watcher, Navigator)의 모든 디버깅 로그와 print 비명을
현재 부모 터미널로 100% 실시간 유도 및 직결하여 숨김없이 자백하게 만듭니다.
"""

import os
import sys
import subprocess
import time
from pathlib import Path

# 🎛️ [절대 규칙 2번] 원터치 디버깅 로그 스위치
DEBUG_MODE = True  # INFO: True로 두시면 워처와 GUI 내부의 모든 로그가 실시간 도배됩니다.

# 🎯 1. 경로 정의 (절대 경로 보장)
ROOT_DIR = Path(__file__).parent.resolve()
CLINE_TOOLS_DIR = ROOT_DIR / "cline_tools"

# 🔍 현재 가동 가능한 최적의 파이썬 인터프리터 자동 추적
def get_best_python():
    # 1순위: 로컬 가상환경(.venv) 내부의 파이썬
    venv_python_win = ROOT_DIR / ".venv" / "Scripts" / "python.exe"
    venv_python_unix = ROOT_DIR / ".venv" / "bin" / "python"
    
    if DEBUG_MODE:
        print(f"🔍 [디버그] 가상환경(윈도우) 경로 점검: {venv_python_win} (존재: {venv_python_win.exists()})")
        print(f"🔍 [디버그] 가상환경(유닉스) 경로 점검: {venv_python_unix} (존재: {venv_python_unix.exists()})")
    
    if venv_python_win.exists():
        return str(venv_python_win)
    elif venv_python_unix.exists():
        return str(venv_python_unix)
    
    if DEBUG_MODE:
        print(f"⚠️ [디버그] 가상환경 미싱 -> 현재 가동 중인 시스템 엔진 우회 배정: {sys.executable}")
    return sys.executable

TARGET_PYTHON = get_best_python()
WATCHER_SCRIPT = CLINE_TOOLS_DIR / "jjap_watcher.py"
NAVIGATOR_SCRIPT = CLINE_TOOLS_DIR / "agent_navigator.py"


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

    # 📡 1단계: 실시간 백그라운드 워처(jjap_watcher.py) 가동 및 출력 사포 인양
    print("➡️ 1단계: 실시간 백그라운드 자동 감시망(Watcher) 투입 중...")
    
    if not WATCHER_SCRIPT.exists():
        print(f"❌ [경로 에러] 워처 스크립트가 지정된 궤도에 존재하지 않습니다: {WATCHER_SCRIPT}")
        return

    # 환경변수에 프로젝트 루트 및 cline_tools 삽입하여 import 크래시 영구 봉쇄
    env = os.environ.copy()
    env["PYTHONPATH"] = os.path.pathsep.join([str(ROOT_DIR), str(CLINE_TOOLS_DIR), env.get("PYTHONPATH", "")])
    # 💡 실시간 무버퍼링 출력 강제화 스위치 탑재 (파이썬 로그가 메모리에 갇히는 현상 원천 차단)
    env["PYTHONUNBUFFERED"] = "1"

    # ⭐ [핵심 수술 부위] stdout과 stderr를 현재 형님이 보고 계신 터미널 화면(sys.stdout/err)으로 다이렉트 바느질!!
    watcher_process = subprocess.Popen(
        [TARGET_PYTHON, str(WATCHER_SCRIPT)],
        cwd=str(ROOT_DIR),
        env=env,
        stdout=sys.stdout if DEBUG_MODE else subprocess.DEVNULL,
        stderr=sys.stderr if DEBUG_MODE else subprocess.DEVNULL,
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if os.name == 'nt' else 0
    )
    
    time.sleep(1.0) # 워처 안착용 시동 대기 타임 보정
    
    # 워처가 시작하자마자 구문 오류나 모듈 로딩 오류로 즉사했는지 체크하는 안전핀
    if watcher_process.poll() is not None:
        print(f"❌ [기동 즉사] 감시망 프로세스가 실행 즉시 사망했습니다. (리턴코드: {watcher_process.poll()})")
        print("💡 상단에 출력된 파이썬 문법/모듈 에러 내역을 추적하십시오.")
        return
    else:
        print("✅ [SUCCESS] 감시망이 백그라운드 메모리에 안착 후 정상 실시간 중계 중입니다.")

    # 🧠 2단계: 에이전트 네비게이터(agent_navigator.py) GUI 창 띄우기
    print("➡️ 2단계: 세맨틱 네비게이터 검색기(GUI) 전면 배치 중...")
    if not NAVIGATOR_SCRIPT.exists():
        print(f"❌ [경로 에러] 네비게이터 GUI 스크립트가 없습니다: {NAVIGATOR_SCRIPT}")
        watcher_process.terminate()
        return
        
    print("💡 [안내] 검색기 창을 닫으면 백그라운드 감시망도 함께 안전하게 종료됩니다.")
    print("----------------------------------------------------------------------")
    
    try:
        # GUI 프로세스도 동일하게 환경변수 및 터미널 출력 완벽 동기화
        subprocess.run(
            [TARGET_PYTHON, str(NAVIGATOR_SCRIPT)],
            cwd=str(ROOT_DIR),
            env=env,
            check=True
        )
    except KeyboardInterrupt:
        print("\n\n🛑 [사용자 중단] 터미널에서 종료 신호를 수신했습니다.")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ [런타임 사고] 검색기(GUI) 내부에서 무단 크래시 예외 발생! 리턴코드: {e.returncode}")
    except Exception as e:
        print(f"\n❌ [런타임 사고] 검색기 실행 중 치명적 시스템 오류 발생: {e}")
    finally:
        # 🧼 3단계: 청소 작전
        print("----------------------------------------------------------------------")
        print("🧼 3단계: 검색기 종료 감지 -> 백그라운드 감시망 자원 회수(종료) 중...")
        try:
            if watcher_process.poll() is None:
                watcher_process.terminate()
                watcher_process.wait(timeout=3)
                print("✅ [CLEANUP] 백그라운드 프로세스가 안전하게 전원 종료되었습니다.")
            else:
                print("ℹ️ [CLEANUP] 백그라운드 감시망 프로세스가 이미 종료되어 있습니다.")
        except Exception as ex:
            if DEBUG_MODE:
                print(f"🔍 [디버그] 자원 정리 중 내부 예외 유출: {ex}")
            watcher_process.kill()
            print("⚡ [FORCE KILL] 프로세스를 강제 종료 처리했습니다.")
            
    print("======================================================================")
    print("🏁 [Jjap-Cursor] 마스터 사령탑 철수 완료. 깔끔하게 정리되었습니다!")
    print("======================================================================")


if __name__ == "__main__":
    main()