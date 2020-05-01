/root/steamcmd/steamcmd.sh +@ShutdownOnFailedCommand 1 +@NoPromptForPassword 1 +login anonymous +force_install_dir /root/DST +app_update 343050 +quit
/root/DST/bin/dontstarve_dedicated_server_nullrenderer -only_update_server_mods
# 是否开启洞穴,默认不开启洞穴
if [ -n "$1" ] && [ $1 = caves ]; then
    /root/DST/bin/dontstarve_dedicated_server_nullrenderer -shard Master & \
    /root/DST/bin/dontstarve_dedicated_server_nullrenderer -shard Caves
else
    /root/DST/bin/dontstarve_dedicated_server_nullrenderer -shard Master
fi