import random
import matplotlib.pyplot as plt

def monty_hall_simulation(num_simulation=100000):
    win_if_switch = 0
    win_if_stay = 0

    for _ in range(num_simulation):
        # randomly place the pearl under one of the three seashells
        seashells = [0,0,0]
        pearl_position = random.randint(0,2)
        seashells[pearl_position] = 1

        #player makes an initial choice
        contestant_choice = random.randint(0,2)

        remaining_seashells = [i for i in range(3) if i != contestant_choice and seashells[i] == 0]
        host_reveal = random.choice(remaining_seashells)

        switch_choice = [i for i in range(3) if i != contestant_choice and i != host_reveal][0]

        if seashells[switch_choice] == 1:
            win_if_switch += 1
        if seashells[contestant_choice] == 1:
            win_if_stay += 1
    
    strategies = ['switch','stay']
    win_counts = [win_if_switch, win_if_stay]

    plt.figure(figsize=(8,5))
    bars = plt.bar(strategies, win_counts, color=['green','blue'])
    plt.xlabel('strategy')
    plt.ylabel('number of wins')
    plt.title('Monty Hall Simulation: Number of wins by strategy')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval}', ha='center', va='bottom')

    plt.show()

#run simulation
monty_hall_simulation()