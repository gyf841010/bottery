pid=`ps aux | grep "python" | grep "server.py" | fgrep -f ports | awk '{print $2}'`
[ -z $pid ]|| kill -9 $pid
python server.py -port=20005 -log_file_prefix=logs/20005 1>/dev/null 2>/dev/null&

