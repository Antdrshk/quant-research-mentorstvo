""""""  		  	   		  		 			  		 			 	 	 		 		 	
"""Assess a betting strategy.  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  		 			  		 			 	 	 		 		 	
Atlanta, Georgia 30332  		  	   		  		 			  		 			 	 	 		 		 	
All Rights Reserved  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
Template code for CS 4646/7646  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  		 			  		 			 	 	 		 		 	
works, including solutions to the projects assigned in this course. Students  		  	   		  		 			  		 			 	 	 		 		 	
and other users of this template code are advised not to share it with others  		  	   		  		 			  		 			 	 	 		 		 	
or to make it available on publicly viewable websites including repositories  		  	   		  		 			  		 			 	 	 		 		 	
such as github and gitlab.  This copyright statement should not be removed  		  	   		  		 			  		 			 	 	 		 		 	
or edited.  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
We do grant permission to share solutions privately with non-students such  		  	   		  		 			  		 			 	 	 		 		 	
as potential employers. However, sharing with other current or future  		  	   		  		 			  		 			 	 	 		 		 	
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  		 			  		 			 	 	 		 		 	
GT honor code violation.  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
-----do not edit anything above this line---  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
Student Name: Anton Darashuk  		  	   		  		 			  		 			 	 	 		 		 	
GT User ID: abc123  		  	   		  		 			  		 			 	 	 		 		 	
GT ID: 900000001  		  	   		  		 			  		 			 	 	 		 		 	
"""  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
import os

import matplotlib
import numpy as np

matplotlib.use("Agg")

import matplotlib.pyplot as plt


WIN_PROB = 18 / 38
TARGET_WINNINGS = 80
SPINS_PER_EPISODE = 1000
PLOT_X_MIN = 0
PLOT_X_MAX = 300
PLOT_Y_MIN = -256
PLOT_Y_MAX = 100
  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
def author():  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    :return: The GT username of the student  		  	   		  		 			  		 			 	 	 		 		 	
    :rtype: str  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    return "abc123"  # replace tb34 with your Georgia Tech username.  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
def gtid():  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    :return: The GT ID of the student  		  	   		  		 			  		 			 	 	 		 		 	
    :rtype: int  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    return 900000001  # replace with your GT ID number  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
def get_spin_result(win_prob):  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
    :param win_prob: The probability of winning  		  	   		  		 			  		 			 	 	 		 		 	
    :type win_prob: float  		  	   		  		 			  		 			 	 	 		 		 	
    :return: The result of the spin.  		  	   		  		 			  		 			 	 	 		 		 	
    :rtype: bool  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    result = False  		  	   		  		 			  		 			 	 	 		 		 	
    if np.random.random() <= win_prob:  		  	   		  		 			  		 			 	 	 		 		 	
        result = True  		  	   		  		 			  		 			 	 	 		 		 	
    return result  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
def simulate_episode(win_prob):
    winnings = np.zeros(SPINS_PER_EPISODE + 1)
    episode_winnings = 0
    bet_amount = 1
    spin = 1

    while spin <= SPINS_PER_EPISODE and episode_winnings < TARGET_WINNINGS:
        if get_spin_result(win_prob):
            episode_winnings += bet_amount
            bet_amount = 1
        else:
            episode_winnings -= bet_amount
            bet_amount *= 2

        winnings[spin] = episode_winnings
        spin += 1

    if episode_winnings >= TARGET_WINNINGS and spin <= SPINS_PER_EPISODE:
        winnings[spin:] = TARGET_WINNINGS

    return winnings


def simulate_episodes(num_episodes, win_prob):
    all_winnings = np.zeros((num_episodes, SPINS_PER_EPISODE + 1))

    for episode in range(num_episodes):
        all_winnings[episode] = simulate_episode(win_prob)

    return all_winnings


def format_axes(ax, title):
    ax.set_title(title)
    ax.set_xlabel("Spin Number")
    ax.set_ylabel("Winnings")
    ax.set_xlim(PLOT_X_MIN, PLOT_X_MAX)
    ax.set_ylim(PLOT_Y_MIN, PLOT_Y_MAX)
    ax.legend()


def plot_figure_1(episodes, output_dir):
    x_values = np.arange(SPINS_PER_EPISODE + 1)
    fig, ax = plt.subplots()

    for episode in range(episodes.shape[0]):
        ax.plot(x_values, episodes[episode], label=f"Episode {episode + 1}")

    format_axes(ax, "Figure 1: 10 Episodes of Martingale")
    fig.savefig(os.path.join(output_dir, "figure1.png"))
    plt.close(fig)


def plot_figure_2(episodes, output_dir):
    x_values = np.arange(SPINS_PER_EPISODE + 1)
    mean_values = np.mean(episodes, axis=0)
    std_values = np.std(episodes, axis=0)
    upper_line = mean_values + std_values
    lower_line = mean_values - std_values

    fig, ax = plt.subplots()
    ax.plot(x_values, mean_values, label="Mean")
    ax.plot(x_values, upper_line, label="Mean + Std")
    ax.plot(x_values, lower_line, label="Mean - Std")

    format_axes(ax, "Figure 2: Mean Winnings Across 1000 Episodes")
    fig.savefig(os.path.join(output_dir, "figure2.png"))
    plt.close(fig)


def plot_figure_3(episodes, output_dir):
    x_values = np.arange(SPINS_PER_EPISODE + 1)
    median_values = np.median(episodes, axis=0)
    std_values = np.std(episodes, axis=0)
    upper_line = median_values + std_values
    lower_line = median_values - std_values

    fig, ax = plt.subplots()
    ax.plot(x_values, median_values, label="Median")
    ax.plot(x_values, upper_line, label="Median + Std")
    ax.plot(x_values, lower_line, label="Median - Std")

    format_axes(ax, "Figure 3: Median Winnings Across 1000 Episodes")
    fig.savefig(os.path.join(output_dir, "figure3.png"))
    plt.close(fig)


def test_code():  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    Method to test your code  		  	   		  		 			  		 			 	 	 		 		 	
    """  		  	   		  		 			  		 			 	 	 		 		 	
    np.random.seed(gtid())

    output_dir = os.path.join(os.path.dirname(__file__), "images")
    os.makedirs(output_dir, exist_ok=True)

    figure_1_episodes = simulate_episodes(10, WIN_PROB)
    figure_2_3_episodes = simulate_episodes(1000, WIN_PROB)

    plot_figure_1(figure_1_episodes, output_dir)
    plot_figure_2(figure_2_3_episodes, output_dir)
    plot_figure_3(figure_2_3_episodes, output_dir)
  		  	   		  		 			  		 			 	 	 		 		 	
  		  	   		  		 			  		 			 	 	 		 		 	
if __name__ == "__main__":  		  	   		  		 			  		 			 	 	 		 		 	
    test_code()  		  	   		  		 			  		 			 	 	 		 		 	
