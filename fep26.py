x = int(raw_input('Enter an Integer: '))
epsilon = 0.01
step = epsilon**2
numGuess = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    numGuess += 1
print 'numGuess =' , numGuess
if abs(ans**2 - x) >= epsilon:
    print 'Failed on square root of', x
else:
    print ans, 'is close to square root of', x 
