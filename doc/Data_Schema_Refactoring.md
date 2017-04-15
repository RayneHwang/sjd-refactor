# 数据库表重构(基于SQLAlchemy)
Lei, HUANG: 18:01 15/04/2017

SQLAlchemy是Python的数据库工具, 包含`SQLAlchemy Core`和`SQLAlchemy ORM`两部分. `Core`实现了基本的数据库连接/表映射和CRUD/事务操作, `ORM`实现了Python对象到数据库表的映射, 方便用户像使用Python对象一样操作数据库的表并且持久化到数据库. 三角地的重构在数据库层面分为三个步骤:
- 根据原有的业务逻辑区分哪些表和表里面的哪些字段需要保留;
- 根据保留的字段编写DDL, 创建表并且将原来表里面的数据导入到新的表;
- 使用SQLAlchemy创建新表的映射类和基本操作

## 基于原有代码分析数据库表
三角地原有代码基于ThinkPHP, 

## 编写新表的DDL并导入数据

## 创建SQLAlchemy的映射类

## SQLAlchemy的基本使用


