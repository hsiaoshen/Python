# 向流中输出

with open('file.text','w+') as fd:
#    缩进原则一定要遵循
#    版本2
#    print>>fd,'hello world'
#    版本3
     print('hello',file=fd)