# INSERTION-SORT
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
    print(f"before sorting {li}")
    k=f(li)
    print(f"b \t\t\t\t\t\t after sorting {k}")
func_call(insertion_sort)