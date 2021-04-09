def fibonacci(n):
    if(0<n<=1):
      return n
    else:

       n_minus2,n_minus1=0,1
       result=None

       for i in range(n-1):
          result=n_minus2+n_minus1
          n_minus2=n_minus1
          n_minus1=result

       return result

n=int(input("enter a number to print the nth fibonacci : "))
print(fibonacci(n))