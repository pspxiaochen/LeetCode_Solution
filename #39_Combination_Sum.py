def combinationSum(candidates, target):
    res = []
    temp = []
    candidates = sorted(candidates)
    dfs(candidates, res, temp, target, 0)
    return res


def dfs(candidates, res, temp, target, idx):
    if target == 0:
        res.append(temp.copy())
    elif target < 0:
        return
    else:
        for i in range(idx, len(candidates)):
            if target < candidates[i]:
                return
            temp.append(candidates[i])
            dfs(candidates, res, temp, target - candidates[i], i)
            temp.pop(len(temp) - 1)

print(combinationSum([2,3,5],8))

