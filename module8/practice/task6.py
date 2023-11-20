def solve_riddle(riddle, word_length, start_letter, reverse=False):
    if reverse:
        riddle = riddle[::-1]
       
    idx = riddle.find(start_letter)
    return riddle[idx:word_length+idx]
print(solve_riddle('mi1rewopret',5, 'p', reverse=True))
print(solve_riddle('KaripowerMo',5, 'p'))
