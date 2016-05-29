# Finger Exercise Input 10 integers and print largest odd

x = 0
count = 10
oddint = 0 

while (count != 0):
    x = int(raw_input('Enter an integer: '))
    count = count - 1
    if (x%2 != 0 and oddint < x):
        oddint = x
if (oddint == 0):
    print ('None odd int')
else:
    print ('Largest odd int', oddint )

    
        
