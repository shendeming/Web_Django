### 项目：Web_Django

#### 1 介绍

使用Python语言，基于Django2.2+MySQL5.7搭建Web点餐项目。

#### 2 项目运行环境

- 编程语言：Python 3.8.0
- 运行框架：Django 2.2.27
- 数据库：MySQL 5.7.26
- 数据连接驱动：Mysqlclient 
- python扩展库：Pillow

#### 3 项目目录

```
|--myadmin/ 后台管理应用
|    |-- __init__.py
|    |--views/
|    |    |--index.py 后台首页、登录、退出、验证码加载等视图方法
|    |    |--user.py 员工信息管理视图
|    |    |--member.py 会员信息管理视图
|    |    |--shop.py 店铺信息管理视图
|    |    |--product.py 菜品信息管理视图
|    |    |--orders.py 订单信息管理视图
|    |    |--.....
|    |
|    |-- admin.py
|    |-- apps.py
|    |-- models.py  定义了整个网站的models类,除了本应使用，还提供给其他应用
|    |-- shopmiddleware.py 定了整个网站的中间件（验证是否登录及权限管理信息）
|    |-- tests.py
|    |-- urls.py 配置了整个网站后台所有请求路由
|
|--web/ 前台应用（大堂点餐）
|    |-- __init__.py
|    |--views/
|    |    |--index.py 大堂点餐应用的登录、退出、验证码、加载店铺等方法
|    |    |--product.py 菜品展示视图
|    |    |--shopcart.py 购物车管理视图
|    |    |--orders.py 订单管理视图
|    |-- admin.py
|    |-- apps.py
|    |-- models.py 
|    |-- tests.py
|    |-- urls.py 配置了大堂点餐应用的所有请求路由
|
|--mobile/ 移动端点餐应用\
|    |-- __init__.py
|    |--views/
|    |    |--index.py 登录，退出路由
|    |    |--shop.py 店铺信息加载视图
|    |    |--product.py 菜品信息加载展示视图
|    |    |--orders.py 个人订单信息管理视图
|    |    |--member.py 个人中心管理视图
|    |    |--......
|    |
|    |-- admin.py
|    |-- apps.py
|    |-- models.py
|    |-- tests.py
|    |-- urls.py 配置了移动端点餐应用的所有请求路由
|
|--myobject/ 项目目录
|    |-- __init__.py
|    |-- settings.py
|    |-- urls.py
|    |-- wsgi.py
|
|--static/ 静态资源目录
|    |-- uploads/   上传文件存储目录
|    |-- myadmin/   后台管理静态资源目录
|    |-- web/   	大堂点餐静态资源目录
|    |-- mobile/    移动端管理静态资源目录
|
|--templates/ 模板目录
|    |-- myadmin/   后台管理模板目录
|    |-- web/   	大堂点餐模板目录
|    |-- mobile/    移动端管理模板目录
|
|--manage.py 入口文件
```

#### 4 访问方式

##### （1）本地访问

1.导入数据库   
2.启动服务： python manage.py runserver   
3.打开浏览器：网址：http://localhost:8000

##### （2）远程访问

1.导入数据库   
2.启动服务： python manage.py runserver 0.0.0.0:8000   
3.打开浏览器：网址：http://10.62.34.164:8000

#### 5 效果展示
##### （1）后台管理
<img width="540" alt="image" src="https://user-images.githubusercontent.com/38714822/159835881-9dd3f85d-2f08-4f7b-b2ae-403373167c3c.png">
<img width="1278" alt="image" src="https://user-images.githubusercontent.com/38714822/159835304-59755162-bd40-4d38-920a-4a8f7f823f36.png">

##### （2）前台大堂点餐
<img width="328" alt="image" src="https://user-images.githubusercontent.com/38714822/159836002-62cef75c-e680-41bf-b33c-4115ae0bba7a.png">
<img width="1270" alt="image" src="https://user-images.githubusercontent.com/38714822/159835421-b460539b-753c-4e14-900e-e4bcee53bcd5.png">

##### （3）移动端点餐
<img width="489" alt="image" src="https://user-images.githubusercontent.com/38714822/159835475-7df0ec07-38e9-42d8-9fe3-6a04ad294491.png">
<img width="807" alt="image" src="https://user-images.githubusercontent.com/38714822/159836232-d0cd3f94-8eef-4d2c-aaed-0b46e1d8122b.png">
<img width="810" alt="image" src="https://user-images.githubusercontent.com/38714822/159836395-e4caf628-1ffc-45b4-85f7-1cc096bafd57.png">
<img width="809" alt="image" src="https://user-images.githubusercontent.com/38714822/159836299-33c0f454-54b4-475d-a254-3a2c28ac1b7d.png">




