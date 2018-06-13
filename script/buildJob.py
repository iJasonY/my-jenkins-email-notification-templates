# -*- coding: utf-8 -*-

#Build Jenkins Job

import jenkins
from time import sleep
import yaml
import os


# 读取yaml文件
def readyaml():
    # 获取当前文件夹路径
    fileDirPath = os.path.dirname(__file__)
    # print(fileDirPath)

    # 获取yaml配置文件的路径
    yamlFilePath = os.path.join(fileDirPath, '_config.yml')
    # print(yamlFilePath)

    # 加上 ,encoding='utf-8'，处理配置文件中含中文出现乱码的情况。
    f = open(yamlFilePath, 'r', encoding='utf-8')
    #读取yaml配置文件内容
    data = yaml.load(f)
    f.close()
    # print data
    return data



# 读取_config.yml文件的配置信息
api_confg_data = readyaml()

# 远程的jenkins master server的url，以及port
jenkins_server_url=api_confg_data['jenkins_server_url']

# 用户的User Id 和 API Token，
user_id=api_confg_data['user_id']
api_token=api_confg_data['api_token']



# 实例化jenkins对象，连接远程的jenkins master server
server=jenkins.Jenkins(jenkins_server_url, username=user_id, password=api_token)
user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s \n' % (user['fullName'], version))





# 获取job名为job_name的job的相关信息
job_name='JenkinsTestDemo'

isExists=server.job_exists(job_name)

if(isExists==True):
    # 如果存在job,则开始构建job
    # 获取本次构建编号
    next_build_number = server.get_job_info(job_name)['nextBuildNumber']
    # 开始构建job（不带构建参数）
    output = server.build_job(job_name)
    print('正在构建%s job...' % (job_name))
    sleep(7) # 睡眠7秒
    # 获取构建信息并打印
    build_info = server.get_build_info(job_name, next_build_number)
    print(build_info)
else:
    print('┗|｀O′|┛ 嗷~~ ，名为 %s 的 job 居然不存在🙄 ' % (job_name))






# get all jobs from the specific view
# jobs = server.get_jobs()
# print(jobs)

# 构建job名为job_name的job（不带构建参数）

# server.build_job(job_name)

# #String参数化构建job名为job_name的job, 参数param_dict为字典形式，如：param_dict= {"param1"：“value1”， “param2”：“value2”} 

# server.build_job(job_name, parameters=param_dict)

# #获取job名为job_name的job的最后次构建号

# server.get_job_info(job_name)['lastBuild']['number']

# #获取job名为job_name的job的某次构建的执行结果状态

# server.get_build_info(job_name,build_number)['result']　　   

# #判断job名为job_name的job的某次构建是否还在构建中

# server.get_build_info(job_name,build_number)['building']
