package com.desertcore;

import org.bukkit.plugin.java.JavaPlugin;
import org.bukkit.event.Listener;
import com.desertcore.session.GameSessionManager;

import java.io.File;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

public final class DesertCore extends JavaPlugin {
    private GameSessionManager gameSessionManager;

    @Override
    public void onEnable() {
        // 1. 중앙 교통 통제국 우선 가동
        this.gameSessionManager = new GameSessionManager(this);

        // 2. ⚡ [자동화] com.desertcore.legacy 폴더 안의 모든 Listener 파일 자동 등록
        registerAllListenersInPackage("com.desertcore.legacy");

        if (Switch.DEBUG_MODE) {
            getLogger().info("[DEBUG] 패키지 자동 스캔 및 리스너 일괄 등록 프로세스 완료.");
        }
    }

    @Override
    public void onDisable() {
        getLogger().info("DesertCore가 비활성화되었습니다.");
    }

    public GameSessionManager getGameSessionManager() {
        return gameSessionManager;
    }

    /**
     * 지정한 패키지(폴더) 내부의 모든 클래스를 찾아 마인크래프트 이벤트 리스너로 자동 등록하는 브레인 메소드
     */
    private void registerAllListenersInPackage(String packageName) {
        try {
            String path = packageName.replace('.', '/');
            ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
            URL resource = classLoader.getResource(path);
            
            if (resource == null) return;

            // 팩트 교정: String에서 getAbsoluteFile()을 호출하던 결함을 java.io.File 변환으로 정밀 수정
            File directory = new File(resource.toURI());
            if (!directory.exists()) return;

            // 폴더 내부의 모든 파일명을 가져옴
            File[] files = directory.listFiles();
            if (files == null) return;

            for (File file : files) {
                // .class 파일만 검열
                if (file.getName().endsWith(".class")) {
                    String className = packageName + '.' + file.getName().substring(0, file.getName().length() - 6);
                    Class<?> clazz = Class.forName(className);

                    // 해당 클래스가 마인크래프트 Listener 인터페이스를 구현했는지 확인
                    if (Listener.class.isAssignableFrom(clazz) && !clazz.isInterface()) {
                        try {
                            // 생성자에 DesertCore 플러그인을 주입하며 동적으로 인스턴스 생성
                            Listener listener = (Listener) clazz.getConstructor(DesertCore.class).newInstance(this);
                            
                            // 버킷에 최종 자동 등록
                            getServer().getPluginManager().registerEvents(listener, this);
                            
                            if (Switch.DEBUG_MODE) {
                                getLogger().info("[DEBUG] 자동 로드 성공: " + className);
                            }
                        } catch (Exception e) {
                            getLogger().warning("클래스 동적 생성 실패 (생성자 규격 확인 필요): " + className);
                        }
                    }
                }
            }
        } catch (Exception e) {
            getLogger().severe("패키지 스캔 중 치명적 오류 발생: " + e.getMessage());
        }
    }
}