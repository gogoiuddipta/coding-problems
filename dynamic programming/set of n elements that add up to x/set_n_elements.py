#program to find the number of set of n elements that add upto x
#Steps:
# There are two methods:
#   method 1:  returns the number of sets, method 2:  contains the recursive cases
# In the recursive case, we compare x with the array element i is pointing to:
#    case1:  x<ar[i]:
#            result= move to the next element
#    case2: x>=ar[i]:
#            a. move to the next element
#            b. consider element ar[i], subtract the value of ar[i] from x and move to the next element
#            result= a+b



class set_number:
  #method to return the number of sets
  def sets_dp(self,ar,total):
    cache={}
    i=len(ar)-1
    return self.dp(ar,total,i,cache)

  #method containing the recursive cases
  def dp(self,ar,total,i,cache):
    key=str(total)+":"+str(i)
    if key in cache:
      return cache[key]
    else:
      #base case
      if total==0:
        return 1
      elif i<0:
        return 0
      elif total<0:
        return 0
      else:
        #recursive case
        if total<ar[i]:
          result=self.dp(ar,total,i-1,cache)
        else:
          result=self.dp(ar,total,i-1,cache)+self.dp(ar,total-ar[i],i-1,cache)
        cache[key]=result
        return result        

ar=[2,4,6,10]     #given array containing n elements
req_total=16      #given value of x
set_op=set_number()
output=set_op.sets_dp(ar,req_total)
print("The numer of sets of n elements that equals to "+str(req_total)+" are: "+str(output))

