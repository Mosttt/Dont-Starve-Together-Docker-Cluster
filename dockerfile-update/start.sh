#!/bin/bash
/root/steamcmd/steamcmd.sh +@ShutdownOnFailedCommand 1 +@NoPromptForPassword 1 +login anonymous +force_install_dir /root/DST +app_update 343050 +quit
/root/DST/bin/dontstarve_dedicated_server_nullrenderer -only_update_server_mods
echo -e "\033[31m 游戏启动中 \033[0m" 
# 是否开启洞穴,默认不开启洞穴
if [ -n "$1" ] && [ $1 = caves ]; then
    echo -e "\033[33m 开启洞穴 \033[0m"
    /root/DST/bin/dontstarve_dedicated_server_nullrenderer -shard Master & \
    /root/DST/bin/dontstarve_dedicated_server_nullrenderer -shard Caves
else
    echo -e "\033[33m 不开启洞穴 \033[0m"
    /root/DST/bin/dontstarve_dedicated_server_nullrenderer -shard Master
fi