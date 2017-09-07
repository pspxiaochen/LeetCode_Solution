<<<<<<< HEAD
def strStr(haystack, needle):
    for i in range(len(haystack) - len(needle)+1):
        if(haystack[i:i+len(needle)] == needle):
            return i
    return -1
=======
def strStr(haystack, needle):
    for i in range(len(haystack) - len(needle)+1):
        if(haystack[i:i+len(needle)] == needle):
            return i
    return -1
>>>>>>> f591eb1c08fb1fdb158d747d63451b73e2f00dbd
