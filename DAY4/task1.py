contacts={"ruthu":1234,"rithin":4321,"rithu":1324}
print(contacts)
contacts["rithu"]=5678#updating
print(contacts)
contacts["sanjana"]=6543 
print(contacts)
print(contacts.get("rithin"))#accessing
print(contacts.get("sam"))#accessing
for name in contacts.keys():
    phone = contacts[name]