#coding=utf-8

import MySQLdb

def ExecuteMySQL(host, user, passwd, db, sql):
	ret = {'ret':True, 'count':0, 'row':None}
	conn = MySQLdb.connect(host=host, user=user, db=db, passwd=passwd)
	try:
		cursor = conn.cursor()
		count = cursor.execute(sql)
		allrow = cursor.fetchall()
		conn.commit()
		ret['ret'] = True
		ret['count'] = count
		ret['row'] = allrow
	except Exception:
		ret['ret'] = False
	finally:
		conn.close()
		return ret	
