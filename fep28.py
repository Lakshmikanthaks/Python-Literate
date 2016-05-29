x = abs(int(raw_input('Enter an integer:')))
epsilon = 0.01
numGuess = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon:
    print 'low =', low, 'high =', high, 'ans =', ans
    numGuess += 1
    if ans**3 < x: 
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print 'numGuess =', numGuess
print ans, 'is close to cube root of', x 
