#SJD Refactoring Project

##1. Install python3

##2. Install `pip`,`virtualenv`

##3. Install dependencies

```bash
virtualenv --no-site-packages flask-env
source flask-env/bin/activate
pip3 install --upgrade flask flask_login sqlalchemy

cd lib/mysql-connector-python-2.1.5
python setup.py install
```
##4. Database configuration
```
cp config.json.default config.json
```

Edit `config.json` 