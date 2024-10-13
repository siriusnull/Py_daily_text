# scissors,rock,paper
import sys, random

win = 0
loss = 0
ties = 0

while True:
    print(' win: %s\n loss: %s \n ties: %s\n q to stop' % (win, loss, ties))
    while True:
        PlayerMove = input()
        if PlayerMove == 'q':
            sys.exit()
        if PlayerMove == 'r' or PlayerMove == 's' or PlayerMove == 'p':
            break

    if PlayerMove == 's':
        print('scissors versus....', end=' ')
    elif PlayerMove == 'r':
        print('rock versus...', end=' ')
    elif PlayerMove == 'p':
        print('paper versus...', end=' ')

    RandomNum = random.randint(1, 3)
    if RandomNum == 1:
        ComputerMove = 'r'
        print('rock')
    elif RandomNum == 2:
        ComputerMove = 's'
        print('scissors')
    elif RandomNum == 3:
        ComputerMove = 'p'
        print('paper')

    # 统计结果
    if ComputerMove == PlayerMove:
        print('ties')
        ties = ties + 1
    elif PlayerMove == 's' and ComputerMove == 'r':
        print('computer win')
        loss = loss + 1
    elif PlayerMove == 's' and ComputerMove == 'p':
        print('player win ')
        win = win + 1
    elif PlayerMove == 'r' and ComputerMove == 'p':
        print('computer win')
        loss = loss + 1
    elif PlayerMove == 'r' and ComputerMove == 's':
        print('player win ')
        win = win + 1
    elif PlayerMove == 'p' and ComputerMove == 's':
        print('computer win')
        loss = loss + 1
    elif PlayerMove == 'p' and ComputerMove == 'r':
        print('player win ')
        win = win + 1