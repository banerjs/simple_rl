#!/usr/bin/env python

# Python imports.
import sys

# Other imports.
import srl_example_setup
from simple_rl.agents import QLearningAgent, RandomAgent, LinearQAgent, DQNAgent
from simple_rl.tasks import TaxiOOMDP
from simple_rl.run_experiments import run_agents_on_mdp, run_single_agent_on_mdp

def main(open_plot=True, viz=True):
    # Taxi initial state attributes..
    # agent = {"x":1, "y":1, "has_passenger":0}
    # passengers = [{"x":3, "y":2, "dest_x":2, "dest_y":3, "in_taxi":0}]
    # walls = []
    # mdp = TaxiOOMDP(width=4, height=4, agent=agent, walls=walls, passengers=passengers)
    # agent = {"x":6, "y":10, "has_passenger":0}
    # passengers = [{"x":2, "y":2, "dest_x":10, "dest_y":10, "in_taxi":0}]
    # walls = [
    #     {"x": 1, "y": 1}, {"x": 2, "y": 1}, {"x": 3, "y": 1}, {"x": 4, "y": 1}, {"x": 5, "y": 1}, {"x": 6, "y": 1}, {"x": 7, "y": 1}, {"x": 8, "y": 1}, {"x": 9, "y": 1}, {"x": 10, "y": 1}, {"x": 11, "y": 1},
    #     {"x": 1, "y": 2}, {"x": 1, "y": 3}, {"x": 1, "y": 4}, {"x": 1, "y": 5}, {"x": 1, "y": 6}, {"x": 1, "y": 7}, {"x": 1, "y": 8}, {"x": 1, "y": 9}, {"x": 1, "y": 10}, {"x": 1, "y": 11},
    #     {"x": 11, "y": 2}, {"x": 11, "y": 3}, {"x": 11, "y": 4}, {"x": 11, "y": 5}, {"x": 11, "y": 6}, {"x": 11, "y": 7}, {"x": 11, "y": 8}, {"x": 11, "y": 9}, {"x": 11, "y": 10}, {"x": 11, "y": 11},
    #     {"x": 2, "y": 11}, {"x": 3, "y": 11}, {"x": 4, "y": 11}, {"x": 5, "y": 11}, {"x": 6, "y": 11}, {"x": 7, "y": 11}, {"x": 8, "y": 11}, {"x": 9, "y": 11}, {"x": 10, "y": 11},
    #     {"x": 3, "y": 2}, {"x": 3, "y": 3}, {"x": 3, "y": 4}, {"x": 3, "y": 5},
    #     {"x": 7, "y": 2}, {"x": 7, "y": 3}, {"x": 7, "y": 4}, {"x": 7, "y": 5},
    #     {"x": 5, "y": 7}, {"x": 5, "y": 8}, {"x": 5, "y": 9}, {"x": 5, "y": 10},
    # ]
    # mdp = TaxiOOMDP(width=11, height=11, agent=agent, walls=walls, passengers=passengers)
    agent = {"x":5, "y":6, "has_passenger":0}
    passengers = [{"x":2, "y":2, "dest_x":6, "dest_y":6, "in_taxi":0}]
    walls = [
        {"x": 1, "y": 1}, {"x": 2, "y": 1}, {"x": 3, "y": 1}, {"x": 4, "y": 1}, {"x": 5, "y": 1}, {"x": 6, "y": 1}, {"x": 7, "y": 1},
        {"x": 1, "y": 2}, {"x": 1, "y": 3}, {"x": 1, "y": 4}, {"x": 1, "y": 5}, {"x": 1, "y": 6}, {"x": 1, "y": 7},
        {"x": 7, "y": 2}, {"x": 7, "y": 3}, {"x": 7, "y": 4}, {"x": 7, "y": 5}, {"x": 7, "y": 6}, {"x": 7, "y": 7},
        {"x": 2, "y": 7}, {"x": 3, "y": 7}, {"x": 4, "y": 7}, {"x": 5, "y": 7}, {"x": 6, "y": 7},
        {"x": 3, "y": 2}, {"x": 3, "y": 3},
        {"x": 4, "y": 5}, {"x": 4, "y": 6},
        {"x": 5, "y": 2}, {"x": 5, "y": 3},
    ]
    mdp = TaxiOOMDP(width=7, height=7, agent=agent, walls=walls, passengers=passengers)

    # Agents.
    ql_agent = QLearningAgent(actions=mdp.get_actions())
    rand_agent = RandomAgent(actions=mdp.get_actions())
    linear_ql_agent = LinearQAgent(actions=mdp.get_actions(), num_features=mdp.get_num_state_feats())
    dqn_agent = DQNAgent(actions=mdp.get_actions(), x_dim=mdp.get_num_state_feats(), y_dim=1, num_channels=1)

    if viz:
        # Visualize Taxi.
        run_single_agent_on_mdp(dqn_agent, mdp, episodes=100, steps=1000)
        mdp.visualize_agent(dqn_agent)
    else:
        # Run experiment and make plot.
        run_agents_on_mdp([dqn_agent, linear_ql_agent, ql_agent, rand_agent], mdp, instances=3, episodes=100, steps=1000, reset_at_terminal=True, open_plot=open_plot)

if __name__ == "__main__":
    main(open_plot=("no_plot" not in sys.argv), viz=("viz" in sys.argv))
