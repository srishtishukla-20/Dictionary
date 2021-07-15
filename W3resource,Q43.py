a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]
dic={}
l=[]
for i in range(0,len(b)):
    dic[b[i]]=c[i]
    f= dict.fromkeys(a,dic)
print(f)
#w3 resource Q.43

a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]
dict1={}
list=[]
for i in range (0,len(b)):
    dict2={}
    dict2[b[i]]=c[i]
    dict1[a[i]]=dict2
list.append(dict1)
print(list)
#Q43.w3resource(one method)

a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]
list=[]
for key in range(len(a)):
    d={a[key]:{b[key]:c[key]}}
    list.append(d)
print(list)

#Q43.w3resource(2nd method)
