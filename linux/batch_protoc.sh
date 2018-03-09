PACKAGE=protobuf
CONFIG=debug

SRC_ROOT="/home/www/newproto"
PROTO_ROOT="/home/www/build"

mkdir -p "$PROTO_ROOT"

find "$SRC_ROOT" -name \*.proto |\
 xargs "/home/www/protocl/bin/protoc"\
   --proto_path "$SRC_ROOT"\
   --python_out="$PROTO_ROOT"
