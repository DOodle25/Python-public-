def SackKnap(W, wt, val, n): 
	dp = [0 for i in range(W+1)] 
	for i in range(1, n+1): 
		for w in range(W, 0, -1): 
			if wt[i-1] <= w: 
				dp[w] = max(dp[w], dp[w-wt[i-1]]+val[i-1]) 
	return dp[W]

def backtrackindpSackKnap(w, wt, val, n):
	#pass
	

if __name__ == '__main__': 
	profit = [60, 100, 120, 20] 
	weight = [10, 20, 30, 10] 
	W = 70
	n = len(profit) 
	print(SackKnap(W, weight, profit, n)) 