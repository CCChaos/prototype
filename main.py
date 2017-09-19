#coding=utf-8

import os
import sys
sys.path.append(os.path.abspath('./py_proto'))

import getopt
import ConfigParser
import player	

def usage():
	print 'python op.py --role_id=value --select or --update --file=value [-o:-c:]'

def init_err(msg):
	print msg
	usage()

if __name__ == '__main__':
	
	opt_out_file=''
	opt_config_file='config.ini'
	opt_role_id = None
	opt_oper=None # 1-获取数据  2-更新数据
	opt_file=None
	opt_filter=set()
	opts, args = getopt.getopt(sys.argv[1:], 'c:o:', ['role_id=','select','update','file=','filter='])
	

	for op,value in opts:
		if op == '-c':
			opt_config_file = value
		if op == '-o':
			opt_out_file = value
		if op == '--role_id':
			opt_role_id = int(value)
		if op == '--file':
			opt_file = value
		if op == '--filter':
			opt_filter.add(value)
		if op == '--select':
			opt_oper = 1
		if op == '--update':
			opt_oper = 2	

	if not os.path.exists(opt_config_file):
		init_err('配置文件config.ini不存在')
		exit()
	if opt_oper is None:
		init_err('没有操作类型, --select or -- update')
		exit()
	if opt_role_id is None:
		init_err('没有role_id,指定 --role_id=value')
		exit() 

	if opt_out_file == '':
		opt_out_file='./data/role_%d' % opt_role_id

	config = ConfigParser.ConfigParser()
	config.read(opt_config_file)

	if opt_oper == 1: # select player
		text_role = player.GetPlayer(config, opt_role_id, opt_filter)
		if text_role is None:
			print '没有数据'
			exit()
		utf8_text = text_role.encode('utf-8')
		f = open(opt_out_file,'w')
		f.write(utf8_text)
		f.close()	
	elif opt_oper == 2: # update player
		if opt_file is None:
			init_err('没有输入文件')
			exit()
		f = open(opt_file, 'r')
		content = f.read()
		f.close()
		content = content.decode('utf-8')
		ret = player.UpdatePlayer(config, content, opt_role_id, opt_filter)
		if ret == True:
			print('完成')
		else:
			print('失败')
	else:
		init_err('未知操作, --select or --update')	
	
	#pb_role = player.GetPlayer(config, 2)
	#content = PBFormat.MessageToString(pb_role)
	#f = open('role_2.json', 'w')
	#f.write(content)
	#f.close()
	#f = open('role_2.json','r')
	#content = f.read()
	#pb = ums_role_detail.UMS_ROLE_DETAIL()
	#PBFormat.Parse(content, pb )
	#print pb
