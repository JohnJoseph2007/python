#User function Template for python3

class Solution:
    def minimumAttacks(self, X, K):
        count = 1
        add = 2
        while K>X:
            X+=add
            count+=1
            add+=2
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        X,K=map(int, input().split())
        ob=Solution()
        print(ob.minimumAttacks(X,K))

# } Driver Code Ends