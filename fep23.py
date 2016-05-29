num = int(raw_input('Enter a positive integer:'))
pwr = 2
root = 1
ans= False
while pwr < 6:
    while abs(root**pwr)<=abs(num):
        if root**pwr == num:
          print 'the root is', root
          print 'the power is', pwr
          ans = True 
        root += 1
    pwr += 1
#    root = 1
if ans != True:
    print('No such pair of integer exist')
