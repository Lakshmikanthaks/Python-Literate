x = 50
y = 05
z = 50

if x%2 != 0 and y%2 != 0 and z%2 != 0:
    if x > y and x > z:
        print 'x is highest'
    if x == y and y == z: 
            print 'x, y and z are highest'
    elif x == y:
            print 'x and y are highest'
    elif x == z:
            print 'x and z are highest' 
    elif y == z:
        print 'y and z are highest'
    elif y > z:
        print 'y is highest'
    elif y < z:
        print 'Z is highest'
    else:
        print 'All are equal' 

elif x%2 != 0 and y%2 != 0 and z%2 == 0:
    if x > y:
        print 'x is highest'
    elif y > x:
        print 'y is highest'
    else:
        print 'x and y are highest'

elif x%2 != 0 and y%2 == 0 and z%2 == 0:
    print 'x is highest'
        
elif x%2 != 0 and y%2 == 0 and z%2 != 0:
    if x > z:
        print 'x is highest'
    elif z > x:
        print 'z is highest'
    else:
        print 'x and z are highest'

elif x%2 == 0 and y%2 == 0 and z%2 != 0:
    print 'z is highest'
        
elif x%2 == 0 and y%2 != 0 and z%2 != 0:
    if y > z:
        print 'y is highest'
    elif z > y:
        print 'z is highest'
    else:
        print 'y and z are highest' 

elif x%2 == 0 and y%2 != 0 and z%2 == 0:
    print 'y is highest'

else:
    print 'None are odd' 



##if x > y and x > z and x%2 != 0:
##    print 'x is highest'
##elif y > z and y%2 != 0:
##    print 'y is highest'
##elif y < z and z%2 ==0:
##    print 'y is highest'
##elif z%2 != 0:
##    print 'z is highest'
##else:
##    print ' none is odd' 



##if x%2 != 0 or y%2 != 0 or z%2 != 0:
##    if x%2 != 0 and y%2 != 0 and z%2 != 0:
##        if x < y and x < z:
##            print 'x is least'
##        elif y < z:
##            print 'y is lease'
##        elif y > z:
##            print 'Z is least'
##        
##    if x%2 != 0 and y%2 != 0 and z%2 == 0:
##        if x < y and x < z:
##            print 'x is least'
##        elif y < z:
##                print 'y is lease'
##    elif x%2 != 0 and y%2 == 0 and z%2 != 0:
##        if x < y and x < z:
##            print 'x is least'
##        else:
##            print 'z is least'
##    elif x%2 == 0 and y%2 != 0 and z%2 != 0:
##        if y < z:
##            print 'y is lease'
##        else:
##            print 'z is least'    
##else:
##    print 'None odd numbers' 
