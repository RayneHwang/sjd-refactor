-- Lei, HUANG: 17:30 22/04/2017
-- 创建新的用户表
DROP TABLE IF EXISTS SJD_EVENT;
DROP TABLE IF EXISTS SJD_SHOT;
DROP TABLE IF EXISTS SJD_PICTURES;
DROP TABLE IF EXISTS SJD_USER_TRACK;
DROP TABLE IF EXISTS SJD_USER;
CREATE TABLE `SJD_USER` (
  `ID`        int(10) unsigned  NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `USERNAME`  VARCHAR(32)       NOT NULL                COMMENT '用户名',
  `PASSWORD`  VARCHAR(32)       NOT NULL                COMMENT '密码',
  `REALNAME`  VARCHAR(32)                               COMMENT '真实姓名',
  `NICKNAME`  VARCHAR(32)                               COMMENT '昵称',
  `AVATAR`    VARCHAR(20)                               COMMENT '头像路径',
  `SIGNATURE` text                                      COMMENT '个性签名',
  `WX_ID`     VARCHAR(30)                               COMMENT '微信OpenID',
  `SEX`       tinyint(3) unsigned NOT NULL DEFAULT '0'  COMMENT '性别, 0无可奉告1女2男',
  `BIRTHDAY`  date        DEFAULT '2016-10-10'          COMMENT '生日',
  `MOBILE`    VARCHAR(15) NOT NULL                      COMMENT '用户手机',
  `STATUS`    tinyint(4)  DEFAULT '0'                   COMMENT '用户状态',
  `TYPE`      tinyint(4)                                COMMENT '1为用户名注册，2为邮箱注册，3为手机注册',
  `SCHOOL`    VARCHAR(50)                               COMMENT '学校信息',
  `DEPARTMENT` VARCHAR(50)                              COMMENT '学院信息',
  `MAJOR`      VARCHAR(15)                              COMMENT  '专业',
  `STUDENT_ID` VARCHAR(15)                              COMMENT '学号',
  PRIMARY KEY (`ID`),
  INDEX `NICKNAME` (`NICKNAME`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表';

-- Lei, HUANG: 17:30 22/04/2017
-- Reset SJD_USER auto increment counter to max(id) in sjd_ucenter_member
SELECT MAX(id) + 1 FROM sjd_ucenter_member INTO @MAX_UID;
SET @s = CONCAT("ALTER TABLE SJD_USER AUTO_INCREMENT=", @MAX_UID);
PREPARE stmt FROM @s;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- Lei, HUANG: 17:30 22/04/2017
-- 将sjd_ucenter_member和sjd_member表里面的数据导入到SJD_USER
INSERT INTO SJD_USER (`ID`,
                      `USERNAME`,
                      `PASSWORD`,
                      `REALNAME`,
                      `NICKNAME`,
                      `SIGNATURE`,
                      `SEX`,
                      `BIRTHDAY`,
                      `MOBILE`,
                      `STATUS`,
                      `TYPE`,
                      `SCHOOL`,
                      `DEPARTMENT`,
                      `MAJOR`,
                      `STUDENT_ID`)
  SELECT
    um.id,
    um.username,
    um.password,
    um.realname,
    m.nickname,
    m.signature,
    m.sex,
    m.birthday,
    um.mobile,
    um.status,
    um.type,
    um.stu_school,
    um.department,
    um.major,
    um.student_id

  FROM sjd_ucenter_member um, sjd_member m
  WHERE um.id = m.uid;




-- Lei, HUANG: 17:30 22/04/2017
-- 将用户登录状态记录的数据从sjd_ucenter_member表当中抽出
DROP TABLE IF EXISTS SJD_USER_TRACK;
CREATE TABLE `SJD_USER_TRACK`(
  `UID` INT(10) UNSIGNED PRIMARY KEY NOT NULL COMMENT 'id in SJD_SUER',
  `LOGIN_COUNT` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '登录次数',
  `REG_IP` bigint(20) NOT NULL DEFAULT '0' COMMENT '注册IP',
  `REG_TIME` DATETIME COMMENT '注册时间',
  `LAST_LOGIN_IP` bigint(20) NOT NULL DEFAULT '0' COMMENT '最后登录IP',
  `LAST_LOGIN_TIME` DATETIME  COMMENT '最后登录时间',
  CONSTRAINT UID_FK FOREIGN KEY (UID) REFERENCES SJD_USER(ID)
  ON DELETE CASCADE
  ON UPDATE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户信息追踪';

-- Lei, HUANG: 17:30 22/04/2017
-- Reset SJD_USER auto increment counter to max(id) in sjd_ucenter_member
SELECT MAX(id) + 1 FROM sjd_ucenter_member INTO @MAX_UID;
SET @s = CONCAT("ALTER TABLE SJD_USER_TRACK AUTO_INCREMENT=", @MAX_UID);
PREPARE stmt FROM @s;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;


-- Lei, HUANG: 17:30 22/04/2017
-- 将redis当中用户和微信的绑定数据导入到SJD_USER表
UPDATE SJD_USER SET WX_ID='o4q_jwL4ATcp5Y3ct7Llk7wCA3bE' WHERE ID=4232;
UPDATE SJD_USER SET WX_ID='o4q_jwAphw36YF7o-PEMiaJALqxA' WHERE ID=4197;
UPDATE SJD_USER SET WX_ID='o4q_jwA5iG4rQqRqmNByzV7Bm8mQ' WHERE ID=4289;
UPDATE SJD_USER SET WX_ID='o4q_jwOdjfmJtbJM8G6dW9Nk11Tc' WHERE ID=4319;
UPDATE SJD_USER SET WX_ID='o4q_jwOXxlahM-fIjyM1y2Z7qOF8' WHERE ID=4345;
UPDATE SJD_USER SET WX_ID='o4q_jwAXluqdlnLQYcpOh1zvwl5U' WHERE ID=4301;
UPDATE SJD_USER SET WX_ID='o4q_jwJLaDoJTbnxG0ZNfhqCfoa4' WHERE ID=4194;
UPDATE SJD_USER SET WX_ID='o4q_jwOs-BE7NJJf5shAx5BaBMv8' WHERE ID=4144;
UPDATE SJD_USER SET WX_ID='o4q_jwNx2GNV6i6Tl2XLuRLpulD0' WHERE ID=4287;
UPDATE SJD_USER SET WX_ID='o4q_jwIo2fj3cdRaxEQqrQe8YcKk' WHERE ID=4087;
UPDATE SJD_USER SET WX_ID='o4q_jwMU4f8QF41TcTaR8YSYHxJE' WHERE ID=4129;
UPDATE SJD_USER SET WX_ID='o4q_jwFZ2fZNMtPTERLh1PszPbEM' WHERE ID=4168;
UPDATE SJD_USER SET WX_ID='o4q_jwP1KoSoNSl_VWuHPcPVv9Ag' WHERE ID=4308;
UPDATE SJD_USER SET WX_ID='o4q_jwCs_EweVeYCHQxfzxx9KPhA' WHERE ID=4218;
UPDATE SJD_USER SET WX_ID='o4q_jwNFnwfb_8wMR7t3XeNDfd4I' WHERE ID=4192;
UPDATE SJD_USER SET WX_ID='o4q_jwG37UvcGeIUNQey2eV08fdk' WHERE ID=4307;
UPDATE SJD_USER SET WX_ID='o4q_jwIwhMshGK-7ZVDljGV1rsCA' WHERE ID=4141;
UPDATE SJD_USER SET WX_ID='o4q_jwHByUvUxxTusKYrzy1kjOxs' WHERE ID=4147;
UPDATE SJD_USER SET WX_ID='o4q_jwIcWHYA1s7XELt0TEDjukwg' WHERE ID=4314;
UPDATE SJD_USER SET WX_ID='o4q_jwH9UcORMOrk7GQAKaGHInyU' WHERE ID=4231;
UPDATE SJD_USER SET WX_ID='o4q_jwN8itAGSCeDIt2cgSpsGNMw' WHERE ID=4149;
UPDATE SJD_USER SET WX_ID='o4q_jwHY3rpqPYwORqNsViY_exoc' WHERE ID=4145;
UPDATE SJD_USER SET WX_ID='o4q_jwAVGZc_0tjG5Nv6HSVYzvIk' WHERE ID=4071;
UPDATE SJD_USER SET WX_ID='o4q_jwG0_IXdLFXwLcnS4dhPIkuI' WHERE ID=4193;
UPDATE SJD_USER SET WX_ID='o4q_jwHvj3ws-6774qZMnk-GFigw' WHERE ID=4240;
UPDATE SJD_USER SET WX_ID='o4q_jwMAhZwlwaUu81pSrwrXoEig' WHERE ID=4089;
UPDATE SJD_USER SET WX_ID='o4q_jwOqfaJZczqo9bZY_ApBMhIk' WHERE ID=4355;
UPDATE SJD_USER SET WX_ID='o4q_jwP9yyRw6JoAKVwUQpsLaC3s' WHERE ID=4235;
UPDATE SJD_USER SET WX_ID='o4q_jwPostaorD0orcvRYHIatec4' WHERE ID=4331;
UPDATE SJD_USER SET WX_ID='o4q_jwHGgdk7ws2mVowQtDNE6Njs' WHERE ID=4361;
UPDATE SJD_USER SET WX_ID='o4q_jwFRcVcX9TsMeUcat33BsUJE' WHERE ID=4220;
UPDATE SJD_USER SET WX_ID='o4q_jwIMMDd1FQWdrD8lrtivRTNM' WHERE ID=4247;
UPDATE SJD_USER SET WX_ID='o4q_jwDSuwFUm0gJYqGyzJ1wWAJw' WHERE ID=4215;
UPDATE SJD_USER SET WX_ID='o4q_jwCNUytZ3ElvIZVqFefTu5lk' WHERE ID=4211;
UPDATE SJD_USER SET WX_ID='o4q_jwHKG8icY1XRfiGW6LKV5-mY' WHERE ID=4363;
UPDATE SJD_USER SET WX_ID='o4q_jwFaenAyAhcEiqyyZS6sf4z0' WHERE ID=4316;
UPDATE SJD_USER SET WX_ID='o4q_jwF3qzHnnmatadaeovgY1AhY' WHERE ID=4330;
UPDATE SJD_USER SET WX_ID='o4q_jwFmpGdSRFCWnoBTfCtS3rDc' WHERE ID=4229;
UPDATE SJD_USER SET WX_ID='o4q_jwOJaBRlIr0pr48v_QZi90bI' WHERE ID=4212;
UPDATE SJD_USER SET WX_ID='o4q_jwMU7Nun8tz9Wvj7xUceXfbs' WHERE ID=4213;
UPDATE SJD_USER SET WX_ID='o4q_jwLmfFgkmPoNYPGAAcBw-bAA' WHERE ID=4285;
UPDATE SJD_USER SET WX_ID='o4q_jwPCBkMaOM3Zhr9x0gf59pz0' WHERE ID=4338;
UPDATE SJD_USER SET WX_ID='o4q_jwPIWfiLprgHNaC9Kn6aZMd8' WHERE ID=4322;
UPDATE SJD_USER SET WX_ID='o4q_jwFnbzUD_tnV7lqNkIwiVhwU' WHERE ID=4293;
UPDATE SJD_USER SET WX_ID='o4q_jwAizgOqmJ0WEBMAq220xduQ' WHERE ID=4088;
UPDATE SJD_USER SET WX_ID='o4q_jwGYyf4hR7rVXOwTXeEU3uLU' WHERE ID=4102;
UPDATE SJD_USER SET WX_ID='o4q_jwBfh4dt8MsxC_f_n7M_0Kpk' WHERE ID=4099;
UPDATE SJD_USER SET WX_ID='o4q_jwDzT9ewu1Xeci5Gh1EGDceQ' WHERE ID=4182;
UPDATE SJD_USER SET WX_ID='o4q_jwNjCm2-wzk_YVGOGH2yRv8c' WHERE ID=4333;
UPDATE SJD_USER SET WX_ID='o4q_jwKrT27v4dTF8A8B6aHdeO58' WHERE ID=4313;
UPDATE SJD_USER SET WX_ID='o4q_jwIPPVyBoVvDD_CsiV3Ct1_8' WHERE ID=4343;
UPDATE SJD_USER SET WX_ID='o4q_jwOUvcfFqC2CgmHp-1WQviMg' WHERE ID=4304;
UPDATE SJD_USER SET WX_ID='o4q_jwC0-rnzZTJolSjUmUVxOOWo' WHERE ID=4336;
UPDATE SJD_USER SET WX_ID='o4q_jwAlGwVaLPX6XeKFEFGDrptw' WHERE ID=4089;
UPDATE SJD_USER SET WX_ID='o4q_jwO4vBd24iZUn_rjlKfokOfw' WHERE ID=4244;
UPDATE SJD_USER SET WX_ID='o4q_jwECWDmerqCCq3vG0_m0RmI8' WHERE ID=4364;


# YuKun Wang: 09:20 24/04/2017
# 创建图片封面表
DROP TABLE IF EXISTS SJD_PICTURES;
CREATE TABLE `SJD_PICTURES` (
  `ID`              INT(11) UNSIGNED NOT NULL AUTO_INCREMENT    COMMENT '图片ID',
  `PATH`         	  VARCHAR(255)   	 NOT NULL DEFAULT ''        COMMENT '图片路径',
  `CREATE_TIME`     INT(10) UNSIGNED NOT NULL DEFAULT '0'       COMMENT '创建时间',
  `MD5`     		    CHAR(32)         NOT NULL DEFAULT ''        COMMENT '文件md5',
  `SHA1`     	      CHAR(40)         NOT NULL DEFAULT ''        COMMENT '文件sha1',
   PRIMARY KEY (`ID`)
)ENGINE=InnoDB DEFAULT CHARSET = utf8 COMMENT = '图片封面表';

# YuKun Wang: 09:45 24/04/2017
# 将sjd_picture内容导入新表SJD_PICTURES
INSERT INTO SJD_PICTURES(ID,PATH,CREATE_TIME,MD5,SHA1)
	SELECT ID, PATH, CREATE_TIME, MD5,SHA1
    FROM sjd_picture;

# YuKun Wang: 09:40 24/04/2017
# 创建新的随手拍表
DROP TABLE IF EXISTS SJD_SHOT;
CREATE TABLE `SJD_SHOT` (
  `ID`              INT(11) UNSIGNED  NOT NULL AUTO_INCREMENT    COMMENT '随手拍ID',
  `CONTENT`         TEXT   			      NOT NULL                   COMMENT '随手拍内容',
  `UID`        		  INT(10) UNSIGNED  NOT NULL                   COMMENT '发布者ID',
  `CREATE_TIME`     INT(11)           NOT NULL                   COMMENT '随手拍创建时间',
  `VIEW_COUNT`      INT(11)           NOT NULL DEFAULT '0'       COMMENT '浏览量',
  `COVER_ID`        INT(11) UNSIGNED  NOT NULL                   COMMENT '封面ID',
  `REPLY_COUNT`     INT(11)           NOT NULL DEFAULT '0'       COMMENT '评论数',
  `STATUS`			TINYINT(11)		        NOT NULL DEFAULT '1'		   COMMENT '状态',
   PRIMARY KEY (`ID`),
   CONSTRAINT FK_SHOT_UID FOREIGN KEY (`UID`) REFERENCES SJD_USER(`ID`)
     ON DELETE CASCADE
     ON UPDATE CASCADE,
   CONSTRAINT FK_SHOT_COVER FOREIGN KEY (`COVER_ID`)REFERENCES SJD_PICTURES(`ID`)
     ON DELETE CASCADE
     ON UPDATE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET = utf8 COMMENT = '随手拍表';

# YuKun Wang: 21:57 22/04/2017
# 将sjd_issue_content内容导入新随手拍表SJD_SHOT
INSERT INTO SJD_SHOT (ID, CONTENT, UID, CREATE_TIME, VIEW_COUNT, COVER_ID, REPLY_COUNT, STATUS)
  SELECT
    sjd_issue_content.ID,
    sjd_issue_content.CONTENT,
    sjd_issue_content.UID,
    sjd_issue_content.CREATE_TIME,
    sjd_issue_content.VIEW_COUNT,
    sjd_issue_content.COVER_ID,
    sjd_issue_content.REPLY_COUNT,
    sjd_issue_content.STATUS
  FROM sjd_issue_content, SJD_USER, SJD_PICTURES
  WHERE     sjd_issue_content.UID = SJD_USER.ID
        AND sjd_issue_content.COVER_ID = SJD_PICTURES.ID;

# YuKun Wang, Feiyang Wang, 11:50  24/04/2017
# 创建新的活动表
DROP TABLE IF EXISTS SJD_EVENT;
ALTER TABLE sjd_event RENAME TO sjd_event_old;
CREATE TABLE `SJD_EVENT` (
  `ID`              INT(11) UNSIGNED  NOT NULL AUTO_INCREMENT     COMMENT '活动ID',
  `UID`        		  INT(10) UNSIGNED  NOT NULL                    COMMENT '发布者ID',
  `TITLE`        	  VARCHAR(255) 	    NOT NULL                    COMMENT '活动标题',
  `CONTENT`         TEXT   			      NOT NULL                    COMMENT '活动内容',
  `STIME`        	  INT(11)           NOT NULL                    COMMENT '活动开始时间',
  `ETIME`        	  INT(11)           NOT NULL                    COMMENT '活动结束时间',
  `ADDRESS`    	    VARCHAR(255)      NOT NULL                    COMMENT '活动地点',
  `CREATE_TIME`     INT(11)           NOT NULL 			              COMMENT '发布时间',
  `MAXCOUNT`        INT(11)           NOT NULL 			              COMMENT '活动最大报名人数',
  `COVER_ID`        INT(11) UNSIGNED  NOT NULL                    COMMENT '封面ID',
  `DEADLINE`     	  INT(11)           NOT NULL 					          COMMENT '报名截止时间',
  `IS_SIGN`			    INT(3)		 	      NOT NULL                    COMMENT '是否需要报名',
  `NEED_MONEY`		  INT(3)		 	      NOT NULL                    COMMENT '是否需要费用',
  `CLASSIFICATION`  INT(11)           NOT NULL 					          COMMENT '活动分类',
  `STATUS`     		  INT(11)           NOT NULL 					          COMMENT '状态',
  `UPDATE_TIME`     INT(11)           NOT NULL 					          COMMENT '更新时间',
  `VIEW_COUNT`  	  INT(11)           NOT NULL 					          COMMENT '浏览量',
  `REMARK_COUNT`    INT(11)           NOT NULL 					          COMMENT '评论数',
  `TYPE_ID`     	  INT(11)           NOT NULL 					          COMMENT '活动分类',
  `PASS_COUNT`     	INT(11)           NOT NULL 					          COMMENT '审核通过人数',
  `SIGN_COUNT`      INT(11)           NOT NULL 					          COMMENT '报名人数',
  `RANK_LEVEL`     	INT(3)            NOT NULL 					          COMMENT '排名等级',
  `IS_RECOMMEND`    TINYINT(4)        NOT NULL 					          COMMENT '是否首页推荐',
  `TAG`     	 	    TEXT          	  NOT NULL 					          COMMENT '活动标签',

   PRIMARY KEY (`ID`),
   CONSTRAINT FK_EVENT_UID FOREIGN KEY (`UID`) REFERENCES SJD_USER(`ID`)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
   CONSTRAINT FK_EVENT_COVER FOREIGN KEY (`COVER_ID`) REFERENCES SJD_PICTURES(`ID`)
     ON DELETE CASCADE
     ON UPDATE CASCADE
)ENGINE=InnoDB  DEFAULT CHARSET = utf8 COMMENT = '活动表';
  
# YuKun Wang, Feiyang Wang, 11:50  24/04/2017
# 旧活动表sjd_event数据导入SJD_EVENT
# 如果新表名和旧表名冲突, 把旧表名加上后缀_old
ALTER TABLE sjd_event RENAME TO sjd_event_old;

INSERT INTO SJD_EVENT (ID, UID, TITLE, CONTENT, STIME, ETIME, ADDRESS, CREATE_TIME, MAXCOUNT, COVER_ID, DEADLINE, IS_SIGN, NEED_MONEY, CLASSIFICATION, STATUS, UPDATE_TIME, VIEW_COUNT, REMARK_COUNT, TYPE_ID, PASS_COUNT, SIGN_COUNT, RANK_LEVEL, IS_RECOMMEND, TAG)
  SELECT
    sjd_event_old.id,
    sjd_event_old.uid,
    sjd_event_old.title,
    sjd_event_old.`explain`,
    sjd_event_old.sTime,
    sjd_event_old.eTime,
    sjd_event_old.address,
    sjd_event_old.create_time,
    sjd_event_old.limitCount,
    sjd_event_old.cover_id,
    sjd_event_old.deadline,
    sjd_event_old.is_sign,
    sjd_event_old.related_money,
    sjd_event_old.classification,
    sjd_event_old.`status`,
    sjd_event_old.update_time,
    sjd_event_old.view_count,
    sjd_event_old.reply_count,
    sjd_event_old.type_id,
    sjd_event_old.attentionCount,
    sjd_event_old.signCount,
    sjd_event_old.rank_level,
    sjd_event_old.is_recommend,
    sjd_event_old.biaoqian
  FROM sjd_event_old, SJD_USER, SJD_PICTURES
  WHERE sjd_event_old.uid = SJD_USER.id AND sjd_event_old.cover_id = SJD_PICTURES.id;


