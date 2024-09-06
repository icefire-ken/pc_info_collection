# 简介

- 企业网络运维时，可能需要采集员工PC的网络信息，让网络运维人员能够根据这些信息快速判断员工PC的网络问题。
- 使用本脚本程序，可以方便、快捷的实现采集员工PC网络信息的工作。
- 并通过飞书机器人，将采集结果发送给指定网络运维人员。

# 创建飞书机器人

此脚本程序需要调用飞书机器人，需要先在飞书官网创建一个机器人。

## 1、登录飞书开放平台，进入开发者后台

访问[飞书开放平台](https://open.feishu.cn/)，登录后，进入开发者后台。
![login_open_feishu.png](https://github.com/icefire-ken/pc_info_collection/blob/main/Images/login_open_feishu.png)
![login_open_feishu_app.png](https://github.com/icefire-ken/pc_info_collection/blob/main/Images/login_open_feishu_app.png)

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
![app_authority_1.png](https://github.com/icefire-ken/pc_info_collection/blob/main/Images/app_authority_1.png)
![app_authority_2.png](https://github.com/icefire-ken/pc_info_collection/blob/main/Images/app_authority_2.png)
![app_authority_3.png](https://github.com/icefire-ken/pc_info_collection/blob/main/Images/app_authority_3.png)
权限包括：获取用户受雇信息、获取用户User ID、通过手机号或邮箱获取用户ID、获取与更新群组信息、获取群组信息、获取与发送单聊、群组消息、接收群聊中@机器人消息事件、以应用的身份发消息、获取与上传图片或文件资源、

## 5、发布应用

最后创建版本，发布应用，等待审核通过即可使用飞书机器人。
![app_release.png](https://github.com/icefire-ken/pc_info_collection/blob/main/Images/app_release.png)

# 使用方法

## 一、提供给普通员工使用

### Step1

提供给普通员工使用，需要网络运维人员提前配置好脚本程序使用的全局变量如下图：


# 更新日志

详见[UPDATE.md](https://github.com/icefire-ken/pc_info_collection/blob/main/UPDATE.md)。