from random import randint

nm_array=[]

for x in xrange(3):
    sub_array = []
    for i in range(3):
        sub_array.append(randint(1,10))
    nm_array.append(sub_array)


a,b,c,d,e,f,g,h,i = nm_array[0][0],nm_array[0][1],nm_array[0][2],nm_array[1][0],nm_array[1][1],nm_array[1][2],nm_array[2][0],nm_array[2][1],nm_array[2][2]

print nm_array
if e >= b and e>=d and e >= h and e >= f:
    print e, " passed"
if b >= a and b >= c and b >= e:
    print b, " paased"
if h >= g and h >= i and h >= e:
    print h, " passed"
if d >= a and d >= g and d >= e:
    print d, " passed"
if f >= c and f >= i and f >= e:
    print f, " passed"
if a >= b and a >= d:
    print a, " passed"
if c >= b and c >= f:
    print c, " passed"
if g >= d and g >= h:
    print g, " passed"