#-*- coding: utf-8 -*-
for i in range(1,10):
    row = ""
    for j in range(1,i):
        row += "\t\t"
    for k in range(i,10):
        row +="{}*{}={}\t".format(i,k,i*k)
    print row
