# ==========================================================================
# 🎯 AI GLOBAL GUIDELINES: 코드 무결성 및 디버깅 중심 가이드
# [SCAN_MODE] EXTRACTION_TARGET_PROJECT
# ==========================================================================
# 📄 [요청 1] TARGET: extraction_target_project/src/main/java/com/desertcore/lobbycmd.java (1-49라인)
# ----------------------------------------------------------
```python
package com.desertcore;

import net.kyori.adventure.text.Component;
import net.kyori.adventure.text.format.NamedTextColor;
import org.bukkit.Bukkit;
import org.bukkit.GameMode;
import org.bukkit.Location;
import org.bukkit.World;
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.jetbrains.annotations.NotNull;

public class lobbycmd implements CommandExecutor {

    @Override
    public boolean onCommand(@NotNull CommandSender sender, @NotNull Command command, @NotNull String label, @NotNull String[] args) {

        // 1. 명령어를 친 대상이 플레이어인지 확인 (콘솔창 입력 방지)
        if (!(sender instanceof Player)) {
            sender.sendMessage(Component.text("이 명령어는 인게임 플레이어만 사용할 수 있습니다.").color(NamedTextColor.RED));
            return true;
        }

        Player player = (Player) sender;

        // 2. [핵심] 오퍼레이터(OP) 권한이 있는지 체크
        if (!player.isOp()) {
            player.sendMessage(Component.text("❌ 이 명령어를 사용할 권한이 없습니다. (OP 전용)").color(NamedTextColor.RED));
            return true;
        }

        // 3. 로비 월드("world") 정보 가져오기
        World lobbyWorld = Bukkit.getWorld("world");
        if (lobbyWorld != null) {
            // 서바이벌 모드로 안전하게 변경 후 지정된 로비 좌표로 텔레포트
            player.setGameMode(GameMode.SURVIVAL);
            Location lobbyLocation = new Location(lobbyWorld, 0.0, -44.0, 17.0, 180f, 0f);
            player.teleport(lobbyLocation);

            player.sendMessage(Component.text("[!] 관리자 권한으로 로비에 강제 복귀했습니다.").color(NamedTextColor.GREEN));
        } else {
            player.sendMessage(Component.text("❌ 'world' 월드를 찾을 수 없습니다. 월드 이름을 확인해 주세요.").color(NamedTextColor.RED));
        }

        return true;
    }
}
```

# 📄 [요청 2] TARGET: extraction_target_project/src/main/java/com/desertcore/legacy/samakportal.java (1-60라인)
# ----------------------------------------------------------
```python
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
```

# 📄 [요청 3] TARGET: extraction_target_project/src/main/java/com/desertcore/legacy/deathevent.java (35-80라인)
# ----------------------------------------------------------
```python
public class deathevent implements Listener {

    private final DesertCore plugin;
    private final HashSet<UUID> promptActive = new HashSet<>();

    public deathevent(DesertCore plugin) {
        this.plugin = plugin;
    }

    @EventHandler
    public void onPlayerDeath(PlayerDeathEvent event) {
        Player player = event.getEntity();
        String currentWorld = player.getWorld().getName();

        if (currentWorld.startsWith("desert_")) {
            if (Switch.DEBUG_MODE) plugin.getLogger().info("[DEBUG] " + player.getName() + " 전장 내 사망 감지. 인벤토리 보존 활성화.");
            event.setKeepInventory(true);
            event.getDrops().clear();

            Bukkit.getScheduler().runTaskLater(plugin, () -> {
                if (Switch.DEBUG_MODE) plugin.getLogger().info("[DEBUG] " + player.getName() + " 강제 즉시 리스폰 패킷 전송.");
                player.spigot().respawn();
            }, 1L);
        }
    }

    @EventHandler
    public void onPlayerRespawn(PlayerRespawnEvent event) {
        Player player = event.getPlayer();
        String currentWorld = player.getWorld().getName();

        if (currentWorld.startsWith("desert_")) {
            event.setRespawnLocation(player.getLocation());
            if (Switch.DEBUG_MODE) plugin.getLogger().info("[DEBUG] " + player.getName() + " 리스폰 위치 고정.");

            Bukkit.getScheduler().runTaskLater(plugin, () -> {
                player.setGameMode(GameMode.SPECTATOR);
                promptActive.remove(player.getUniqueId());
                
                GameSession session = plugin.getGameSessionManager().getSessionByPlayer(player);
                if (session != null) {
                    if (Switch.DEBUG_MODE) plugin.getLogger().info("[DEBUG] 세션 장부 확인됨. 기존 활성 타이머 초기화 클리어 시도.");
                    session.clearActiveTimer();
                }

                player.sendMessage(Component.text("\n☠️ 전장에서 전사하셨습니다. 관전자 모드로 전환됩니다.").color(NamedTextColor.RED));
```
