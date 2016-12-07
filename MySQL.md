#�鿴��ṹ

desc ������;

----

#MERGE�洢����

�ٷ��ĵ���http://dev.mysql.com/doc/refman/5.7/en/merge-storage-engine.html

�鿴���õ����棺**show engines**

##����һ�������ı�

������a,b�����ǵĽṹ��ȫ��ͬ��Ȼ��Ϳ��Խ���һ��c������ǵ�ddl��ȫһ��

```sql
drop table if exists data;
CREATE TABLE c (
   `id` int(11) NOT NULL,
  `data` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE= MRG_MYISAM ,UNION=(a,b);
```

�ص㣺

���ֱ��ᴴ������������ͼ�ٶȸ��죻

�����������ֱ��Ͻ���ȫ������

----

#ɾ���������

����ֻ��һ��(gettime)��ͬ��ɾ������һ��

```sql
delete t1 from t as t1, t as t2 where
    t1.id = t2.id and
    t1.������=t2.������ and
    t1.gettime>t2.gettime;
```

----

#�޸ı� alter table

```sql
ALTER IGNORE TABLE `������`
MODIFY COLUMN `id`  int(11) NOT NULL FIRST,
MODIFY COLUMN `user` varchar(66) NOT NULL AFTER `id`,
MODIFY COLUMN `content` longtext NOT NULL AFTER `user`,
DROP PRIMARY KEY,
ADD PRIMARY KEY (`id`),
DROP INDEX `a1`,
ADD INDEX `a1` (`user`);
```

