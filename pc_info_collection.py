#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 导入模块
import PySimpleGUI as sg
import requests
import subprocess
import json
import lark_oapi as lark
from lark_oapi.api.im.v1 import *
from lark_oapi.api.contact.v3 import *

# 全局变量
# 这里配置好各个变量方便将程序提供给普通用户使用，普通用户不再需要填写这些配置，点击使用功能即可。
# 这里配置各个变量保持为空，是给高级用户使用，可以按需填写这些配置，达到灵活使用的目的。
INTERNAL_URL = ''  # 内部测试URL
EXTERNAL_URL = ''  # 外部测试URL
APP_ID = ''  # 飞书app id
APP_SECRET = ''  # 飞书app secret
RECEIVER_MOBILE = ''  # 飞书接收者手机号码
RECEIVER_USER_ID = ''  # 飞书接收者user id


# 获取公网IP地址
def get_public_ip(gui):
    try:
        response = requests.get('http://4.ipw.cn')  # 访问此链接，显示本机公网IP地址
        public_ip = response.text  # 提取返回的公网IP地址

    except Exception as e:  # 捕获异常，并弹出提示
        sg.popup(f'发生错误：{e}', title='错误提示', keep_on_top=True)

    else:  # 没有异常，则在GUI上显示获取到的信息
        gui['-DISPLAY-'].print('=' * 10 + ' ' + '公网 IP 地址' + ' ' + '=' * 10 + '\n')
        gui['-DISPLAY-'].print(public_ip + '\n')  # 在GUI界面上显示公网IP地址
        return f'### 公网 IP 地址 ###\n{public_ip}'  # 返回信息，给飞书发送


# 获取网络配置信息
def get_network_info(gui):
    try:  # 模仿CMD输入ipconfig /all命令，获取网络配置信息
        network_info = subprocess.run('ipconfig /all', capture_output=True, text=True, check=True)

    except Exception as e:  # 捕获异常，并弹出提示
        sg.popup(f'发生错误：{e}', title='错误提示', keep_on_top=True)

    else:  # 没有异常，则在GUI上显示获取到的信息
        gui['-DISPLAY-'].print('=' * 10 + ' ' + '网络信息' + ' ' + '=' * 10 + '\n')
        gui['-DISPLAY-'].print(network_info.stdout + '\n')  # 在GUI界面上显示网络配置信息
        return f'### 网络信息 ###\n{network_info.stdout}'  # 返回信息，给飞书发送


# 测试内部URL访问
def test_internal_url_connection(gui, url_internal):
    real_internal_url = 'https://' + url_internal  # 拼接requests所需的完整URL
    try:  # 访问内部URL
        response_internal = requests.get(real_internal_url, timeout=5)

        if response_internal.status_code == 200:  # 判断HTTP返回码，200即访问成功
            test_internal_url_result = f'内网：{real_internal_url} 访问成功！'
        else:
            test_internal_url_result = f'内网：{real_internal_url} 访问失败！'
            # 注意，有些URL即便能打开，返回码未必是200

    except Exception as e:  # 捕获异常，并弹出提示
        sg.popup(f'发生错误：{e}', title='错误提示', keep_on_top=True)

    else:  # 没有异常，则在GUI上显示测试内部URL的结果
        gui['-DISPLAY-'].print('=' * 10 + ' ' + '测试内、外网URL访问' + ' ' + '=' * 10 + '\n')
        gui['-DISPLAY-'].print(test_internal_url_result + '\n')  # 在GUI界面上显示测试内部URL的结果
        return f'### 测试内网URL访问 ###\n{test_internal_url_result}'  # 返回信息，给飞书发送


# 测试外部URL访问
def test_external_url_connection(gui, url_external):
    real_external_url = 'https://' + url_external  # 拼接requests所需的完整URL
    try:  #
        response_external = requests.get(real_external_url, timeout=5)

        if response_external.status_code == 200:  # 判断HTTP返回码，200即访问成功
            test_external_url_result = f'外网：{real_external_url} 访问成功！'
        else:
            test_external_url_result = f'外网：{real_external_url} 访问失败！'
            # 注意，有些URL即便能打开，返回码未必是200

    except Exception as e:  # 捕获异常，并弹出提示
        sg.popup(f'发生错误：{e}', title='错误提示', keep_on_top=True)

    else:  # 没有异常，则在GUI上显示测试外部URL的结果
        gui['-DISPLAY-'].print('=' * 10 + ' ' + '测试外网URL访问' + ' ' + '=' * 10 + '\n')
        gui['-DISPLAY-'].print(test_external_url_result + '\n')  # 在GUI界面上显示测试外部URL的结果
        return f'### 测试外网URL访问 ###\n{test_external_url_result}'  # 返回信息，给飞书发送


