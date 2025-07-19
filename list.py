mylist = ["ram", "shyam","monu", "sita", "gita"]
mylist[1] = "hello"
mylist[-2] = "hello"
mylist.append("new item")
mylist.insert(2, "inserted item")
mylist.remove("monu")
mylist.sort() #['gita', 'hello', 'hello', 'inserted item', 'new item', 'ram']
mylist.reverse() #['ram', 'new item', 'inserted item', 'hello', 'hello', 'gita']
mylist.pop() #removes last item and returns it
mylist.pop(2) #removes item at index 2 and returns it
mylist.clear() #removes all items from the list
print(mylist)