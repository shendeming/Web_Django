# 自定义中间件类(执行是否登录判断)
from django.shortcuts import redirect
from django.urls import reverse

import re

class shopMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("shopMiddleware")

    def __call__(self, request):
        path = request.path
        print("url:", path)

        # 判断后台管理是否登录
        # 定义后台不登录也可直接访问的url列表
        urllist = ['/myadmin/login', '/myadmin/dologin', '/myadmin/logout','/myadmin/verify']
        # 判断当前请求url地址是否以/myadmin开头，并且不在urllist中，才做是否登录判断
        if re.match(r'^/myadmin',path) and (path not in urllist):
            # 判断是否登录(session中是否有adminuser)
            if 'adminuser' not in request.session:
                # 重定向到登录页
                return redirect(reverse("myadmin_login"))        # 由myadmin_login名字反向解析出url地址，然后重定向

        
        # 判断大堂点餐请求是否登录
        if re.match(r'^/web',path):
            # 判断是否登录(session中是否有webuser)
            if 'webuser' not in request.session:
                # 重定向到登录页
                return redirect(reverse("web_login"))        # 由web_login名字反向解析出url地址，然后重定向


        # 判断移动端是否登录
        # 定义移动端不登录也可直接访问的url列表
        urllist = ['/mobile/register', '/mobile/doregister']
        # 判断当前请求url地址是否以/mobile开头，并且不在urllist中，才做是否登录判断
        if re.match(r'^/mobile',path) and (path not in urllist):
            # 判断是否登录(session中是否有mobileuser)
            if 'mobileuser' not in request.session:
                # 重定向到登录页
                return redirect(reverse("mobile_register"))        # 由mobile_register名字反向解析出url地址，然后重定向

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response