#SJD Refactoring Project

##1. Install python3

##2. Install `pip`,`virtualenv`

##3. Install dependencies

```bash
virtualenv --no-site-packages flask-env
source flask-env/bin/activate
pip3 install --upgrade flask flask_login flask-session sqlalchemy

cd lib/mysql-connector-python-2.1.5
python setup.py install
```
##4. Database configuration
```
cp config.json.default config.json
```

Edit `config.json`
 
 
##5. Flask
- [Flask框架](https://www.sqlalchemy.org/)

- 关于Jinja2模板引擎

- [关于WSGI/uWSGI](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832689740b04430a98f614b6da89da2157ea3efe2000)


##6. ORM框架:SQLAlchemy
[SQLAlchemy文档](https://www.sqlalchemy.org/)

##7. 插件flask_login
[flask_login文档](http://flask-login.readthedocs.io/en/latest/)

##8. fl
