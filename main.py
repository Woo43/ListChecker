a_list = open("list.txt").readlines()
dedupelist = list(dict.fromkeys(a_list))
print(dedupelist)
cool_thing = open("final.txt", "w+")
y = [x.replace('\n', '') for x in dedupelist]
cool_thing.write(str(y))
