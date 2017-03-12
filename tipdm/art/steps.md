## 俱乐部文章存储
---
### 1. 设计模型
文章模型有五个字段:
 - title
 - author
 - link
 - publish_time
 - content
将上面内容写一个art类，然后放在**project/app/models.py**里面。
>某个字段为空用空字符串表示

---
### 2. 数据存储
将原始的文章资料改成markdown形式，用**\n**分割content与其他字段，用**+**分割除了conetnt的其他字段
存储代码（以下代码要在django shell中执行）
```python
from app.models import art
f = open('art/installpython.txt','r')
raw = f.read()
mes,content = raw.split('\n',1)
title,time,author,link = mes.split('+',3)
ar = art(title=title,author=author,link=link,content=content,publishTime=time)
ar.save()
f.close()
```

---
### 3. 数据展示
写渲染模板，读取数据，渲染数据，返回页面
>md数据中需要插入图片，需要图片路径，现在只能以绝对路径保存。。。
