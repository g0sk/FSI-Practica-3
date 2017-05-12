import random
import numpy as np
import matplotlib.pyplot as plt


# Environment size
width = 5
height = 16

# Actions
num_actions = 4

actions_list = {"UP": 0,
                "RIGHT": 1,
                "DOWN": 2,
                "LEFT": 3
                }
diccionario = {
                0 : "UP",
                1 : "RIGHT",
                2 : "DOWN",
                3 :  "LEFT"

}

actions_vectors = {"UP": (-1, 0),
                   "RIGHT": (0, 1),
                   "DOWN": (1, 0),
                   "LEFT": (0, -1)
                   }

# Discount factor
discount = 0.8

Q = np.zeros((height * width, num_actions))  # Q matrix
Rewards = np.zeros(height * width)  # Reward matrix, it is stored in one dimension


def getState(y, x):
    return y * width + x


def getStateCoord(state):
    return int(state / width), int(state % width)


def getActions(state):
    y, x = getStateCoord(state)
    actions = []
    if x < width - 1:
        actions.append("RIGHT")
    if x > 0:
        actions.append("LEFT")
    if y < height - 1:
        actions.append("DOWN")
    if y > 0:
        actions.append("UP")
    return actions


def getRndAction(state):
    return random.choice(getActions(state))


def getRndState():
    return random.randint(0, height * width - 1)


Rewards[4 * width + 3] = -10000
Rewards[4 * width + 2] = -10000
Rewards[4 * width + 1] = -10000
Rewards[4 * width + 0] = -10000

Rewards[9 * width + 4] = -10000
Rewards[9 * width + 3] = -10000
Rewards[9 * width + 2] = -10000
Rewards[9 * width + 1] = -10000

Rewards[3 * width + 3] = 100
final_state = getState(3, 3)

print np.reshape(Rewards, (height, width))


def qlearning(s1, a, s2):
    Q[s1][a] = Rewards[s2] + discount * max(Q[s2])
    return


# Episodes
media = 0
for i in xrange(100):

    state = getRndState()
    while state != final_state:
        action = getRndAction(state)
        y = getStateCoord(state)[0] + actions_vectors[action][0]
        x = getStateCoord(state)[1] + actions_vectors[action][1]
        new_state = getState(y, x)
        qlearning(state, actions_list[action], new_state)
        state = new_state
        media = media + 1

print Q
print "la media es " , media/100
Q = np.zeros((height * width, num_actions))
# Q matrix plot

#greedy
media = 0
for i in xrange(100):
    state = getRndState()
    while state != final_state:
        media = media + 1
        if max(Q[state]) > 0:
            value = np.argmax(Q[state])
            """ if value == 0:
                mov = "UP"
            if value == 1:
                mov = "RIGHT"
            if value == 2:
                mov = "DOWN"
            if value == 3:
                mov = "LEFT" """
            mov =  diccionario [value]

        else:
            mov = getRndAction(state)

        y = getStateCoord(state)[0] + actions_vectors[mov][0]
        x = getStateCoord(state)[1] + actions_vectors[mov][1]
        new_state = getState(y, x)
        qlearning(state, actions_list[mov], new_state)
        state = new_state


print Q
print "El promedio de explotacion es", media/100, "\n"
Q = np.zeros((height * width, num_actions))

#greedy
media = 0
for i in xrange(100):
    state = getRndState()
    while state != final_state:
        media = media + 1
        aleat = random.random()
        if(aleat < 0.8):
            #print aleat
            if max(Q[state]) > 0:
                value = np.argmax(Q[state])
                """ if value == 0:
                    mov = "UP"
                if value == 1:
                    mov = "RIGHT"
                if value == 2:
                    mov = "DOWN"
                if value == 3:
                    mov = "LEFT" """
                mov =  diccionario [value]

            else:
                mov = getRndAction(state)
        else:
            mov= getRndAction(state)

        y = getStateCoord(state)[0] + actions_vectors[mov][0]
        x = getStateCoord(state)[1] + actions_vectors[mov][1]
        new_state = getState(y, x)
        qlearning(state, actions_list[mov], new_state)
        state = new_state


print Q
print "El promedio de e-greedy es", media/100, "\n"


s = 0
ax = plt.axes()
ax.axis([-1, width + 1, -1, height + 1])

for j in xrange(height):

    plt.plot([0, width], [j, j], 'b')
    for i in xrange(width):
        plt.plot([i, i], [0, height], 'b')

        direction = np.argmax(Q[s])
        if s != final_state:
            if direction == 0:
                ax.arrow(i + 0.5, 0.75 + j, 0, -0.35, head_width=0.08, head_length=0.08, fc='k', ec='k')
            if direction == 1:
                ax.arrow(0.25 + i, j + 0.5, 0.35, 0., head_width=0.08, head_length=0.08, fc='k', ec='k')
            if direction == 2:
                ax.arrow(i + 0.5, 0.25 + j, 0, 0.35, head_width=0.08, head_length=0.08, fc='k', ec='k')
            if direction == 3:
                ax.arrow(0.75 + i, j + 0.5, -0.35, 0., head_width=0.08, head_length=0.08, fc='k', ec='k')
        s += 1

    plt.plot([i+1, i+1], [0, height], 'b')
    plt.plot([0, width], [j+1, j+1], 'b')

plt.show()
