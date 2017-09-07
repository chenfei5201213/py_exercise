# nmon安装
nmon版本下载
访问网址[nmon](http://nmon.sourceforge.net/pmwiki.php?n=Site.Download),下载`nmon16e_mpginc.tar.gz`

## nmon安装
```shell
wget http://sourceforge.net/projects/nmon/files/nmon16e_mpginc.tar.gz
tar -xvfz nmon16e_mpginc.tar.gz
cd nmon16e_mpginc
# 授权运行权限
chmod +x nmon_x86_64_centos7
# 使nmon在任何地方都能运行
mv nmon_x86_64_centos7 /usr/bin/nmon
```
## 实时监控
运行`nmon` 进入nmon监控界面
![](http://images2017.cnblogs.com/blog/874243/201708/874243-20170823171953293-1625706676.png)
操作快捷键
- 键入“c”查看系统CPU使用情况
![](http://nmon.sourceforge.net/docs/nmon16a_CPU_600.gif)
- 键入“m”查看系统内存使用情况
![](http://nmon.sourceforge.net/docs/nmon16a_Memory.gif)
- 键入“d”查看系统磁盘I/O情况
![](http://nmon.sourceforge.net/docs/nmon16a_Disk_600.gif)
- 键入“h”查看帮助信息
![](http://nmon.sourceforge.net/docs/nmon16a_Help_600.gif)

## 后台监控

为了配合性能测试，我们往往需要将一个时间段内系统资源消耗情况记录下来，这时可以使用命令在远程窗口执行命令：
```shell
./nmon/ nmon_x86_rhel5  -f -N -m /nmon/log  -s 30 -c 120
```
其中各参数表示：
  - -f 按标准格式输出文件：<hostname>_YYYYMMDD_HHMM.nmon
  - -N include NFS sections
  - -m 切换到路径去保存日志文件
  - -s 每隔n秒抽样一次，这里为30
  - -c 取出多少个抽样数量，这里为120，即监控=120*(30/60/60)=1小时

根据小时计算这个数字的公式为：c=h*3600/s，比如要监控10小时，每隔30秒采样一次，则c=10*3600/30=1200

该命令启动后，会在nmon所在目录下生成监控文件，并持续写入资源数据，直至360个监控点收集完成——即监控1小时，这些操作均自动完成，无需手工干 预，测试人员可以继续完成其他操作。如果想停止该监控，需要通过“#ps –ef|grep nmon”查询进程号，然后杀掉该进程以停止监控。

## 定时任务

除配合性能测试的短期监控，我们也可以实现对系统的定期监控，作为运营维护阶段的参考。定期监控实现如下：

1)   执行命令：#`crontab  –e`

2)   在最后一行添加如下命令：
`0 8 * * 1,2,3,4,5  /nmon/nmon_x86_rhel5  -f -N -m /nmon/log  -s 30 -c 1200`
表示：
周一到周五，从早上08点开始，监控10个小时（到18:00整为止），输出到/nmon/log

## 测试指标可视化
> nmon命令 生成的nmon可以通过工具进行可视化展示，一般可以使用nmonchart、nmon_analyser
### nmonchart
> nmonechart 使用Google charts 生成html报告，唯一的缺点是google charts的接口被国内墙了。

参考：[官方网站](http://nmon.sourceforge.net/pmwiki.php?n=Site.Nmonchart)
下载：[nmonchart31.tar](http://sourceforge.net/projects/nmon/files/nmonchart31.tar)
下载`nmonchart31.tar`
```shell
wget http://sourceforge.net/projects/nmon/files/nmonchart31.tar
tar -xvf nmonchart31.tar
chmod u+x nmonchart
mv nmonchart /usr/bin/
```

使用方式
```
nmonchart <nmon-file> <output-file>.html
```
example:
```
nmonchart blue_150508_0800.nmon blue_150508_0800.html
```
![](http://nmon.sourceforge.net/docs/pic16.png)

### nmon_analyser

> nmon_analyser 由IBM提供， 使用excel的宏命令分析加载生成excel图表，展示资源占用
> 值得注意的是，当nmon文件大于10m时，要使用64位的Excel
参考：[官方文档](https://www.ibm.com/developerworks/community/wikis/home?lang=en#!/wiki/Power+Systems/page/nmon_analyser)
下载：[nmon_analyser_v51_2.zip](https://www.ibm.com/developerworks/community/wikis/form/anonymous/api/wiki/61ad9cf2-c6a3-4d2c-b779-61ff0266d32a/page/b7fc61a1-eef9-4756-8028-6e687997f176/attachment/d32a74ae-0ab5-4abc-8e61-567b5f41c5e5/media/nmon_analyser_v51_2.zip)

1. 双击打开 nmon analyser v51_2.xlsm
2. 点击 Analyze nmon data 打开nmon文件
![](http://images2017.cnblogs.com/blog/874243/201708/874243-20170817102311896-1732094185.png)
3. 等待文件分析完成
![](http://images2017.cnblogs.com/blog/874243/201708/874243-20170817102829553-1488708567.png)

4. 保存文件
最后得到的报告如下：
![](http://images2017.cnblogs.com/blog/874243/201708/874243-20170817102532584-1852866837.png)