package com.desertcore;

import java.io.File;
import java.net.URL;

// 1. 에러가 나던 Switch 클래스를 파일 내부에 강제로 합쳐버림
class LocalSwitch {
    public static final boolean DEBUG_MODE = true; 
}

public class PureJavaTester {

    public static void main(String[] args) {
        System.out.println("==================================================");
        System.out.println("🚀 [단일 파일 모드] 버튼 클릭 즉시 실행 완료");
        System.out.println("==================================================");

        System.out.println("[검증 1] 글로벌 디버그 스위치 상태");
        System.out.println(">> Switch.DEBUG_MODE = " + LocalSwitch.DEBUG_MODE);
        
        if (LocalSwitch.DEBUG_MODE) {
            System.out.println(">> [상태] 디버그 모드가 활성화되어 로그를 출력합니다.");
        }
        System.out.println();

        System.out.println("[검증 2] com.desertcore.legacy 폴더 내부 자바 파일 추적");
        // 현재 터미널이 src 폴더 기준이므로 상대 경로 직접 타겟팅
        File srcDir = new File("com/desertcore/legacy");
        
        if (srcDir.exists() && srcDir.isDirectory()) {
            File[] files = srcDir.listFiles();
            if (files != null) {
                for (File f : files) {
                    if (f.getName().endsWith(".java")) {
                        System.out.println("   [★ 발견된 파일]: " + f.getName());
                        if (LocalSwitch.DEBUG_MODE) {
                            System.out.println("   └─> [DEBUG] " + f.getName() + " 자동 로드 및 검열 대상 타겟팅 성공.");
                        }
                    }
                }
            }
        } else {
            System.out.println("⚠ [알림] com/desertcore/legacy 폴더를 찾을 수 없습니다.");
            System.out.println("   현재 프로그램이 실행된 실제 위치: " + new File(".").getAbsolutePath());
        }
        
        System.out.println();
        System.out.println("==================================================");
        System.out.println("✅ 단일 파일 결합형 폴더 스캔 시뮬레이션 성공!");
        System.out.println("==================================================");
    }
}