-- Use mysql to store zhihu user information.

CREATE DATABASE `zhihu_user` /*!40100 DEFAULT CHARACTER SET utf8 */;


-- User base information table
CREATE TABLE `t_user` (
  `uid` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL COMMENT '用户名',                      
  `brief_info` varchar(400)  COMMENT '个人简介',
  `industry` varchar(50) COMMENT '所处行业',             
  `education` varchar(50) COMMENT '毕业院校',             
  `major` varchar(50) COMMENT '主修专业',
  `answer_count` int(10) unsigned DEFAULT 0 COMMENT '回答数',
  `article_count` int(10) unsigned DEFAULT 0 COMMENT '文章数',
  `ask_question_count` int(10) unsigned DEFAULT 0 COMMENT '提问数',
  `collection_count` int(10) unsigned DEFAULT 0 COMMENT '收藏数',
  `follower_count` int(10) unsigned DEFAULT 0 COMMENT '被关注数',
  `followed_count` int(10) unsigned DEFAULT 0 COMMENT '关注数',
  `follow_live_count` int(10) unsigned DEFAULT 0 COMMENT '关注直播数',
  `follow_topic_count` int(10) unsigned DEFAULT 0 COMMENT '关注话题数',
  `follow_column_count` int(10) unsigned DEFAULT 0 COMMENT '关注专栏数',
  `follow_question_count` int(10) unsigned DEFAULT 0 COMMENT '关注问题数',
  `follow_collection_count` int(10) unsigned DEFAULT 0 COMMENT '关注收藏夹数',
  `gmt_create` datetime NOT NULL COMMENT '创建时间',   
  `gmt_modify` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后一次编辑',             
  PRIMARY KEY (`uid`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='用户基本信息表';
