# BC_voice_assisstant
## API
- Snowboy(语音唤醒)
- 百度语音识别 ASR
- jd云垃圾分类（需要配合wx_sdk）

## 配置列表 
- 系统ubuntu 14.04.06，可从163镜像下载
- Python 2.7.3
- 依赖包：
  1. sudo apt-get install python-pyaudio python3-pyaudio sox
  2. pip install pyaudio
  3. wx_sdk，可从pip网站直接下载，放入jd_api里直接引用
  4. 版本需要较新的，原则上是swig3.0.10(+)，版本太低会报缺少编译支持文件
## 硬件配置（待）
## 功能（待）
## API内核主要改动
为适应本项目，对Snowboy python内核做出了一些改动。
 - 改动动机：
   1. 热词检测到之后，录音窗口的算法无法适用于实际项目：静默录音太长时，超出阀值后自动产生的无效录音。
   2. 原阀值不可变，当人声在临近超时阀值时被检测到，会出现人未讲完话，录音结束
   3. 未检测到人声时，原机制也保存录音，效率底下
 - 改动前：    
   1. 热词检测后，静默时长 与 录音最大时常同时计时。逻辑❌
   2. 无人声的录音也会调用API进行识别。逻辑❌
   3. 人在录音窗口末期讲话，部分可能人声丢失。Bug❌
   4. 无人声的声音frame也存储。逻辑❌
 - 改动后：
   1. 静默时长 从 人声检测到后开始计时
   2. 声音从探测到人声时，开始录音。
## 常见问题
- Python.h: No such file or directory的错误出现
可执行sudo apt-get install python-dev

- 新装系统缺少g++，需要安装gcc/g++5.0+ 
