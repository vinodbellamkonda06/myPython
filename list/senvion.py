num_list = [4, 5, 6]
sub_setlist = []

for i in num_list:
    for j in num_list:
        if i == j:
            sub_setlist.append({i})
        else:
            if {i, j} not in sub_setlist:
                sub_setlist.append({i, j})
sub_setlist.extend([set(num_list), {}])
print(sub_setlist)
print(len(sub_setlist))
