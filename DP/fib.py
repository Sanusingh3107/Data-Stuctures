def fib(n):
    dp=[None]*(n+1)
    if dp[n] is not None:
        return dp[n]
    
    if n <= 1:
        return n
    
    dp[n] = fib(n-1) + fib(n-2)

    return dp[n]
n=7
print(fib(n))