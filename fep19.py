# Square an integer, the hard way
x = -10
ans = 0
itersLeft = abs(x)
while (itersLeft != 0):
    ans = ans + abs(x)
    itersLeft = itersLeft - 1
print str(x) + '*' + str(x) + ' = '  +str(ans)
