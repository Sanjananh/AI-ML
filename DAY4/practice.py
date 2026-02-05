student ={
    "name":"sanjana",
    "age": 20,
    "course": "python"
}
print(student["name"])#accessing 
student["age"]=21#updating
print(student["age"])
student.pop("course")#removing
print(student)
print(student.keys())
print(student.values())
print(len(student))
#sets
colors={"red","green","blue"}
colors.add("yellow")
print(colors)
colors.remove("green")
print(colors)
a={1,2,3}
b={3,4,5}
print(a|b)
print(a&b)
print(a-b)
