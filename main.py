a_list = open("list.txt").readlines()
dedupelist = list(dict.fromkeys(a_list))
cool_thing = open("final.txt","w")
cool_thing.write(str(dedupelist))