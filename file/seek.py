#coding=utf-8

# 占位,比如下载视频资源(1024B),会占位

fd = open('朦胧夜色', 'w+')

fd.write('\0')
fd.seek(1024)
fd.write('\0')

fd.close()