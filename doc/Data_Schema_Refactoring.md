# 数据库表重构(基于SQLAlchemy)
> Lei, HUANG: 18:01 15/04/2017

SQLAlchemy是Python的数据库工具, 包含`SQLAlchemy Core`和`SQLAlchemy ORM`两部分. `Core`实现了基本的数据库连接/表映射和CRUD/事务操作, `ORM`实现了Python对象到数据库表的映射, 方便用户像使用Python对象一样操作数据库的表并且持久化到数据库. 三角地的重构在数据库层面分为三个步骤:
- 根据原有的业务逻辑区分哪些表和表里面的哪些字段需要保留;
- 根据保留的字段编写DDL, 创建表并且将原来表里面的数据导入到新的表;
- 使用SQLAlchemy创建新表的映射类和基本操作

## 基于原有代码分析数据库表
三角地原有代码基于ThinkPHP, 因此对数据库表的分析需要查看PHP代码中的数据库操作. 
以登录操作为例, 涉及到`sjd_ucenter_member`表中`username`和`password`两项的对比, 因此需要找到源代码中对这个表的操作.

```php
<?php
  $uid = UCenterMember()->register($aUsername, $aNickname, $aPassword, $email, $mobile,$aUnType,$addregisterinfo); 
?>
```

其中密码的生成
```php
  function sjd_md5($str){    
      return '' === $str ? '' : substr(md5($str),8,16);
  }
```
可以看出原来三角地当中的密码存储是将用户输入的明文密码使用md5加密然后截取第8到24位构成16位的密码密文.
原来`sjd_ucenter_member`表的表结构:
```sql
CREATE TABLE `sjd_ucenter_member` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `username` char(32) NOT NULL COMMENT '用户名',
  `password` char(32) NOT NULL COMMENT '密码',
  `realname` char(32) DEFAULT NULL COMMENT '真实姓名',
  `email` char(32) DEFAULT NULL,
  `mobile` char(15) NOT NULL COMMENT '用户手机',
  `email_checked` tinyint(1) NOT NULL,
  `mobile_checked` tinyint(1) NOT NULL,
  `full_level` int(3) NOT NULL,
  `trust_score` int(3) NOT NULL,
  `reg_time` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '注册时间',
  `reg_ip` bigint(20) NOT NULL DEFAULT '0' COMMENT '注册IP',
  `last_login_time` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '最后登录时间',
  `last_login_ip` bigint(20) NOT NULL DEFAULT '0' COMMENT '最后登录IP',
  `update_time` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '更新时间',
  `status` tinyint(4) DEFAULT '0' COMMENT '用户状态',
  `type` tinyint(4) NOT NULL COMMENT '1为用户名注册，2为邮箱注册，3为手机注册',
  `stu_school` char(50) NOT NULL COMMENT '学校信息',
  `department` char(50) NOT NULL COMMENT '学院信息',
  `major` char(50) NOT NULL COMMENT '班级信息',
  `identification` int(3) NOT NULL,
  `is_upload` int(11) DEFAULT '0',
  `random_num` int(11) DEFAULT '0',
  `student_id` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `status` (`status`)
) ENGINE=MyISAM AUTO_INCREMENT=4374 DEFAULT CHARSET=utf8 COMMENT='用户表'
```
显然我们只需要一部分字段就行了, 比如保留`id`, `username`, `password`, `realname`, `email`, `mobile`, `reg_time`, `reg_ip`, `last_login_time`, `last_login_ip`, `update_time`, `status`, `type`, `school`, `department`, `major`, `student_id`这些字段, 即可完成最基本的登录功能. 




