# def find_sum(n):
#     sum=0;
#     for i in n:
#         print(i)
#         sum +=i;
#     return sum;


# num=[3,4,5,6,7,89,2,2,3,4,4]    
# print(find_sum(num))
def find_sum(n):
    sum=0;
    for i in range(1,n+1):
        sum +=i;
    return sum;





# recursion

def find_sum_recursion(n):
    if n==1:
        return 1;
    return n+find_sum_recursion(n-1)
   
def fibo(n):
    if n==0 or n==1:
        return n;
    return fibo(n-1) + fibo(n-2)


def fibo_series(n):
    list_of_fibo_series=[]
    for i in range(n):
        list_of_fibo_series.append(fibo(i))
    return list_of_fibo_series



print(find_sum(5))
print(find_sum(10))
print(fibo(10))
print(fibo_series(11))


