a_list = open("list.txt").readlines()
dedupelist = list(dict.fromkeys(a_list))
cool_thing = open("final.txt", "w+")
for x in cool_thing:
    x = x.replace("\n", "")
cool_thing.write(str(x))
