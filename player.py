#coding=utf-8

import MySQLdb
from sql import ExecuteMySQL
import pb_db as PBSql
import google.protobuf.text_format as PBFormat 
import py_proto.ums_role_detail.hxx_pb2  as ums_role_detail

def GetPlayer(conf_db, role_id, filter_set = None):
	host=conf_db.get('db', 'host')
	db=conf_db.get('db', 'db')
	user=conf_db.get('db', 'user')
	passwd=conf_db.get('db', 'passwd')
	
	sql = PBSql.GetSelectSQL( ums_role_detail._UMS_ROLE_DETAIL, 'UMS_ROLE_DETAIL', 'where role_id = %d' % role_id )	

	ret = ExecuteMySQL(host, user, passwd, db, sql)
	if ret['ret'] == False or ret['count'] != 1:
		print '从数据库获取数据失败'
		return
 
	row = ret['row'][0]

	pb_role = PBSql.GetPBFromDB( ums_role_detail.UMS_ROLE_DETAIL, row, filter_set ) 
	content = PBFormat.MessageToString( pb_role )
	return content

def UpdatePlayer(conf_db, content, role_id, filter_set):
	host=conf_db.get('db', 'host')
	db=conf_db.get('db', 'db')
	user=conf_db.get('db', 'user')
	passwd=conf_db.get('db', 'passwd')

	pb = ums_role_detail.UMS_ROLE_DETAIL()
	PBFormat.Parse(content, pb )
	sql = PBSql.GetUpdateSQL( pb, 'UMS_ROLE_DETAIL', 'where role_id = %d' % role_id, filter_set )
	ret = ExecuteMySQL(host, user, passwd, db, sql )

	return ret['ret']			
