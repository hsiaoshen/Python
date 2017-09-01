fd = open('jq.html')
fd1 = open('jq1.html','a+')

for line in fd:
    fd1.write(line)
    


fd.close()
fd1.close()