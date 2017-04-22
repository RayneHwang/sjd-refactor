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


# YuKun Wang: 22:00 21/04/2017
# 完善SJD_USER表字段
alter table `SJD_USER` 
add `nickname`			CHAR(32)				NOT NULL	DEFAULT ''		COMMENT '用户昵称',
add `sex`				TINYINT(3)	UNSIGNED	NOT NULL	DEFAULT '0' 	COMMENT '用户性别',
add `login`				INT(10) 				NOT NULL 	DEFAULT '0' 	COMMENT '登录次数',
add `full_level` 		INT(3) 					NOT NULL 					COMMENT '用户等级',
add `trust_score` 		INT(3) 					NOT NULL 					COMMENT '信任值',
add `identification` 	INT(3)					NOT NULL 					COMMENT '用户身份',
add `signature` 		TEXT					NOT NULL 					COMMENT '用户签名';

# YuKun Wang: 22:05 21/04/2017
# 将sjd_member, sjd_ucenter_member对应字段插入SJD_USER表
update `SJD_USER`, `sjd_member`
set `SJD_USER`.nickname = `sjd_member`.nickname, `SJD_USER`.sex = `sjd_member`.sex, `SJD_USER`.login = `sjd_member`.login, `SJD_USER`.signature = `sjd_member`.signature
where `SJD_USER`.id = `sjd_member`.uid;
update `SJD_USER`, `sjd_ucenter_member`
set `SJD_USER`.full_level = `sjd_ucenter_member`.full_level, `SJD_USER`.trust_score = `sjd_ucenter_member`.trust_score, `SJD_USER`.identification = `sjd_ucenter_member`.identification
where `SJD_USER`.id = `sjd_ucenter_member`.id;

# YuKun Wang: 21:43 22/04/2017
# 创建新的随手拍表
CREATE TABLE `SJD_SHOT` (
  `id`              INT(11) UNSIGNED NOT NULL AUTO_INCREMENT    COMMENT '随手拍ID',
  `content`         TEXT   			 NOT NULL                   COMMENT '随手拍内容',
  `uid`        		INT(10) UNSIGNED NOT NULL                   COMMENT '发布者ID',
  `create_time`     INT(11)          NOT NULL                   COMMENT '随手拍创建时间',
  `view_count`      INT(11)          NOT NULL DEFAULT '0'       COMMENT '浏览量',
  `cover_id`        INT(11)          NOT NULL                   COMMENT '封面ID',
  `reply_count`     INT(11)          NOT NULL DEFAULT '0'       COMMENT '评论数',
   PRIMARY KEY (`id`),
   CONSTRAINT fk_shot_uid FOREIGN KEY (`uid`) 
   REFERENCES SJD_USER(`ID`) ON DELETE CASCADE
)
  DEFAULT CHARSET = utf8                  COMMENT = '随手拍表';

# YuKun Wang: 21:57 22/04/2017
# 将sjd_issue_content内容导入新随手拍表SJD_SHOT
insert into SJD_SHOT(id, content, uid, create_time, view_count, cover_id, reply_count)
	select sjd_issue_content.id, sjd_issue_content.content, sjd_issue_content.uid, sjd_issue_content.create_time, sjd_issue_content.view_count, sjd_issue_content.cover_id, sjd_issue_content.reply_count 
    from sjd_issue_content, SJD_USER 
    where sjd_issue_content.uid = SJD_USER.id;
    


