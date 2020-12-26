import random, time, threading
l1 = ['_' for _ in range(20)]
l2 = ['__' for _ in range(20)]
l3 = ['___' for _ in range(20)]
l4 = ['_' for _ in range(7)] + [' ' for _ in range(6)] + ['_' for _ in range(7)]
l5 = ['__' for _ in range(5)] + ['  ' for _ in range(3)] + ['__' for _ in range(4)] + ['  ' for _ in range(3)] + ['__' for _ in range(5)]
l6 = ['___' for _ in range(3)] + ['   ' for _ in range(2)] + ['___' for _ in range(3)] + ['   ' for _ in range(2)] + ['___' for _ in range(3)] + ['   ' for _ in range(2)] + ['___' for _ in range(5)]
decider = [l1, l2, l3, l4, l5, l6]
angle = 0
slash = '/'
k = 0
depth = 0
shit1 = l1
shit2 = l2
flag = 0
jump = 0
game = 0
score = 0
flips = 0
max_flip = 0
chasm = 0
print("""RULES

Gameplay :

i) Press enter once to jump!

ii) Press enter multiple times to backflip.(8 times for a complete backflip)


Scoring : 

i) Distance : 5 X (The distance covered by Slash)

ii) Backflips : More the number of backflips performed by you, more your score.
  For successive backflips, score increases exponentially!


Game Over :

i) If Slash falls into a chasm.

ii) If he lands on his head or lands flat while performing a flip. (Remember Slash is a very symmetrical character, so often it's difficult to distinguish between his head and feet while performing a somersault.)
                                                                    
Press enter to continue!(After each game preferably restart the terminal.)                                                                    
      """)
input()

def show():
    global slash
    global angle
    global jump
    if angle % 360 == 0 or angle % 360 == 180:
        slash = '/'
    elif angle % 360 == 45 or angle % 360 == 225:
        slash = '|'
    elif angle % 360 == 90 or angle % 360 == 270:
        slash = '\\'
    else:
        slash = ' __'
    print(slash)
    
def gameplay():
    global flag
    global angle
    while True:
        input()
        angle += 45
        if flag == 0:
            flag = 1
threading.Thread(target=gameplay).start()
while game != 1:
    x = depth % 20
    if x == 0:
        shit1 = shit2
        shit2 = decider[random.randint(0, 5)]
    display = shit1[x:] + shit2[:x]
    k = 0
    for i in range(20):
        if i == 9:
            print(k * ' ' + display[i], end='')
            if flag == 1:
                jump = k + len(display[i]) + 1
                flag = 2
            elif flag == 2:
                jump += 1
                flag += 1
            elif flag == 3:
                jump += 1
                flag += 1
            elif flag == 4:
                jump -= 1
            if jump - k > 0:
                print((jump - k) * ' ', end='')
            else:
                jump = 0
                flag = 0
                flip = angle // 360
                score += 100 * (2 ** flip - 1)
                flips += flip
                if flip > max_flip:
                    max_flip = flip
                if angle % 360 == 0 or angle % 360 == 315 or angle % 360 == 45:
                    slash = '/'
                    angle = 0
                else:
                    game = 1
            show()
            if flag == 0:
                if display[i][-1] == ' ':
                    game = 1
            k += len(display[i])
        else:
            print(k * ' ' + display[i])
            k += len(display[i])   
    depth += 1
    time.sleep(0.2)
print("""_____________________________
GAME OVER!
distance : {} x 5
flips : {}
maximum successive flips : {}
flip bonus : {}
_______________________________
SCORE : {}
""".format(depth, flips, max_flip, score, score + 5 * depth))