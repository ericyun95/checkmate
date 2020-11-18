'''
def take_coin(coin, i, j):
    if i == j: # 1개의 코인만 남은 경우
        return coin[i]
    if i + 1 == j: # 2개의 코인이 남은 경우
        return max(coin[i], coin[j])
    left_end = coin[i] + min(take_coin(coin, i + 2, j), take_coin(coin, i + 1, j - 1))
    right_end = coin[j] + min(take_coin(coin, i + 1, j - 1), take_coin(coin, i, j - 2))
    return max(left_end, right_end)

coin_list = [30, 70, 10, 20, 60, 40] # 동전수는 반드시 짝수 개이어야
print("알콩이가 얻는 최대 금액: ", take_coin(coin_list, 0, len(coin_list) - 1))
'''


def take_coin(coinlist):
    coin_first = []
    steps = []
    for i in range(len(coinlist)-1):
        firstvalue = max(coinlist[i],coinlist[i+1])-min(coinlist[i],coinlist[i+1])
        coin_first.append([firstvalue, [coinlist[i],coinlist[i+1]]])
    steps.append(coin_first)

    for j in range(len(coinlist)-2):
        for i in range(len(coin_first) - 1):
            joined_list = coin_first[i][1] + [coin_first[i + 1][1][-1]]
            if len(joined_list) % 2 == 1:
                first_one = coin_first[i][0] - coin_first[i + 1][1][-1]
                second_one = coin_first[i + 1][0] - coin_first[i][1][0]
                joined_value = min(first_one, second_one)
                coin_first[i] = [joined_value, joined_list]
            else:
                first_one = coin_first[i][0] + coin_first[i + 1][1][-1]
                second_one = coin_first[i + 1][0] + coin_first[i][1][0]
                joined_value = max(first_one, second_one)
                coin_first[i] = [joined_value, joined_list]
        coin_first.pop(-1)
        print(coin_first)
        steps.append(coin_first)
    print(steps)
    '''
    story = []
    for i in range(10):
        if steps[-1][-1][-1] == len(coin_list):
            story.append(steps[-1][-1])
            steps.remove(steps[-1])
        else:
            story_candidates = []
            for a in steps[-1]:
                if a[-1] == story[-1][:-1] or a[-1] == story[-1][1:]:
                    story_candidates.append(a)
                    if story_candidates[-1][-1] % 2 == 1:
                        b = max(story_candidates[0][0], story_candidates[1][0])
                        for things in story_candidates:
                            if b == things[0]:
                                story.append(things[1])
                    elif story_candidates[-1][-1] % 2 == 0:
                        b = min(story_candidates[0][0], story_candidates[1][0])
                        for things in story_candidates:
                            if b == things[0]:
                                story.append(things[1])
                    steps.remove(steps[-1])
    return story
'''










"""
    return coin_first
"""
coin_list = [30, 70, 10, 20, 60, 40] # 동전수는 반드시 짝수 개이어야
take_coin(coin_list)
123456789
