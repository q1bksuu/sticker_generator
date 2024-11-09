# sticker_generator

## 简介

一个表情包生成器的服务器。服务器使用于Django，图片处理使用Pillow。

时不时找适合套模板的表情包，加以魔改，封装成接口以供灵活生成。通常都是注入一些文字之类。

代码架构简单（至少现在是的），部署方便，有手就行。

本项目偏娱乐，一时兴起，现学现卖。

抽象也好，具象也罢，开心就好。

......

不知道写啥了，先这样吧。

## 如何搭建？

先git克隆本项目并进入
```shell
git clone https://github.com/q1bksuu/sticker_generator.git
cd sticker_generator
```

### 本地环境
1. 安装[Python](https://www.python.org/downloads/)(>3.9)
2. (推荐) 在项目构建venv环境
3. (可选) 升级pip ```python -m pip install --upgrade pip```
4. 安装依赖 ```python -m pip install -r requirements.txt```
5. 启动。以监听本地8000端口为例：```python manage.py runserver 127.0.0.1:8000```
6. 这个时候已经可以开玩了，Enjoy！

### Docker
保证本机已经有完整的docker环境，项目也提供了Dockerfile和docker-compose.yml，直接构建即可。（PS：这里没有docker教程）

### 接口文档
[api.md](api.md)
