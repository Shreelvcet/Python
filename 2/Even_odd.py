a=int(input("Enter The number: "))
if(a%2==0):
    print("The Number is Even")
else:
    print("The Number is Odd")

b=int(input("Enter The number: "))
c=int(input("Enter The number: "))
d=int(input("Enter The number: "))
if(b>c & c>d):
    print("Biggest Number is ",b)
elif(c>b & b>d):
    print("Biggest Number is ",c)
else:
    print("Biggest Number is ",d)

print("Output 'for loop': ")
for i in range (11):
    print(i)