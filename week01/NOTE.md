description:一周总结
author:fuguoliang <fglone@126.com>
createtime:2020-06-27

1. 常用命令
  1.1 临时替换
    pip install [packname] -i https://mirrors.aliyun.com/pypi/simple
   
  1.2 永久替换
    pip install pip -U  # 升级pip
    pip config set global.index-url https://mirror.aliyun.com/pypi/simple

  1.3 scrapy
    scrapy startproject [projectname] ## 新建项目
    scrapy genspider taobao taobao.com  # 创建蜘蛛模板
    scrapy crawl taobao   # 运行蜘蛛
   
2.第一遍仿老师代码，第二遍仿第一遍代码，第三遍参考第二遍，第四遍寻找扩展
多多思考，多多练习