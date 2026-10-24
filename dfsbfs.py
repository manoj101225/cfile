# def dfs(graph,start,visited=None):
#     if visited is None:
#         visited=set()
#     visited.add(start)
#     print(start)
#     for n in graph[start]:
#         if n not in visited:
#             dfs(graph,n,visited)
# dfs({'A':['B','C'],'B':['D'],'C':['E'],'D':[],'E':[]},'A')
# print()
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# from collections import deque
# def bfs(graph,start):
#     visited=set([start])
#     queue=deque([start])
#     while queue:
#         node=queue.popleft()
#         print(node)
#         for n in graph[node]:
#             if n not in visited:
#                 visited.add(n)
#                 queue.append(n)
        
# print(bfs({'A':['B','C'],'B':['D'],'C':['E'],'D':[],'E':[]},'A'))
# import sys
# input=sys.stdin.readline
# def hashmap(arr):

#     seen={}
#     for i in arr:
#         if i not in seen:
#             seen[i]=[i]
#         else:
#             seen[i].append(i)
#     return seen
# data=list(map(int,input().strip().split(",")))
# print(hashmap(data))


# def countsubarray(arr,k):
#     n=len(arr)
#     dp=[-1]*k+1
#     def dfs(i,currsum):
#         if i==n:
#             return 1 if currsum==k else 0
#         take=dfs(i+1,currsum+arr[i])
#         nottake=dfs(i+1,currsum)
#         return take + nottake
#     return dfs(0,0)
# print(countsubarray([1,2,2,3],3))

# def countpartition(arr,diff):
#     n=len(arr)
#     res=[]
#     path=[]
#     def dfs(i):
#         if i==n:
#             res.append(path[:])
#             return
#         path.append(arr[i])
#         dfs(i+1)
#         path.pop()
#         dfs(i+1)
#     dfs(0)
#     count=0
#     total=sum(arr)
#     for sub in res:
#         s1=sum(sub)
#         s2=total-s1
#         if abs(s1-s2)==diff:
#             count+=1
#     return count//2

# print(countpartition([1,1,2,3],1))

# def lcs(s1,s2):
#     m=len(s1)
#     n=len(s2)
#     dp=[[0]*(n+1) for _ in range(m+1)]
#     for i in range(1,m+1):
#         for j in range(1,n+1):
#             if s1[i-1]==s2[j-1]:
#                 dp[i][j]=dp[i-1][j-1]+1
#             else:
#                 dp[i][j]=max(dp[i-1][j],dp[i][j-1])
#     lcs=[]
#     i,j=m,n
#     while i>0 and j>0:
#         if s1[i-1]==s2[j-1]:
#             lcs.append(s1[i-1])
#             i-=1
#             j-=1
#         else:
#             if dp[i-1][j]>dp[i][j-1]:
#                 i-=1
#             else:
#                 j-=1
#     return ''.join(reversed(lcs))
# print(lcs("abcd","bdef"))

# def lcs(s1,s2):
#     m=len(s1)
#     n=len(s2)
#     def dfs(i,j):
#         if i==m or j==n:
#             return 0
#         if s1[i]==s2[j]:
#             return 1+dfs(i+1,j+1)
#         else:
#             return max(dfs(i+1,j),dfs(i,j+1))
#     return dfs(0,0)
# print(lcs("abcd","bdef"))
# def longestPalindromeSubseq(s):
#     n=len(s)
#     def dfs(i):
#         if i>=n:
#             return 0
#         max_len=1
#         for j in range(i+1,n):
#             if s[i]==s[j]:
#                 max_len=max(max_len,2+dfs(j+1))
#         return max_len
#     return dfs(0)
# print(longestPalindromeSubseq("cbbd"))


# from functools import lru_cache


# def mininsertions(s):
#     n=len(s)

#     @lru_cache(None)
#     def dfs(i,j):
#         if i>=j:
#             return 0
#         if s[i]==s[j]:
#             return dfs(i+1,j-1)
#         else:
#             return 1+min(dfs(i+1,j),dfs(i,j-1))
#     return dfs(0,n-1)
# print(mininsertions("leetcode"))


# class Solution:
#     def minInsertions(self, s: str) -> int:
#         n=len(s)
#         dp=[[-1]*n for _ in range(n)]
#         def dfs(i,j):
#             if i>=j:
#                 return 0
#             if dp[i][j]!=-1:
#                 return dp[i][j]
#             if s[i]==s[j]:
#                 dp[i][j]=dfs(i+1,j-1)
#             else:
#                 dp[i][j]=1+min(dfs(i+1,j),dfs(i,j-1))
#             return dp[i][j]
#         return dfs(0,n-1)
# print(Solution().minInsertions("leetcode"))

