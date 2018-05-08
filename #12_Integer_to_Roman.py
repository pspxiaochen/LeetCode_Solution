def intToRoman(num):
    res = ""
    dict1 = {1000:'M',500:'D',100:'C',50:'L',10:'X',5:'V',1:'I'}
    dict2 = {900:'CM',400:'CD',90:'XC',40:'XL',9:'IX',4:'IV'}
    list1 = [1000,500,100,50,10,5,1]
    list2 = [900,400,90,40,9,4,1]
    if num in dict1:
        res += dict1[num]
    elif num in dict2:
        res += dict2[num]
    else:
        for i in range(len(list1)):
            temp = num // list1[i]
            res += temp * dict1[list1[i]]
            num = num % list1[i]
            if num >= list2[i]:
                res += dict2[list2[i]]
                num -= list2[i]
    return res
