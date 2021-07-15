l=[1,2,3,4,5,6,7,8,9]
s=["one","two","three","four","five","six","seven","eight","nine"]
a=dict(zip(l,s))
user=int(input("enter numbers in numeric"))
list1=[]
list2=[]
dic={}
i=0
while i<len(l):
    if user%10==l[i]:
        a=s[i]
    if user//10==l[i]:
        b=s[i]
    n=b+a
    i+=1
    list1.append(n)
print(list1)

