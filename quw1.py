arr=[100,101,100,102,101,100]
count=0
dict={}
for i in arr:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1

print(dict)