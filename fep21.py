# Find the cube root of a perfect cube

x = int(raw_input('Enter and integer: '))
ans = 0
while ans**3 < abs(x):
#    print 'Value of the decrementing function abs(x) - ans**3 is', abs(x) - ans**3 
    ans = ans + 1 
if ans**3 != abs(x):
        print x, 'is not a perfect cube'
else:
        if x < 0:
            ans = -ans
        print 'Cube root of', x, 'is', ans
        
    
        
