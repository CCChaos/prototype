#!/bin/sh

PROTOC=../protoc/protoc
CONFPB_DIR=../../../conf/pb_gen/pb_proto/
PROTO_DIR=../../common/protocol/
PYTHON_OUT=./py_proto/

# 删掉旧的PB文件
for dir in `ls $PYTHON_OUT` 
do
	if [ -d ${PYTHON_OUT}${dir} ]
	then
		rm ${PYTHON_OUT}${dir} -r
	fi
	
done

# 生成conf的PB文件(conf库的pb文件)
for hxx in `ls $CONFPB_DIR | grep 'hxx'`
do
	if [ -f ${CONFPB_DIR}${hxx} ]
	then
		$PROTOC -I=${PROTO_DIR} -I=../../../conf/pb_gen/pb_proto -I=../../../server-common/3rd/protobuf-2.6.1/src --python_out=${PYTHON_OUT}  ${CONFPB_DIR}${hxx}
	fi
done

# 生成common/protocol的PB文件(conf库的pb文件)
for hxx in `ls ${PROTO_DIR} | grep 'hxx'`
do
	if [ -f ${PROTO_DIR}${hxx} ]
	then
		$PROTOC -I=${PROTO_DIR} -I=../../../conf/pb_gen/pb_proto -I=../../../server-common/3rd/protobuf-2.6.1/src --python_out=${PYTHON_OUT}  ${PROTO_DIR}${hxx}
	fi
done

# 给工程添加__init__.py文件，变成Python的Package
cd ${PYTHON_OUT}
for dir in `ls`
do
	if [ -d $dir ]
	then
		cd $dir
		touch __init__.py
		cd ..
	fi
done

touch __init__.py
