# BC_voice_assisstant
## 功能（待更新）

## 配置列表 
- Deitpi os
- Python 3.4
- 百度云语音识别API，京东云垃圾分类识别API
- 依赖包：
  1. sudo apt-get install python-pyaudio python3-pyaudio sox
  2. pip3 install pyaudio
  3. wx_sdk，可从pip网站直接下载，放入jd_api里直接引用
  4. swig3.0.10(+)，版本太低会报缺少编译支持文件
  5. snowboy 项目其他所依赖文件
## 硬件配置（待）
    Orange Pi zero lte. and extention board
## 功能（待）
## 文件
 - audio
   （1）. 欢迎
   （2）. 可回收物
   （3）. 湿垃圾
   （4）. 干垃圾
   （5）. 有害垃圾
   （6）. 无人应答时
   （7）. 无法回答提问
   （8）. 正在查询音
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
## 常见问题解决办法
- Python.h: No such file or directory的错误出现
可执行sudo apt-get install python3-dev

- 新装系统缺少g++，需要安装gcc/g++5.0+ 
- 关键文件：_snowboydetect.so,该文件为交叉编译（C++&&python）自动生成的文件，若报缺失错误，可在snowboy原文档下的swig文档里，从新编译（根据系统编译）
- 播放音频没有声音：声卡设置里默认‘audio lineout' 为 MM （静音），开启即可。
