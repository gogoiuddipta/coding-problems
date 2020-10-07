#return the length of longest common subsequence from a set of two strings, P and Q.
#The substring from which the subsequence is derived, need not be comprised of contigious charachters.
#Steps:
#We consider two scenarios:
#  Case1: When both P and Q end with the same character.
#        a. We add 1 to the result.
#        b. We return LCS(P1,Q1) excluding the last characters from both P and Q.
#  Case2: When P and Q don't end with the same character.
#        a. We exclude the last character of P, and compare P1 with Q, LCS(P1,Q). Store the result in temp1.
#        b. Similarly, we exclude the last character of Q, and compare Q1 with P, LCS(P,Q1). Store the result in temp2.
#        c. Compare temp1 and temp2. Return the larger value as the result.
 
class give_LCS:
  # lcs_string=""

  def LCS(self,P,Q,n,m):
    cache={}
    
    if (n,m) in cache:
      return cache[n,m]
    else:
      if n==0 or m==0:
        result=0
      elif P[n-1]==Q[m-1]:
        result=1+self.LCS(P,Q,n-1,m-1)
      else:
        temp1=self.LCS(P,Q,n-1,m)
        temp2=self.LCS(P,Q,n,m-1)
        result=max(temp1,temp2)

      cache[n,m]=result    
      return result

P="BATD"
Q="ABACD"

required_LCS=give_LCS()
res_len=required_LCS.LCS(P,Q,len(P),len(Q))
print("Length of LCS: "+str(res_len))       