# 获取开放的端口
def get_open_port(gui):
    try:  # 模仿CMD输入netstat -ano命令，获取开放的端口
        open_port = subprocess.run('netstat -ano', capture_output=True, text=True, check=True)

    except Exception as e:  # 捕获异常，并弹出提示
        sg.popup(f'发生错误：{e}', title='错误提示', keep_on_top=True)

    else:  # 没有异常，则在GUI上显示获取到的信息
        gui['-DISPLAY-'].print('=' * 10 + ' ' + '开放的端口' + ' ' + '=' * 10 + '\n')
        gui['-DISPLAY-'].print(open_port.stdout + '\n')  # 在GUI界面上显示开放的端口信息
        return f'### 开放的端口 ###\n{open_port.stdout}'  # 返回信息，给飞书发送


# 获取路由表信息
def get_routing_table(gui):
    try:  # 模仿CMD输入route print命令，获取路由表信息
        routing_table = subprocess.run('route print', capture_output=True, text=True, check=True)

    except Exception as e:  # 捕获异常，并弹出提示
        sg.popup(f'发生错误：{e}', title='错误提示', keep_on_top=True)

    else:  # 没有异常，则在GUI上显示获取到的信息
        gui['-DISPLAY-'].print('=' * 10 + ' ' + '路由表' + ' ' + '=' * 10 + '\n')
        gui['-DISPLAY-'].print(routing_table.stdout + '\n')  # 在GUI界面上显示路由表信息
        return f'### 路由表 ###\n{routing_table.stdout}'  # 返回信息，给飞书发送


# 获取飞书接收者信息
def get_user_info(app_id, app_secret, receiver_mobile):
    # 创建client，指定飞书机器人的app_id和app_secret
    client = lark.Client.builder() \
        .app_id(app_id) \
        .app_secret(app_secret) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象，指定接收者的手机号
    request: BatchGetIdUserRequest = BatchGetIdUserRequest.builder() \
        .user_id_type("open_id") \
        .request_body(BatchGetIdUserRequestBody.builder()
                      .mobiles([receiver_mobile])
                      .build()) \
        .build()

    # 发起请求
    response: BatchGetIdUserResponse = client.contact.v3.user.batch_get_id(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.contact.v3.user.batch_get_id failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))

    return response.data.user_list[0].user_id  # 返回user id


# 飞书发送信息
def feishu_send(app_id, app_secret, receive_id, content):
    # 创建client，指定飞书机器人的app_id和app_secret
    client = lark.Client.builder() \
        .app_id(app_id) \
        .app_secret(app_secret) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象，指定接收者的user id、消息类型、消息内容
    request: CreateMessageRequest = CreateMessageRequest.builder() \
        .receive_id_type("open_id") \
        .request_body(CreateMessageRequestBody.builder()
                      .receive_id(receive_id)
                      .msg_type("text")
                      .content(json.dumps({"text": content}))
                      .build()) \
        .build()

    # 发起请求
    response: CreateMessageResponse = client.im.v1.message.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.im.v1.message.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