# def shortestcommonsupersequence(s1,s2):
#     m=len(s1)
#     n=len(s2)
#     dp=[[0]*(n+1) for _ in range(m+1)]
#     for i in range(1,m+1):
#         for j in range(1,n+1):
#             if s1[i-1]==s2[j-1]:
#                 dp[i][j]=dp[i-1][j-1]+1
#             else:
#                 dp[i][j]=max(dp[i-1][j],dp[i][j-1])
#     lcs=[]
#     i,j=0,0
#     while i<m and j<n:
#         if s1[i]==s2[j]:
#             lcs.append(s1[i])
#             i+=1
#             j+=1
#         else:
#             if dp[i+1][j]>dp[i][j+1]:
#                 lcs.append(s1[i])
#                 i+=1
#             else:
#                 lcs.append(s2[j])
#                 j+=1
#     lcs.extend(s1[i:])
#     lcs.extend(s2[j:])
#     return ''.join(lcs)
# print(shortestcommonsupersequence("abac","cab"))


# def meetinthemiddle(arr,k):
#     n=len(arr)
#     res=[]
#     path=[]
#     def dfs(i):
#         if i==n:
#             res.append(path[:])
#             return
#         path.append(arr[i])
#         dfs(i+1)
#         path.pop()
#         dfs(i+1)
#     dfs(0)
#     count=0
#     for sub in res:
#         if sum(sub)==k:
#             count+=1
#     return count
# print(meetinthemiddle([1,2,3,4],5))

# def lis(arr):
#     n=len(arr)
#     dp=[-1]*n
#     def dfs(i):
#         if i==n:
#             return 0
#         if dp[i]!=-1:
#             return dp[i]
#         max_len=1
#         for j in range(i+1,n):
#             if arr[j]>arr[i]:
#                 max_len=max(max_len,1+dfs(j))
#         dp[i]=max_len
#         return dp[i]
#     return max(dfs(i) for i in range(n))
# print(lis([10,9,2,5,3,7,101,18]))


# def lis(arr):
#     n=len(arr)
#     dp=[1]*n
#     ans=[]
#     for i in range(n):
#         for j in range(i):
#             if arr[i]>arr[j]:
#                 dp[i]=max(dp[i],dp[j]+1)
#     max_len=max(dp)
#     for i in range(n-1,-1,-1):
#         if dp[i]==max_len:
#             ans.append(arr[i])
#             max_len-=1
#     return ans
# print(lis([10,9,2,5,3,7,101,18]))

# def largestdivisiblesubset(arr):
#     n=len(arr)
#     arr.sort()
#     dp=[1]*n
#     ans=[]
#     for i in range(n):
#         for j in range(i):
#             if arr[i]%arr[j]==0:
#                 dp[i]=max(dp[i],dp[j]+1)
#     max_len=max(dp)
#     for i in range(n-1,-1,-1):
#         if dp[i]==max_len:
#             ans.append(arr[i])
#             max_len-=1
#     return ans
# print(largestdivisiblesubset([2,3,4,8]))

# def longestvalidparentheses(s):
#     stack=[-1]
#     max_len=0
#     for i,c in enumerate(s):
#         if c=='(':
#             stack.append(i)
#         else:
#             stack.pop()
#             if not stack:
#                 stack.append(i)
#             else:
#                 max_len=max(max_len,i-stack[-1])
#     return max_len
# print(longestvalidparentheses("(()())"))

# def countsquares(arr):
#     n=len(arr)
#     dp=[[0]*n for _ in range(n)]
#     count=0
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j]==1:
#                 if i==0 or j==0:
#                     dp[i][j]=1
#                 else:
#                     dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
#                 count+=dp[i][j]
#     return count
# print(countsquares([[1,0,1],[1,1,0],[1,1,0]]))

def maxsumafterpartitioning(arr,k):
    n=len(arr)
    dp=[0]*(n+1)
    for i in range(1,n+1):
        max_val=0
        for j in range(1,min(i,k)+1):
            max_val=max(max_val,arr[i-j])
            dp[i]=max(dp[i],dp[i-j]+max_val*j)
    return dp[n]
print(maxsumafterpartitioning([1,15,7,9,2,5,10],3))