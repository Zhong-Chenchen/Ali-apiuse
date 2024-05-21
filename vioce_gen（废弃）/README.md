# Ali-apiuse
首先确认请确认已安装Python包管理工具setuptools。如果没有安装，请在终端使用以下命令安装：
```commandline
pip install setuptools
```
### 下载Python SDK
从 [github](https://github.com/aliyun/alibabacloud-nls-python-sdk/releases) 获取Python SDK，或直接下载[alibabacloud-nls-python-sdk-1.0.0.zip](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20221222/efsj/alibabacloud-nls-python-sdk-1.0.0.zip)。
### 安装SDK依赖
进入SDK根目录使用如下命令安装SDK依赖：
```commandline
python -m pip install -r requirements.txt
```
### 安装SDK
依赖安装完成后使用如下命令安装SDK：
```commandline
python -m pip install .
```
### 导入SDK
安装完成后通过以下代码导入SDK：
```commandline
# -*- coding: utf-8 -*-
import nls
```
实在是跑不出来 故废弃