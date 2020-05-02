#!/usr/bin/python3.6

import os
import yaml
import shutil

service_format = '''
 {name}:
    build: ../dockerfile-update
    ports:
      - "10999/udp"
      - "10998/udp"
    volumes:
      - "./{name}:/root/.klei/DoNotStarveTogether/Cluster_1"
      - "./{name}/dedicated_server_mods_setup.lua:/root/DST/mods/dedicated_server_mods_setup.lua"
    container_name: {name}
    command: "{caves}"
'''

version_format = '''version : "2"
services:'''

cluster_ini = '''[GAMEPLAY]
game_mode = {game_mode}
max_players = {max_players}
pvp = false
pause_when_empty = true
vote_kick_enabled = false


[NETWORK]
lan_only_cluster = false
cluster_intention = cooperative
cluster_description = {introduction}
cluster_name = {room_name}
offline_cluster = false
cluster_password = {passwd}


[MISC]
max_snapshots = 6
console_enabled = true


[SHARD]
shard_enabled = true
bind_ip = 127.0.0.1
master_ip = 127.0.0.1
master_port = 10888
cluster_key = supersecretkey
'''

with open('user-config.yaml', 'r') as f:
    user_config = yaml.load(f)

path = os.path.dirname(os.path.abspath(__file__))
path_data = os.path.join(path, "data")

if os.path.exists(path_data):
    shutil.rmtree(path_data)
os.makedirs(path_data)

docker_compose_yml = version_format
# TODO:没有关于端口号的设置,还不支持同时开启多个服务
for info in user_config:
    room_path = os.path.join(path_data, info['room_name'])
    shutil.copytree(os.path.join(path, 'template'), room_path)
    with open(os.path.join(room_path, "cluster_token.txt"), 'w') as f:
        f.write(info['token'])
    with open(os.path.join(room_path, "adminlist.txt"), 'a') as f:
        for admin in info['adminlist']:
            f.write(admin + '\n')
    with open(os.path.join(room_path, "cluster.ini"), 'w') as f:
        f.write(cluster_ini.format(**info))
    with open(os.path.join(room_path, "dedicated_server_mods_setup.lua"), 'a') as f:
        f.write('\n')
        for mod_id in info['mods']:
            f.write('ServerModSetup("{}")\n'.format(mod_id))

    service_config = service_format.format(name=info['room_name'],
                                           caves='caves' if info['caves'] else 'no-caves')
    docker_compose_yml = docker_compose_yml + service_config


with open(path_data + "/docker-compose.yml", 'w') as f:
    f.write(docker_compose_yml)

print("数据生成完毕！")
print("在data文件夹中执行\033[1;33m docker-compose up -d \033[0m开启服务器")
print("更多设置在data文件中修改配置文件")
print("Enjoying Do-Not-Starve-Together now!!!!!")
