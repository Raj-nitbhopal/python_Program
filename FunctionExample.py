n = 37737.5746
print(abs(n))
print(round(n))

Value = ["Rajan", 89, 0, -88, None]
print(all(Value))

print(any(Value))
print(bin(4))
print(bin(9))

#bin()
m = 67
print(bin(m))
#bool
print(bool(0))
print(bool(-4.5))
print(bool(None))
print(bool("False"))
#bytearray()
print(bytearray())
print(bytearray('Python', 'utf-8'))
#compile()
myCode = 'a = 7\nb=9\nresult=a*b\nprint("result =",result)'
codeObject = compile(myCode, 'resultstring', 'exec')
exec(codeObject)
#list()
print(list()) #returns empty list
stringobj = 'PALINDROME'
print(list(stringobj))
tupleobj = ('a', 'e', 'i', 'o', 'u')
print(list(tupleobj))
listobj = ['1', '2', '3', 'o', '10u']
print(list(listobj))
#len()
stringobj = 'PALINDROME'
print(len(stringobj))
tupleobj = ('a', 'e', 'i', 'o', 'u')
print(len(tupleobj))
listobj = ['1', '2', '3', 'o', '10u']
print(len(listobj))
#max()
num = [11, 13, 12, 15, 14]
print('Maximum is:', max(num))
#min()
sampleObj = ['B', 'a', 't', 'A']
print(min(sampleObj))
print(max(sampleObj))
#pow
print(pow(2, -3))
print(pow(2, 4.5))
print(pow(3, 0))
#oct
print("The octal representation of 32 is " + oct(32))
print("The octal representation of the ascii value of 'A' is " + oct(ord('A')))
print("The octal representation of the binary of 32 is " + oct(100000))
print("The octal representation of the binaryof 23 is " + oct(0x17))
#sorted
sampleObj = (3, 6, 8, 2, 5, 8, 10)
print(sorted(sampleObj, reverse=True))
sampledict = {'a': 'sss', 'g': 'wq', 't': 2}
print(sorted(sampledict, key=len))

#sum()
num = [2.5, 3, 4, -5]
numSum = sum(num)
print(numSum)
numSum = sum(num, 20)
print(numSum)

def myFun():
    return 5
res = myFun
print(callable(res)) #function is called to get this value
num1 = 15 * 5
print(callable(num1))#no function is called
