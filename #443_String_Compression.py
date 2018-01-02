def compress(chars):
    start = 0
    count = 0
    for end in range(len(chars)):
        count += 1
        if end == len(chars)-1 or chars[end] != chars[end+1]:
            chars[start] = chars[end]
            start += 1
            if count > 1:
                for i in str(count):
                    chars[start] = i
                    start += 1
            count = 0
    return start



