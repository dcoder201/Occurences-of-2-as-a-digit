
def numberOf2sinRange(n):
    #add code here
  c=0
  s=0
  for i in range(n+1):
    if '2' in str(i):
       s=str(i).count('2')
       c+=s
  return(c)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        print(numberOf2sinRange(n))
# } Driver Code Ends
