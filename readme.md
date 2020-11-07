### 通信主机1的配置：
* win10
* python 3.6
* 通信ip：在cmd运行ipconfig后 无线局域网WLAN处的IPv4

### 通信主机2的配置：
* win10
* python 3.8
* 通信ip：在cmd运行ipconfig后 无线局域网WLAN处的IPv4

### 实现效果：主机1、2基于UDP的聊天
* 主机1、2均为双工，运行开始时双方均开启发送和接收两个线程
* 主机1发消息结束[主机1发送消息的线程结束]，主机2不再接收[主机2的接收线程结束]；
此时主机1还可以接收2的消息；
此时若主机2发消息结束[主机2发送线程结束]，主机1不再接收[主机1接收线程结束]；
socket结束


### 效果图
分别从两台主机的运行窗口处截图[两台主机时间上差个2秒，主机2快2秒。所以收发消息基本时间一致]
![主机1](https://upload-images.jianshu.io/upload_images/13975801-a005459c930f4902.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![主机2](https://upload-images.jianshu.io/upload_images/13975801-b5135199fa34ffbd.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

PS：已同步至个人简书主页：https://www.jianshu.com/p/e1e7d0441376