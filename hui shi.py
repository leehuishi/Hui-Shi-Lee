import test as mx
a = mx.person1["age"]
print(a) #print 36 

x = mx.greeting("JJ")
print(x)

import datetime

x = datetime.datetime.now()
print(x.strftime("%a")) #Saturday