def func(lt=[]):
    if type(lt).__name__!='list' and type(lt).__name__!='tuple':
        return
    if type(lt).__name__=='tuple':
        lt=list(lt)
    if len(lt)<=1:
        return
    else:
        for i in range(1,len(lt)):
            for j in range(len(lt)-i):
                if lt[j]>lt[j+1]:
                    tmp=lt[j]
                    lt[j]=lt[j+1]
                    lt[j+1]=tmp
    return lt

lt=[32,12,3,27,6,9,1]
tp=(2,6,1,9,4)
print func(lt)
print func(tp)
