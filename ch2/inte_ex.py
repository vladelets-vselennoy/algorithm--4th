# INSERTION-SORT
def ch_data(a,t):
    if not isinstance(a,t):
        print(f"operation can be performed only on {t} not on any other data type")
        raise TypeError
def insertion_sort(a):   
    if not isinstance(a,list):
        print("Only list is allowed not any other data type")
        return
    l=len(a)
    i=0
    j=0
    for i in range(1,l):
        j=i-1
        key=a[i]
        while(a[j]>key and j>=0 ):
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
    return(a) 
def func_call (f):
    li=eval(input("enter list"))
    print(f"before sorting {li}")   # we had printed it because value of li will also be sorted some like concept of array in C that at same memory value get changed
    k=f(li)
    print(f" after sorting {k}")  

# Q 2.1-3 
# Monotonically decreasing INSERTION SORT
def mo_dec_insertion(a):
    try:
        ch_data(a,list)
    except TypeError:
        return
    l=len(a)
    j=1
    i=1
    li=a
    for i in range(1,l):
        j=i-1
        key=a[i]
        while(j>=0 and a[j]<key):
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
    return li # here we had used li which was copy of a list to show that copy of list also get changed if we perform any operation on the original list

# func_call(mo_dec_insertion)
# Q 2.1-4
# linear searching
def linear_search(a,e):
    try:
        ch_data(a,list)
    except TypeError:
        return
    for i in range(0,len(a)):
        if e==a[i]:
            print(f"{i+1} is index") # here i+1 is done because question is considering index from 1 
            return
    print("sorry , not found")
linear_search(eval(input("list")),int(input("element")))
    
    