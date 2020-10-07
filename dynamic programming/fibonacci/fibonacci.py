#Given a number n, provide the fibonnaci sereis value upto n
#use cache(dictionary) to strore the memoization values
#when the value for a particular n is in cache, return cache[n]
#if n is not in cache, carry return the recursive method

class fibonnaci:
  def fib(self,n):
    cache={}
    if n in cache:
      return cache[n]
    else:
      if n<2:
        return n
      
      answer=self.fib(n-1)+self.fib(n-2)
      cache[n]=answer
      return cache[n]

fibo=fibonnaci()
  
while(1):
  n=int(input("enter n:"))
  result=fibo.fib(n)
  print(str(result))
