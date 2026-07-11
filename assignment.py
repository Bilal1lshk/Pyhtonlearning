#list question#1
list=["islamabad","karachi","faislabad","Rahimyarkhan","gujranwala"]
list.append("lahore")
list[2]="islamabad"
list.pop(3)
print(list,len(list))

#question#2

tuple1=("pink","blue","green","purple","white")
tuple1=list(tuple1)
tuple1.append("black")
x=tuple(tuple1)
a, b, c, d, e, f = tuple1
print(a, b, c, d, e, f)
ans=list(tuple1)
print(ans)
#question#3
set1={10,20,30,40}
set2={30,40,50,60}
set1.add(70)
set1.discard(20)
set2.pop()
set3=set1.union(set2)
print(set3)
print(set1)
print(set2)
#question#4
dictioary = {
    "fullname":"bilal",
    "department":"ai",
    "rollno":"33083012"

}
dictioary["semster"]="3"
dictioary.pop("semster")
print("fullname" in dictioary)
print(dictioary["department"])
print(dictioary.items())
#question#5
list=[1,2,3,45,5]
tuple1=tuple(list)
set1=set(tuple1)
print(len(set1))
set.clear()

