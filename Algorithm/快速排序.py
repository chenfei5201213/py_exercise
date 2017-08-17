def func(lt):
    lt = list(lt)
    if len(lt)<=1:
        return lt
    key=lt[0]
    lt_l=[]
    lt_r=[]
    lt_m=[]
    for i in lt:
        if i<key:
            lt_l.append(i)
        elif i>key:
            lt_r.append(i)
        else:
            lt_m.append(i)

    lt_l=func(lt_l)
    lt_r=func(lt_r)
    return lt_l+lt_m+lt_r

lt=[12,34,2,5,8,1,9]
print func(lt)
