# -*- coding:utf-8 -*-

# YAML配置文件读取示例
# 测试使用前请将文件目录下的 _config.yml.template 修改成 _config.yml 并将其中的API信息补足

import yaml
import os

# # 获取当前文件的Realpath  ~/Documents/sourcetree_workspace/my-jenkins-email-notification-templates/script/testymlfileread.py
# fileNamePath = os.path.split(os.path.realpath(__file__))
# print(fileNamePath)
# fileNamePath = os.path.split(os.path.realpath(__file__))[0]
# print(fileNamePath)

# 获取当前文件夹路径 ~/Documents/sourcetree_workspace/my-jenkins-email-notification-templates/script
fileDirPath = os.path.dirname(__file__)
print(fileDirPath)

# 获取配置文件的路径 ~/Documents/sourcetree_workspace/my-jenkins-email-notification-templates/script/_config.yaml
yamlFilePath = os.path.join(fileDirPath,'_config.yml')
print(yamlFilePath)
# 加上 ,encoding='utf-8'，处理配置文件中含中文出现乱码的情况。
f = open(yamlFilePath,'r',encoding='utf-8')

cont = f.read()

x = yaml.load(cont)
print(type(x))
print(x)
print(x['jenkins_server_url'])
print(x['user_id'])
f.close()

