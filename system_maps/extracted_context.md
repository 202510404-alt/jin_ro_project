# ==========================================================================
# 🎯 AI GLOBAL GUIDELINES: 코드 무결성 및 디버깅 중심 가이드
# [SCAN_MODE] SRC
# ==========================================================================
# 📄 [요청 1] TARGET: src/main/java/com/desertcore/DesertCore.java (35-65라인)
# ----------------------------------------------------------
```python
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

            File directory = new File(resource.getFile().getAbsoluteFile().toString().replace("%20", " "));
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
```

# 📄 [요청 2] TARGET: src/main/java/com/desertcore/DesertCoreTester.java (25-55라인)
# ----------------------------------------------------------
```python
        System.out.println("[STEP 2] 'com.desertcore.legacy' 패키지 자동 탐색 시작");
        String targetPackage = "com.desertcore.legacy";
        
        try {
            String path = targetPackage.replace('.', '/');
            ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
            URL resource = classLoader.getResource(path);

            if (resource == null) {
                System.err.println("❌ 에러: 지정된 패키지 경로를 찾을 수 없습니다: " + path);
                return;
            }

            File directory = new File(resource.getFile().getAbsoluteFile().toString().replace("%20", " "));
            if (!directory.exists()) {
                System.err.println("❌ 에러: 디렉토리가 존재하지 않습니다: " + directory.getPath());
                return;
            }

            File[] files = directory.listFiles();
            if (files == null || files.length == 0) {
                System.out.println("⚠ 스캔 결과: 폴더 내에 자바 클래스 파일이 존재하지 않습니다.");
                return;
            }

            int loadCount = 0;
            for (File file : files) {
                if (file.getName().endsWith(".class")) {
                    String className = targetPackage + '.' + file.getName().substring(0, file.getName().length() - 6);
                    Class<?> clazz = Class.forName(className);
```
