cool_thing = open("final.txt","w+")
cool_thing.write("")
a_list = open("list.txt").readlines()
for i in a_list: 
    if i not in cool_thing: 
        cool_thing.write(i) 