#�鿴��ṹ

desc ������;

----

#MERGE�洢����

�ٷ��ĵ���http://dev.mysql.com/doc/refman/5.7/en/merge-storage-engine.html

�鿴���õ����棺**show engines**

##����һ�������ı�

������a,b�����ǵĽṹ��ȫ��ͬ��Ȼ��Ϳ��Խ���һ��c������ǵ�ddl��ȫһ��

```sql
CREATE TABLE a (
   `id` int(11) NOT NULL,
  `data` longtext NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE= MyISAM DEFAULT CHARSET=utf8;
CREATE TABLE b (
   `id` int(11) NOT NULL,
  `data` longtext NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE= MyISAM DEFAULT CHARSET=utf8;
drop table if exists data;
CREATE TABLE c (
   `id` int(11) NOT NULL,
  `data` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE= MRG_MYISAM ,UNION=(a,b);
```