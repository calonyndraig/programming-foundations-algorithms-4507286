# Example file for Programming Foundations: Algorithms by Joe Marini
# determine if a list is sorted


items1 = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]
items2 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def is_sorted(itemlist):
    # TODO: using the brute force method
    # for i in range(1,len(itemlist)):
    #     if itemlist[i] < items1[i-1]:
    #         return False
    # return True

    return all(itemlist[i] <= itemlist[i+1] for i in range(len(itemlist)-1))

print(is_sorted(items1))
print(is_sorted(items2))

