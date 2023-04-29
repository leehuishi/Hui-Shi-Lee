x = [132, 100, 282, 1540, 293, 2410, 1200, 200] #order
#['100','1200','132','1540','200','2400','282','293']

y = []
for i in x:
    a = str(i)
    y.append(a)

y.sort()

z = []
for i2 in y:
    b = int(i2)
    z.append(b)

print(z)

a = ['cbd', 'hyz', 'cdc', 'fhy', 'ekl', 'aab', 'ccd', 'kil'] #order
#['aab', 'cbd','ccd','cdc','ekl','fhy','hyz','kil']
a.sort()
print(a)

#Input: s = "cbacdcbc"
#1 potential Output: "abbccccd"
#2 potential Output: "bacccbcd" 2nd round "abccbccd"
#3 potential Output: "acdb"
#Given a string of lowercase letters, make the string smallest in lexicographical order by swapping its characters.

def switchchar(stringinput):
    s = stringinput
    currentchar = s[0]
    newstring = ''
    for i in range(len(s)):
        if(i == len(s)-1):
            newstring += currentchar
            break
        else:
            nextchar = s[i+1]
        if(nextchar < currentchar):
            newstring += nextchar
            currentchar = currentchar
        elif(nextchar > currentchar):
            newstring += currentchar
            currentchar = nextchar
        else:
            newstring += currentchar
            currentchar = nextchar
    
    return newstring

x = switchchar("cbacdcbc")
y = switchchar(x)
print(y)

#Input: s = "ecbacdcbc"
#Output: "acdb"
#beforemin = ['e', 'c' , 'd']
#out put ['e','a','c','d','b']
#a c d c b c

s = "ecbacdcbc"
minchar = min(s)

posit = s.index(minchar)

beforemin = s[:posit]
aftermin = s[posit:]

newarray = []
newarray.append(aftermin[0])
aftermin = aftermin[1:]

for i in aftermin:
    if i not in newarray:
        newarray.append(i)
    else:
        continue

for i2 in beforemin:
    if i2 not in newarray:
        newarray.insert(0, i2)

y = "".join(newarray)
print (y)

#Sort numbers based on prime factorization.
#Input: N = 5, Numbers = [3, 4, 8, 9, 12, 11]
#Output: 4, 8, 12, 3, 9
def largest_pf(n):
    i = 2
    pf_array = []
    
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

num = [3, 4, 8, 9, 12, 11]
newnum = []
for i in num:
    numarray = []
    while i != 1:
        x = largest_pf(i)
        numarray.append(str(x))
        i //= x
    newnum.append(numarray)

newstr = []
for i2 in newnum:
    a = "".join(i2)
    newstr.append(a)

newdictionary = {}
for i3 in range(len(newstr)):
    newdictionary[newstr[i3]] = num[i3]

newstr.sort()

neworder = []
for i4 in newstr:
    val = newdictionary[i4]
    neworder.append(val)

print (neworder)
