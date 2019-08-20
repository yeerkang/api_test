## 项目结构

- common :这个目录存放的是自己封装的类
- conf ：存放配置文件
- librarys ：别人封装好的模块
- logs ：存放日志文件的
- data ：存放测试数据的
- reporter ：存放测试报告的
- testcases ：自己封装的测试用例类

## vritualenv相关命令

- pip install virtualenv
- pip install virtualenvwrapper-win
- pip install pipenv
- 创建虚拟环境：mkvirtualenv -p python 虚拟环境名称
- 进入虚拟环境：workon 虚拟环境名称
- 退出虚拟环境：deactivate 
- 删除虚拟环境：rmvirtualenv

## virtualenv指定默认的解释器 virtualenv -p C:\xxxxxxxx 


## 导出虚拟环境中所有的模块和包

- 导出环境依赖：pip freeze > requirement.txt
- 恢复环境包：pip install -r requirement.txt

## pipenv的使用

- 创建虚拟环境：pipenv install --three
- 进入虚拟环境：pipenv shell
- 退出虚拟环境：exit
- 查看相关依赖包：pipenv graph
- 删除包：pipenv uninstall 包名
- 删除虚拟环境：pipenv --rm
- 恢复包环境：pipenv
- 导出环境所有包：pipenv lock -r > requirements.txt
- 列出本地工程路径：pipenv --where
- 列出虚拟环境路径：pipenv --venv
- 列出虚拟环境的python解释器：pipenv --py
- 查看包依赖：pipenv --graph
- 生成lock文件：pipenv --lock
- 激活虚拟环境：pipenv --shell






