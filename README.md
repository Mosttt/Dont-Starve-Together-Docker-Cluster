# Dont-Starve-Together-Docker-Cluster

根据配置文件快速建立饥荒联机版 (DST)Docker 集群

## 更新说明
原始仓库为[Thoxvi/Dont-Starve-Together-Docker-Cluster](https://github.com/Thoxvi/Dont-Starve-Together-Docker-Cluster)，但是原作者不更新了，趁着五一放假改了一波源代码，在原版基础上新增或修改的内容有：
- 使用可读性更好的yaml脚本作为配置文件，并且可以支持在一个配置脚本中修改更多的常用配置(具体支持修改的配置参考user-config.yaml的注释)
- 使用docker的python环境来执行配置生成脚本，现在不需要本地的python环境了
- 现在支持开启或者关闭洞穴，以便于在内存较小的服务器上运行
- 更新代码逻辑，便于进一步更新

## 尚不支持的内容
- 现在还没有支持端口的自定义配置，导致无法在一台主机上开启多个饥荒服务器
- 现在还不支持一些不常见的配置，需要在生产data文件夹后手动修改配置文件
- 现在还不支持洞穴和地面分开配置

## 运行状况

- 镜像大约 `580m`，包括底层 Ubuntu 镜像的话大约 `1G`
- 大概每个实例(带洞穴的)占内存`1G`左右，CPU似乎不怎么占用
- 存档在生成的 `data/名字/Master/save` 里面，要备份的话，请用 `chown` 到自己的用户名，再进行备份
- Mod的话请查看 `./template/dedicated_server_mods_setup.lua` 文件，有具体说明，建议 PC 机先建立一个世界，再把 Mod 配置好，最后再复制到对应位置( `dedicated_server_mods_setup.lua` 文件需要自行整理)

## 运行环境配置

### Python3 环境配置
现在不需要python环境了,直接使用python的docker镜像作为配置脚本的运行环境。  
运行makedata.sh脚本会自动拉取python镜像。

### Docker环境配置

1. 请根据自己的操作系统，在 [Docker 官方网站](https://docs.docker.com/engine/installation/#server)选择适合的 **DockerCE**
2. 如果是 Linux 的话，最好把自己的管理员用户添加到 Docker 用户组里，以免每次打命令都得加入 sudo，命令：`sudo usermod -aG docker $USER`
3. 安装 `docker-compose` :如果你是 Ubuntu ，可以直接使用命令:`sudo apt install docker-compose`，如果不是，请前往 [Docker官方网站](https://docs.docker.com/compose/install/)，并寻找自己的操作系统的安装方式
4. 至此，你应该有了一个正常的 Docker 环境，如果有问题可以根据 END 区的联系方式提交

## 基本使用说明

### 步骤介绍

1. Clone 项目:`git clone --depth=1 https://github.com/LaiQE/Dont-Starve-Together-Docker-Cluster.git`
2. 进入目录:`cd ./Dont-Starve-Together-Docker-Cluster`
3. 根据模板修改 user-config.yaml 文件，提供一个测试 Token (每一行对应一个实例,# 号注释，如果不需要密码的话请留空对应位置)
4. 执行生成脚本:`bash makedata.sh`
5. 转到工作目录:`cd data`
6. 启动容器:`docker-compose up`
7. 若不想查看 Log 的话，可以在`启动容器`步骤使用:`docker-compose up -d`
8. 更新,转到工作目录, `docker-compose stop` , 然后 `docker-compose up -d`

### 一套带走

```shell
git clone https://github.com/LaiQE/Dont-Starve-Together-Docker-Cluster.git
cd ./Dont-Starve-Together-Docker-Cluster
# 修改配置文件 makedata.sh
bash makedata.sh
cd ./data
docker-compose up
```

## 参考资料
https://github.com/Thoxvi/Dont-Starve-Together-Docker-Cluster  
https://blog.csdn.net/szhiy/article/details/79996017  
https://blog.csdn.net/qq_35543890/article/details/81257937
