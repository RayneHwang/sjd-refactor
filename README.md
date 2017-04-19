# 三角地重构项目

## 1. 安装Python3

### Ubuntu
```bash
sudo apt-get install python3.4
```

### Windows
[下载安装包](https://www.python.org/downloads/windows/)并安装.

### macOS
[下载安装包](https://www.python.org/downloads/mac-osx/)并安装.



## 2. 安装 `pip3`,`virtualenv`
### Ubuntu
```bash
sudo apt-get install python3-pip
```
### Windows
```
esay_install pip3
```



## 3. 安装依赖

```bash
virtualenv --no-site-packages flask-env
source flask-env/bin/activate
pip3 install --upgrade flask flask_login flask-session sqlalchemy

cd lib/mysql-connector-python-2.1.5
python setup.py install
```
## 4. 数据库配置
```
cp config.default.json config.json
```

编辑`config.json`文件，将其中的配置改为自己的配置

 
##  5. 启动
```
python ./app.py
``` 
打开浏览器,输入`http://localhost:5000`
如果出现`Server started...`说明成功启动.
 
 
## 5. Flask
- [Flask框架](https://www.sqlalchemy.org/)

- 关于Jinja2模板引擎

- [关于WSGI/uWSGI](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832689740b04430a98f614b6da89da2157ea3efe2000)


## 6. ORM框架:SQLAlchemy
[SQLAlchemy文档](https://www.sqlalchemy.org/)

##7. 插件flask_login
[flask_login文档](http://flask-login.readthedocs.io/en/latest/)

