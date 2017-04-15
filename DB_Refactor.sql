# Lei, HUANG: 16:17 15/04/2017
# 创建新的用户表
# 原表名:sjd_ucenter_member
CREATE TABLE `SJD_USER` (
  `id`              INT(10) UNSIGNED NOT NULL AUTO_INCREMENT    COMMENT '用户ID',
  `username`        CHAR(32)         NOT NULL                   COMMENT '用户名',
  `password`        CHAR(32)         NOT NULL                   COMMENT '密码',
  `realname`        CHAR(32)                  DEFAULT NULL      COMMENT '真实姓名',
  `email`           CHAR(32)                  DEFAULT NULL,
  `mobile`          CHAR(15)         NOT NULL                   COMMENT '用户手机',
  `reg_time`        INT(10) UNSIGNED NOT NULL DEFAULT '0'       COMMENT '注册时间',
  `reg_ip`          BIGINT(20)       NOT NULL DEFAULT '0'       COMMENT '注册IP',
  `last_login_time` INT(10) UNSIGNED NOT NULL DEFAULT '0'       COMMENT '最后登录时间',
  `last_login_ip`   BIGINT(20)       NOT NULL DEFAULT '0'       COMMENT '最后登录IP',
  `update_time`     INT(10) UNSIGNED NOT NULL DEFAULT '0'       COMMENT '更新时间',
  `status`          TINYINT(4)                DEFAULT '0'       COMMENT '用户状态',
  `type`            TINYINT(4)       NOT NULL                   COMMENT '1为学号注册，2为邮箱注册，3为手机注册',
  `school`          CHAR(50)         NOT NULL                   COMMENT '学校信息',
  `department`      CHAR(50)         NOT NULL                   COMMENT '学院信息',
  `major`           CHAR(50)         NOT NULL                   COMMENT '班级信息',
  `student_id`      VARCHAR(15)               DEFAULT NULL      COMMENT '学号',
  PRIMARY KEY (`id`),
  KEY `status` (`status`)
)
  ENGINE = MyISAM
  AUTO_INCREMENT = 4374
  DEFAULT CHARSET = utf8                  COMMENT = '用户表';


# Lei, HUANG: 16:18 15/04/2017
# 将原来sjd_ucenter_member表的内容插入到新的用户表里面, 删除无用的字段
INSERT INTO SJD_USER (id, username, password, realname, email, mobile, reg_time, reg_ip, last_login_time, last_login_ip, update_time, status, type, school, department, major, student_id)
  SELECT id, username, password, realname, email, mobile, reg_time, reg_ip, last_login_time, last_login_ip, update_time, status, type, stu_school, department, major, student_id
  FROM sjd_ucenter_member;

