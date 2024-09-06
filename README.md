# 简介

- 企业网络运维时，可能需要采集员工PC的网络信息，让网络运维人员能够根据这些信息快速判断员工PC的网络问题。
- 使用本脚本程序，可以方便、快捷的实现采集员工PC网络信息的工作。
- 并通过飞书机器人，将采集结果发送给指定网络运维人员。


# 创建飞书机器人

此脚本程序需要调用飞书机器人，需要先在飞书官网创建一个机器人。

## 1、登录飞书开放平台，进入开发者后台

访问[飞书开放平台](https://open.feishu.cn/)，登录后，进入开发者后台。

<img src="https://github.com/icefire-ken/pc_info_collection/blob/main/Images/login_open_feishu.png">

## 2、创建企业自建应用

点击创建企业自建应用。

<img src="https://github.com/icefire-ken/pc_info_collection/blob/main/Images/create_app.png" width="300">

为你的应用自定义名称，并点击创建，就可以看到新建的应用了。

<img src="https://github.com/icefire-ken/pc_info_collection/blob/main/Images/create_app_2.png" width="500">

<img src="https://github.com/icefire-ken/pc_info_collection/blob/main/Images/app.png" width="500">

## 3、查看应用信息

点击应用名称，进入应用详情页面，可以看到应用信息。

这里的App ID和App Secret，是非常重要的两个信息，后面需要用到。

![app_id_app_secret.png](https://github.com/icefire-ken/pc_info_collection/blob/main/Images/app_id_app_secret.png)

## 4、开通API权限

需要为应用开通API权限，才能调用飞书机器人的API。

**权限包括：**
- 获取用户受雇信息
- 获取用户User ID
- 通过手机号或邮箱获取用户ID
- 获取与更新群组信息
- 获取群组信息
- 获取与发送单聊、群组消息
- 接收群聊中@机器人消息事件
- 以应用的身份发消息
- 获取与上传图片或文件资源。

![app_authority_1.png](https://github.com/icefire-ken/pc_info_collection/blob/main/Images/app_authority_1.png)

![app_authority_2.png](https://github.com/icefire-ken/pc_info_collection/blob/main/Images/app_authority_2.png)

![app_authority_3.png](https://github.com/icefire-ken/pc_info_collection/blob/main/Images/app_authority_3.png)

## 5、发布应用

最后创建版本，发布应用，等待审核通过即可使用飞书机器人。

<img src="https://github.com/icefire-ken/pc_info_collection/blob/main/Images/app_release.png" width="700">


# 使用方法

## 一、提供给普通员工使用

普通员工启动.exe程序后，直接点击相应功能即可，不需要额外设置配置信息，简化使用成本。

这就要求网络运维人员提前配置好脚本程序中使用到的全局变量，然后再打包成.exe程序。

### 1.1 移植环境

通过`requirements.txt`文件，将脚本移植到本地环境，推荐是虚拟环境。

使用`pip install -r requirements.txt`下载脚本所需要的模块。

### 1.2 配置全局变量

在脚本的全局变量部分中，配置飞书机器人App ID和App Secret、接收者User ID，测试内部、外部URL地址。

这里需要填写的接收者User ID，需要到飞书后台查看，通过API调试台测试获取。

### 1.3 测试脚本

完成配置，测试运行脚本，验证指定的飞书接收者是否能够收到消息。

### 1.4 打包成.exe程序

安装pyinstaller，使用`pyinstaller -F pc_info_collection.py`打包成.exe程序。

## 二、提供给网络运维人员使用

网络运维人员在脚本程序使用上可能需要更灵活一些，因此直接使用项目上Release的.exe程序即可。

其中没有预配置任何参数，每次运行都需要手动输入参数设置，有需要时可以随时修改相关配置参数。


# 更新日志

详见[UPDATE.md](https://github.com/icefire-ken/pc_info_collection/blob/main/UPDATE.md)。