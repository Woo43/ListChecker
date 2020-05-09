cool_thing = open("final.txt","w+")
cool_thing.write("")
print("cool thing:")
print(cool_thing)
a_list = open("list.txt").readlines()
print("a list:")
print(a_list)
for i in a_list: 
    if i not in cool_thing: 
        cool_thing.write(i) 
        print(i)