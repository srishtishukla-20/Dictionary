a={1:"risha",3:"rampi",2:"tom"}
list=sorted(a.keys())
dict={}
i=0
while i<len(list):
    dict[list[i]]=a[list[i]]
    i+=1
print(dict)