## 编写新表的DDL并导入数据
精简过的表结构:
```sql
CREATE TABLE `SJD_USER` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `username` char(32) NOT NULL COMMENT '用户名',
  `password` char(32) NOT NULL COMMENT '密码',
  `realname` char(32) DEFAULT NULL COMMENT '真实姓名',
  `email` char(32) DEFAULT NULL,
  `mobile` char(15) NOT NULL COMMENT '用户手机',
  `reg_time` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '注册时间',
  `reg_ip` bigint(20) NOT NULL DEFAULT '0' COMMENT '注册IP',
  `last_login_time` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '最后登录时间',
  `last_login_ip` bigint(20) NOT NULL DEFAULT '0' COMMENT '最后登录IP',
  `update_time` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '更新时间',
  `status` tinyint(4) DEFAULT '0' COMMENT '用户状态',
  `type` tinyint(4) NOT NULL COMMENT '1为用户名注册，2为邮箱注册，3为手机注册',
  `school` char(50) NOT NULL COMMENT '学校信息',
  `department` char(50) NOT NULL COMMENT '学院信息',
  `major` char(50) NOT NULL COMMENT '班级信息',
  `student_id` varchar(15) DEFAULT NULL COMMENT '学号',
  PRIMARY KEY (`id`),
  KEY `status` (`status`)
) ENGINE=MyISAM AUTO_INCREMENT=4380 DEFAULT CHARSET=utf8 COMMENT='用户表'
```

现在面临的问题是如何将原有`sjd_ucenter_member`当中的数据导入到`SJD_USER`表当中去, 可以使用`INSERT INTO SELECT`语句

```sql
INSERT INTO SJD_USER (id, username, password, realname, email, mobile, reg_time, reg_ip, last_login_time, last_login_ip, update_time, status, type, school, department, major, student_id)
  SELECT id, username, password, realname, email, mobile, reg_time, reg_ip, last_login_time, last_login_ip, update_time, status, type, stu_school, department, major, student_id
  FROM sjd_ucenter_member;
```
> 所有对表结构的更新/新增必须添加到项目根目录的`DB_Refactor`文件当中去, 注释修改人/时间/修改内容

## 创建SQLAlchemy的映射类
有了DDL, 可以据此编写SQLAlchemy的映射类
在项目Models文件夹当中新建python文件,文件名为数据库当中的表名
在文件中新建类, 类目为数据库表名转换成的类名.
> SQL规范当中数据库表名应为大写,使用下划线分割, 而Python的PEP8规范当中要求类名使用首字母大写的[驼峰命名法](https://en.wikipedia.org/wiki/Camel_case), 因此数据库当中的表名若是`SJD_USER`, 那么对应的类名应为`SjdUser`. 
```python

class SjdUser(BASE):
    __tablename__ = "SJD_USER"
    id = Column(Integer, primary_key=True)
    username = Column(String(32))
    password = Column(String(32))
    realname = Column(String(32))
    email = Column(String(32))
    mobile = Column(String(15))
    reg_time = Column(Integer)
    reg_ip = Column(Integer)
    last_login_time = Column(Integer)
    last_login_ip = Column(Integer)
    update_time = Column(Integer)
    status = Column(Integer)
    type = Column(Integer)
    school = Column(String(50))
    department = Column(String(50))
    major = Column(String(50))
    student_id = Column(String(15))

    def __init__(self, username, password, **kwargs):
        self.username = username
        self.password = password
        self.reg_time = datetime.datetime.utcnow()
        self.update_time = datetime.datetime.utcnow()
        self.last_login_time = datetime.datetime.utcnow()
        self.mobile = kwargs['mobile']
        self.type = kwargs['type']
        self.major = kwargs['major']
        self.department = kwargs['department']
        self.student_id = kwargs['student_id']
        self.reg_ip = kwargs['reg_ip']
        self.last_login_ip = kwargs['last_login_ip']
        self.school = kwargs['school']

    def __repr__(self):
        return '<SJD_USER %s>' % self.id

```

**注意类的字段名必须和数据库对应的列名一致.**

到此ORM映射类编写完毕.


## SQLAlchemy的基本使用

有了ORM映射类, 可以直接使用SQLAlchemy框架操作数据库

### 查询
```python
# 通过给定的usernmae查询用户
registered_user = get_session().query(SjdUser).filter(SjdUser.username == username).first()
```

### 新增
```python
user = SjdUser(...) #实例化一个SjdUer
db_session = get_session()
db_session = get_session()
db_session.add(user) # 插入到数据库
db_session.commit()
db_session.close() # 务必记得关闭session
```

其他SQLAlchemy的操作可以查阅SQLAlchemy的[官网](https://www.sqlalchemy.org/).