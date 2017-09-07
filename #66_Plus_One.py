<<<<<<< HEAD
def plusOne_1(digits):
    sum = 0
    for i in range(len(digits)):
        sum += digits[i] * (10**(len(digits)-i-1))
    return [int(i) for i in str(sum+1)]

def plusOne_2(digits):
    for i in range(len(digits)-1,-1,-1):
        if(digits[i]<9):
            digits[i] += 1
            return digits
        else:
            digits[i]=0
    digits.insert(0,1)
    return digits

=======
def plusOne_1(digits):
    sum = 0
    for i in range(len(digits)):
        sum += digits[i] * (10**(len(digits)-i-1))
    return [int(i) for i in str(sum+1)]

def plusOne_2(digits):
    for i in range(len(digits)-1,-1,-1):
        if(digits[i]<9):
            digits[i] += 1
            return digits
        else:
            digits[i]=0
    digits.insert(0,1)
    return digits

>>>>>>> f591eb1c08fb1fdb158d747d63451b73e2f00dbd
print(plusOne_2([9,9,9,9,9]))