# netdata安装
## 安装环境准备
```shell
yum install autoconf automake curl gcc git libmnl-devel libuuid-devel lm_sensors make MySQL-python nc pkgconfig python python-psycopg2 PyYAML zlib-devel
```

## netdata 安装

```shell
# 下载源码，安装netdata
cd /mnt/tools/
git clone https://github.com/firehol/netdata.git --depth=1
cd netdata

# 使用root用户执行 进行编译、安装和启动
./netdata-installer.sh
```

## 配置服务项
```shell
# 复制netdata启动项到 /etc/init.d
cp system/netdata-init-d /etc/init.d/netdata

# 确保启动项可执行
chmod +x /etc/init.d/netdata
# 注册服务
chkconfig --add netdata
# 设置开机启动
# Centos6
chkconfig netdata on

# Centos7
systemctl enable netdata.service
```
## 服务启动与停止
Centos6
```shell
service netdata start
service netdata stop
```
Centos7
```shell
systemctl start netdata.service
systemctl stop netdata.service
```
## 访问网站
```url
http://ip:19999/
http://127.0.0.1:19999/
```

## 卸载netdata
脚本`netdata-installer.sh` 会在安装时生成`netdata-uninstaller.sh`
执行脚本来卸载
```shell
cd /path/to/netdata.git
./netdata-uninstaller.sh --force
```