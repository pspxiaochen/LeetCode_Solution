def judgeCircle(moves):
    dict= {'U':0,'D':0,'L':0,'R':0}
    for i in moves:
        dict[i] = dict[i] + 1
    return dict['U'] == dict['D'] and dict['L'] == dict['R']

def judgeCircle_2(moves):
    return moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L')