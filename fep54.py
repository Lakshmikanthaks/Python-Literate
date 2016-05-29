nameHandle = open('kids', 'a')
nameHandle.write('Lakshmi')
nameHandle.write('kantha\n')
nameHandle.close()
nameHandle = open('kids', 'r')
for line in nameHandle:
    print line[:-1]
nameHandle.close()
