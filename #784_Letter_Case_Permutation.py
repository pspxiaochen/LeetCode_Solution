import collections
def letterCasePermutation(S):
    queue = collections.deque()
    if len(S) == 0:
        return queue
    else:
        queue.append(S)
    for i in range(len(S)):
        if S[i].isdigit():
            continue
        else:
            for j in range(len(queue)):
                s = queue.popleft()
                if s[i].isalpha():
                    queue.append(s[:i] + s[i].upper() + s[i+1:])
                    queue.append(s[:i] + s[i].lower() + s[i+1:])
    return list(queue)
