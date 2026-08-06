
outer_list = [[" ", 2, 3, 4], [2, 5, 5, 9]]
tie = [str(inner_list) for inner_list in outer_list]
spread = "".join(tie)
print(tie)
print(spread)
