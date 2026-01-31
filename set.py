names={"rock","john","mike","smith","shawn","baker"}
names2={"rock","john","mike","smith","shawn","baker"}


print(names)  #onordered
# print(names[1])  no indexes
names.add("meg")
names.update(names2)  #avoid duplictes
print(names.pop())
print(names.remove("meg"))
li=sorted(names)
print(type(li),li)
print(names)  #onordered
