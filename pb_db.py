#coding=utf-8

import  MySQLdb

def GetSelectSQL(pb_descriptor, table_name, where_limit):
	sql = '' 
	for key in pb_descriptor.fields_by_name.iterkeys():
		if sql == '':
			sql = 'select %s' % key
		else:
			sql = "%s, %s" % (sql,key)
	sql = '%s from %s' % (sql, table_name)
	if where_limit == None:
		sql = '%s;' % sql
	else:
		sql = '%s %s;' % (sql, where_limit)
	return sql 

def GetUpdateSQL(pb, table_name, where_limit, filter_set = None):
	sql = ''
	for (field, value) in pb._fields.iteritems():
		if not filter_set is None:
			if not field.name in filter_set:
				continue

		setsql = ''
		if( field.cpp_type == 10 ): #CPPTYPE_MESSAGE
			setsql = "%s = '%s'" % ( field.name, MySQLdb.MySQL.escape_string(value.SerializeToString()))
		else:
			setsql = '%s = %s' % (field.name, value)

		if sql == '':
			sql = 'update %s set %s' % ( table_name, setsql )
		else:
			sql = '%s, %s' % (sql, setsql)
	sql = '%s %s;' % ( sql, where_limit )
	return sql 

def GetPBFromDB(pb_class, row, filter_set = None):
	pb = pb_class()
	i = 0
	for (field_name, descriptor) in pb_class.DESCRIPTOR.fields_by_name.iteritems():
		data = row[i]
		i = i + 1
		if not filter_set is None:
			if not field_name in filter_set:
				continue
		if data == None:
			continue
		if( descriptor.cpp_type == 10 ): #CPPTYPE_MESSAGE 
			pb.__getattribute__(field_name).ParseFromString(data)
		else:
			pb.__setattr__(field_name, data)
	return pb
