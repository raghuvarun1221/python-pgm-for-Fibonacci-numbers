fibo_series = [0, 1]

def fibonacci(n):
	if n<=len(fibo_series) and n>0:
		return fibo_series[n-1]
	else:
		fn = fibonacci(n-1) + fibonacci(n-2)
		if n>len(fibo_series):
			fibo_series.append(fn)
		return fn

n = int(input('Enter a number, N, N>=2 : '))

fibonacci(n)

print(fibo_series)
