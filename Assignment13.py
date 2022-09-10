#Assignment - 13 Full Stack Web Development using Python MySirG List
#1. Write a python script to store multiple items in a single variable ( Items are “Java”,“Python”, “SQL”, “C” ) using list
l1=["Java","Python", "SQL", "C"]
print(l1)
#2. Write a python script to get the data type of a list.
l1=["Java","Python", "SQL", "C"]
print(type(l1))
#3. Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])
mylist = ["Java", "C", "Python"]
print("Last item of list=", mylist[-1])
#4. Write a python script to Change the values "SQL" and "Reactnative" with the values
#"NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]
thislist = ["Java", "SQL", "C", "Reactnative","Javascript", "Python"]
thislist[1],thislist[3]="NoSQL","Fultter"
print('list=',thislist)
#5. Write a python script to add an item to the end of the list (item “Python”. (mylist = ["Java", "SQL", "C", "Reactnative"]
mylist = ["Java", "SQL", "C", "Reactnative"]
mylist.append("Python")
print("New list is=",mylist)
#6. Write a python program to append elements from another list to the current list.(firstlist = ["Java", "Python", "SQL"]
#secondlist = ["C", "Cpp", "NoSQL"] )
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"] 

print(secondlist+firstlist)
#7. Write a python program to Print all items by referring to their index number (thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
a=[]
for e in range(len(thislist)):
    a.append(thislist[e])
print(a)
#8. Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL","C", "Reactjs", "Javascript", "Python"]
thislist = ["Java", "SQL","C", "Reactjs", "Javascript", "Python"]
thislist.sort()
print(thislist)

#9. Write a Python script to create a list of city names taken from the user.
a=input("Enter city name:-")
l1=a.split(',')
print(l1)
#10. Write a Python script to create a list, where each element of the list is a digit of a given number.
a=input("Enter number:-")
l1=[]
for e in a:
    l1.append(int(e))
print(l1,type(l1))

