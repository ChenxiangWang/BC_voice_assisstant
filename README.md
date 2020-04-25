# BC_voice_assisstant

## 配置列表 (主要参照snowboy开发文档)
- 系统ubuntu 14.04.06，可从163镜像下载
- 依赖包：
  1. sudo apt-get install python-pyaudio python3-pyaudio sox
  2. pip install pyaudio
- 官网下载 swig3.0.10(+)

## 问题解决
- Python.h: No such file or directory的错误出现
可执行sudo apt-get install python-dev

- 新装系统缺少g++，需要安装gcc/g++5.0+ 
