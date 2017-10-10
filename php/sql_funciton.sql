#SQL by wooght 2017
create database if not exists vip default character set 'utf8';
#Query OK, 1 row affected (0.00 sec)

drop database vip;
#Query OK, 0 rows affected (0.00 sec)

use wooght_2017;
#Database changed

create table if not exists vip(
id int(4) not null primary key auto_increment,
name varchar(16) not null default 'youke',
age int(3) not null default 18,
phone varchar(16),
mk_time timestamp default current_timestamp);
#Query OK, 0 rows affected (0.12 sec)

 desc vip;
 /*
+---------+-------------+------+-----+-------------------+----------------+
| Field   | Type        | Null | Key | Default           | Extra          |
+---------+-------------+------+-----+-------------------+----------------+
| id      | int(4)      | NO   | PRI | NULL              | auto_increment |
| name    | varchar(16) | NO   |     | youke             |                |
| age     | int(3)      | NO   |     | 18                |                |
| phone   | varchar(16) | YES  |     | NULL              |                |
| mk_time | timestamp   | NO   |     | CURRENT_TIMESTAMP |                |
+---------+-------------+------+-----+-------------------+----------------+
*/
#5 rows in set (0.00 sec)

insert into vip (name,age,phone)values('蒲文锋',29,18989898989);
#Query OK, 1 row affected, 2 warnings (0.33 sec)

#select * from vip;
/*
+----+------+-----+-------------+---------------------+
| id | name | age | phone       | mk_time             |
+----+------+-----+-------------+---------------------+
|  1 |      |  29 | 18989898989 | 2017-09-13 18:55:11 |
+----+------+-----+-------------+---------------------+
1 row in set (0.00 sec)
*/

alter table vip modify name varchar(32) not null default '游客';
#Query OK, 1 row affected (0.52 sec)
#Records: 1  Duplicates: 0  Warnings: 0

insert into vip (phone) values ('18989876556');
#Query OK, 1 row affected (0.31 sec)

select * from vip;
/*
+----+------+-----+-------------+---------------------+
| id | name | age | phone       | mk_time             |
+----+------+-----+-------------+---------------------+
|  1 |      |  29 | 18989898989 | 2017-09-13 18:55:11 |
|  2 | 游客 |  18 | 18989876556 | 2017-09-13 19:01:02 |
+----+------+-----+-------------+---------------------+
2 rows in set (0.00 sec)
*/

update vip set name='蒲文锋' where id=1;
#Query OK, 1 row affected (0.31 sec)
#Rows matched: 1  Changed: 1  Warnings: 0

select * from vip;
/*
+----+--------+-----+-------------+---------------------+
| id | name   | age | phone       | mk_time             |
+----+--------+-----+-------------+---------------------+
|  1 | 蒲文锋 |  29 | 18989898989 | 2017-09-13 18:55:11 |
|  2 | 游客   |  18 | 18989876556 | 2017-09-13 19:01:02 |
+----+--------+-----+-------------+---------------------+
2 rows in set (0.03 sec)
*/
