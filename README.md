# FursuitFriday Improved
## 项目简介
本项目可视为一个用于加载哔哩哔哩动态页面的客户端，提供查看、下载并按照 up-时间 的格式自动重命名,按照up名称搜索的功能

鉴于哔哩哔哩的动态只能向下刷新 不能搜索 翻找过于麻烦 便诞生了本项目 算是对官方的一点补充
## 如何使用？
将本项目下载后安装依赖项
```bash
pip install -r requirements.txt
# 如遇报错可尝试使用 pip3 install -r requirements.txt
```
启动程序
```bash
python v2.py
# 报错可尝试python3 v2.py
```
程序的功能集中于文件菜单中,请自行查看

## 目前已知问题
1. GIF可以加载第一帧,但不能播放(Qt目前无法识别哔哩哔哩通过接口提供的缩略图版GIF)
2. 加载缓慢,容易出现未相应(作者不会多线程优化,曾经尝试过QThread,但目前Windows,macOS均不支持从子线程更改UI)
3. Windows下未选中的图片为灰色(Windows设计问题,考虑后续加入透明度参数实现半透明)

## BUG反馈
请通过issue进行反馈。随缘修复。

如有大佬赏析本项目,欢迎私聊 哔哩哔哩@Rk3368
