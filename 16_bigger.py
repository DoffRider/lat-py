bigg = 0
print("Before:", bigg)
for itervar in [3, 41, 12, 9, 74, 15]:
    if itervar > bigg:
        bigg = itervar
    print("Loop:", itervar, bigg)
print("Biggest:", bigg)