def findRestaurant(list1,list2):
    rank = 99999
    for i in range(len(list1)):
        if list1[i] in list2:
            temp = i + list2.index(list1[i])
            if temp < rank:
                output = []
                rank = temp
                output.append(list1[i])
            elif temp == rank:
                output.append(list1[i])
    return output
