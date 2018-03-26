import table as T
import random

#建立插入对象
i = T.sns_sseinfo.insert()

arr=['abc','bcd','cde','def']#随机获取数组元素
list = dict(time='2017-10-10',ask=random.choice(arr),
    anwser=random.choice(arr),dm=random.randint(1,100))
print(i)

#执行操作
r = T.conn.execute(i,list)

#影响的行数
print(r.rowcount)

#返回主键ID
print(r.inserted_primary_key)

#表中的字段Column
print(T.sns_sseinfo.c)
s = T.select([T.sns_sseinfo])
print(s)
#自定义查询字段
s = T.select([T.sns_sseinfo.c.id,T.sns_sseinfo.c.ask])
r = T.conn.execute(s)
print(r)                            #这里输出的是一个对象 ResultProxy
print(r.rowcount)                   #得到的行数
# print(r.fetchall())               #fetchall 使用后，会自动关闭查询对象ResultProxy
allnum = r.fetchall()
for item in allnum:           #fetchall 元祖的方式获取
    print(item[0],item[1])

#插入测试数据
# the_one = random.choice(allnum)
# the_two = random.choice(allnum)
# arr=[{'info_id':the_one[0],'name':the_one[1]},
#     {'info_id':the_two[0],'name':the_two[1]}]
#一次插入多条数据
# i = T.sns_id.insert()
# r = T.conn.execute(i,arr)

#查询条件,orderby,limit的使用
s = T.select([T.sns_sseinfo]).where(T.sns_sseinfo.c.id>10).order_by(T.sns_sseinfo.c.id.desc()).limit(2).offset(5)
r = T.conn.execute(s)
items = r.fetchall()
for item in items:
    print(item[0],item[1])

#查询两个表
s = T.select([T.sns_sseinfo,T.sns_id]).where(T.sns_sseinfo.c.id==T.sns_id.c.info_id)
r = T.conn.execute(s)
items = r.fetchall()
for item in items:
    print(item[0],item[1])

#修改 update
s = T.sns_sseinfo.update().where(T.sns_sseinfo.c.id<3).values(ask='哈哈')
r = T.conn.execute(s)
print(r.rowcount)

#删除 delete  table.delete（） 清空数据
s = T.sns_sseinfo.delete().where(T.sns_sseinfo.c.id==6)
r = T.conn.execute(s)
print(r.rowcount)
T.conn.close()