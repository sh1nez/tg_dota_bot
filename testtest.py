names_list = ['данил', 'артём', 'никита', 'влад']
print(new_names := [i[0].upper()+i[1:] for i in names_list])
