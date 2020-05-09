a_list = open("list.txt").readlines()
dedupelist = list(dict.fromkeys(a_list))
open("final.txt","w")