# 构建窗体
def create_window():
    global APP_ID, APP_SECRET, RECEIVER_MOBILE, INTERNAL_URL, EXTERNAL_URL, RECEIVER_USER_ID

    # 构建获取公网IP地址按钮，并赋值
    get_public_ip_button = sg.Button('获取公网IP地址', key='-GET_PUBLIC_IP-', size=(15, 1))

    # 构建获取网络配置信息按钮，并赋值
    get_network_info_button = sg.Button('获取网络信息', key='-GET_NETWORK_INFO-', size=(15, 1))

    # 构建测试内部、外部URL访问按钮，并赋值
    test_url_connection_button = sg.Button('测试内、外网URL', key='-TEST_URL_CONNECTION-', size=(15, 1))

    # 构建获取开放的端口按钮，并赋值
    get_open_port_button = sg.Button('获取开放端口', key='-GET_OPEN_PORT-', size=(15, 1))

    # 构建获取路由表信息按钮，并赋值
    get_routing_table_button = sg.Button('获取路由表', key='-GET_ROUTING_TABLE-', size=(15, 1))

    # 构建显示获取信息的窗口
    display_info = sg.Output(key='-DISPLAY-', size=(83, 29))

    # 构建工具栏配置选项
    set_options = sg.Menu([['基本配置', ['APP_ID', 'APP_SECRET', '接收者手机号码']],
                           ['URL测试配置', ['内部URL地址', '外部URL地址']]])

    # 构建窗体布局
    layout = [
        [
            set_options,
            sg.Column([
                [get_public_ip_button],
                [get_network_info_button],
                [test_url_connection_button],
                [get_open_port_button],
                [get_routing_table_button]
            ], size=(150, 500)),
            sg.Column([
                [display_info]
            ], size=(650, 500))
        ]
    ]

    # 构建窗体
    window = sg.Window('PC Infomation Collection', layout, size=(800, 500))

    # 窗体事件
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        elif event == '-GET_PUBLIC_IP-':  # 点击获取公网IP地址按钮
            message_public_ip = get_public_ip(window)  # 获取公网IP地址
            feishu_send(APP_ID, APP_SECRET, RECEIVER_USER_ID, message_public_ip)  # 通过飞书发送公网IP地址给指定用户

        elif event == '-GET_NETWORK_INFO-':  # 点击获取网络配置信息按钮
            message_network_info = get_network_info(window)  # 获取网络配置信息
            feishu_send(APP_ID, APP_SECRET, RECEIVER_USER_ID, message_network_info)  #

        elif event == '-TEST_URL_CONNECTION-':  # 点击测试内、外网URL按钮
            message_test_internal_url = test_internal_url_connection(window, INTERNAL_URL)  # 测试内网URL
            message_test_external_url = test_external_url_connection(window, EXTERNAL_URL)  # 测试外网URL
            feishu_send(APP_ID, APP_SECRET, RECEIVER_USER_ID, message_test_internal_url)  # 通过飞书发送内网URL测试结果给指定用户
            feishu_send(APP_ID, APP_SECRET, RECEIVER_USER_ID, message_test_external_url)  # 通过飞书发送外网URL测试结果给指定用户

        elif event == '-GET_OPEN_PORT-':  # 点击获取开放端口按钮
            message_open_port = get_open_port(window)  # 获取开放端口信息
            feishu_send(APP_ID, APP_SECRET, RECEIVER_USER_ID, message_open_port)  #

        elif event == '-GET_ROUTING_TABLE-':  # 点击获取路由表按钮
            message_routing_table = get_routing_table(window)  # 获取路由表信息
            feishu_send(APP_ID, APP_SECRET, RECEIVER_USER_ID, message_routing_table)  # 通过飞书发送路由表信息给指定用户

        # 设置APP_ID
        elif event == 'APP_ID':
            APP_ID = sg.popup_get_text('请输入飞书开发平台的APP ID', title='设置APP ID', keep_on_top=True, default_text='')

        # 设置APP_SECRET
        elif event == 'APP_SECRET':
            APP_SECRET = sg.popup_get_text('请输入飞书开发平台的APP SECRET', title='设置APP SECRET', keep_on_top=True, default_text='')

        # 设置接收者手机号码
        elif event == '接收者手机号码':
            RECEIVER_MOBILE = sg.popup_get_text('请输入接收者手机号码：', title='设置接收者手机号码', keep_on_top=True, default_text='')
            RECEIVER_USER_ID = get_user_info(APP_ID, APP_SECRET, RECEIVER_MOBILE)  # 通过接收者手机号码获取接收者user id

        # 设置内部URL地址
        elif event == '内部URL地址':
            INTERNAL_URL = sg.popup_get_text('请输入要测试的内部URL地址：', title='设置内部URL地址', keep_on_top=True, default_text='www.163.com')

        # 设置外部URL地址
        elif event == '外部URL地址':
            EXTERNAL_URL = sg.popup_get_text('请输入要测试的外部URL地址：', title='设置外部URL地址', keep_on_top=True, default_text='www.baidu.com')

    window.close()


if __name__ == '__main__':
    create_window()
