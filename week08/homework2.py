def newmap(func,likelist):
    
    if hasattr(likelist,'__iter__'):
        for i in likelist:
            func(i)
    else:
        print("something is wrong.")


def f(i):
    print("you will late")
    print(i)

newmap(f,range(3))
''' 
you will late
0
you will late
1
you will late
2
PS E:\pythoncode202005>
'''