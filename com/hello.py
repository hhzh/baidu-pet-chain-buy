import datetime
import pymysql

# now = datetime.datetime.now()
#
# print(now)
# print(type(now))
# print(str(now)+'\taaa')

# for i in range(1, 5):
#     print(i)

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='SCMD_2017_scmd', db='pets',
                       charset='utf8')
cursor = conn.cursor()
sql = 'insert into pets(genId) ' \
      'values (%s)'
cursor.execute(sql, (1))
conn.commit()
conn.close()
