package com.desertcore.legacy;

import com.desertcore.DesertCore;
import com.desertcore.Switch;
import com.desertcore.session.GameSession;
import net.kyori.adventure.text.Component;
import net.kyori.adventure.text.format.NamedTextColor;
import org.bukkit.Bukkit;
import org.bukkit.GameMode;
import org.bukkit.Location;
import org.bukkit.World;
import org.bukkit.WorldCreator;
import org.bukkit.entity.Player;
import org.bukkit.entity.Villager;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerInteractEntityEvent;

import java.io.File;
import java.io.IOException;
import java.nio.file.*;
import java.nio.file.attribute.BasicFileAttributes;
import java.util.logging.Level;

public class samakportal implements Listener {

    private final DesertCore plugin;

    public samakportal(DesertCore plugin) {
        this.plugin = plugin;
    }

    @EventHandler
    public void onVillagerClick(PlayerInteractEntityEvent event) {
        if (!(event.getRightClicked() instanceof Villager villager)) {
            return;
        }

        if (villager.getScoreboardTags().contains("desert_npc")) {
            event.setCancelled(true);
            Player player = event.getPlayer();

            if (Switch.DEBUG_MODE) {
                plugin.getLogger().info("[DEBUG] " + player.getName() + "이(가) desert_npc 상호작용 감지됨.");
            }

            if (plugin.getGameSessionManager().getSessionByPlayer(player) != null || player.getWorld().getName().startsWith("desert_")) {
                player.sendMessage(Component.text("[!] 이미 전장 월드에 진입했거나 세션이 할당된 상태입니다.").color(NamedTextColor.RED));
                if (Switch.DEBUG_MODE) {
                    plugin.getLogger().warning("[DEBUG] " + player.getName() + " 진입 거부: 이미 세션 존재함 또는 전장 월드에 있음.");
                }
                return;
            }

            player.sendMessage(Component.text("⏳ 새로운 전장(사본)을 생성하고 있습니다. 잠시만 기다려주세요...").color(NamedTextColor.YELLOW));

            String templateName = "desert_template";
            String instanceName = "desert_" + player.getUniqueId().toString().substring(0, 8);

            File serverDir = Bukkit.getWorldContainer();
            File templateDir = new File(serverDir, templateName);
            File instanceDir = new File(serverDir, instanceName);

            if (Switch.DEBUG_MODE) {
                plugin.getLogger().info("[DEBUG] 월드 경로 타겟팅 생성 - Template: " + templateDir.getAbsolutePath() + " | Instance: " + instanceDir.getAbsolutePath());
            }

            if (!templateDir.exists()) {
                player.sendMessage(Component.text("❌ 서버에 '" + templateName + "' 원본 폴더가 없습니다! 관리자에게 문의하세요.").color(NamedTextColor.RED));
                return;
            }

            if (Switch.DEBUG_MODE) {
                plugin.getLogger().info("[DEBUG] 비동기 파일 복사 스케줄러 진입 시도.");
            }

            Bukkit.getScheduler().runTaskAsynchronously(plugin, () -> {
                try {
                    if (instanceDir.exists()) {
                        if (Switch.DEBUG_MODE) plugin.getLogger().info("[DEBUG] 잔재 인스턴스 폴더 발견, 삭제 프로세스 가동.");
                        deleteDirectoryNative(instanceDir.toPath());
                    }

                    if (Switch.DEBUG_MODE) plugin.getLogger().info("[DEBUG] NIO 월드 트리 복사 시작.");
                    copyDirectoryNative(templateDir.toPath(), instanceDir.toPath());
                    if (Switch.DEBUG_MODE) plugin.getLogger().info("[DEBUG] NIO 월드 트리 복사 완료.");

                    File uidFile = new File(instanceDir, "uid.dat");
                    if (uidFile.exists()) {
                        boolean deleted = uidFile.delete();
                        if (Switch.DEBUG_MODE) plugin.getLogger().info("[DEBUG] uid.dat 제거 결과: " + deleted);
                    }

                    Bukkit.getScheduler().runTask(plugin, () -> {
                        if (Switch.DEBUG_MODE) plugin.getLogger().info("[DEBUG] 동기식 메인 스레드 복귀, Bukkit World 인스턴스 로드 시작: " + instanceName);
                        World copiedWorld = Bukkit.createWorld(new WorldCreator(instanceName));
                        if (copiedWorld != null) {
                            
                            if (Switch.DEBUG_MODE) plugin.getLogger().info("[DEBUG] 월드 생성 성공. 세션 매니저에 등록 처리 중.");
                            plugin.getGameSessionManager().createSession(instanceName, player);

                            Location desertLocation = new Location(copiedWorld, 0.0, -43.0, 0.0, 180f, 0f);
                            player.teleport(desertLocation);
                            player.setGameMode(GameMode.SURVIVAL);
                            player.sendMessage(Component.text("[!] 전장(사막 맵)으로 이동했습니다!").color(NamedTextColor.YELLOW));
                            if (Switch.DEBUG_MODE) plugin.getLogger().info("[DEBUG] 유저 전장 텔레포트 및 게임모드 전환 완수.");
                        } else {
                            player.sendMessage(Component.text("❌ 월드 로딩 중 오류가 발생했습니다.").color(NamedTextColor.RED));
                            if (Switch.DEBUG_MODE) plugin.getLogger().severe("[DEBUG] Bukkit.createWorld 가 null을 반환했습니다.");
                        }
                    });

                } catch (IOException e) {
                    player.sendMessage(Component.text("❌ 전장 맵 데이터 복사 중 오류가 발생했습니다.").color(NamedTextColor.RED));
                    plugin.getLogger().log(Level.SEVERE, "전장 복사 중 예외 발생: ", e);
                }
            });
        }
    }

    private void copyDirectoryNative(Path source, Path target) throws IOException {
        Files.walkFileTree(source, new SimpleFileVisitor<>() {
            @Override
            public FileVisitResult preVisitDirectory(Path dir, BasicFileAttributes attrs) throws IOException {
                Path targetDir = target.resolve(source.relativize(dir));
                if (!Files.exists(targetDir)) {
                    Files.createDirectories(targetDir);
                }
                return FileVisitResult.CONTINUE;
            }

            @Override
            public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
                Files.copy(file, target.resolve(source.relativize(file)), StandardCopyOption.REPLACE_EXISTING);
                return FileVisitResult.CONTINUE;
            }
        });
    }

    private void deleteDirectoryNative(Path path) throws IOException {
        Files.walkFileTree(path, new SimpleFileVisitor<>() {
            @Override
            public FileVisitResult visitFile(Path file, BasicFileAttributes attrs) throws IOException {
                Files.delete(file);
                return FileVisitResult.CONTINUE;
            }

            @Override
            public FileVisitResult postVisitDirectory(Path dir, IOException exc) throws IOException {
                Files.delete(dir);
                return FileVisitResult.CONTINUE;
            }
        });
    }
}