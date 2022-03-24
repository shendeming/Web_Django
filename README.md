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

##### 本地访问

1.导入数据库   
2.启动服务： python manage.py runserver   
3.打开浏览器：网址：http://localhost:8000

##### 远程访问

1.导入数据库   
2.启动服务： python manage.py runserver 0.0.0.0:8000   
3.打开浏览器：网址：http://10.62.34.164:8000
