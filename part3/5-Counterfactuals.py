def counterfactual_reasoning(m, p_m, mu):
    goal = 1  
    home = 1  
    opponent = 0  
    win = None  
    
    # counterfactual probability
    p_goal_given_m = [mu if m_i[0] == goal else 1 - mu for m_i in m]  
    p_home_given_m = [mu if m_i[1] == home else 1 - mu for m_i in m]  
    p_opp_given_m = [mu if m_i[2] == opponent else 1 - mu for m_i in m]  
    p_win_given_m = [mu if m_i[3] == 1 else 1 - mu for m_i in m]  
    
    # Calculating predictive probabilities
    numerator = sum([p_goal_given_m[i] * p_home_given_m[i] * p_opp_given_m[i] * p_win_given_m[i] * p_m[i] for i in range(len(m))])  
    denominator = sum([p_goal_given_m[i] * p_home_given_m[i] * p_opp_given_m[i] * p_m[i] for i in range(len(m))])  
    
    # counterfactual probability
    p_win_given_counterfactual = numerator / denominator
    
    return p_win_given_counterfactual
 
# football matches
m = [
    [0, 1, 0, 0],  # m1
    [1, 1, 1, 1],  # m2
    [1, 0, 0, 1],  # m3
    [1, 0, 1, 0]   # m4
]


p_m = [0.25, 0.25, 0.25, 0.25]


mu = 0.99


p_win_given_counterfactual = counterfactual_reasoning(m, p_m, mu)
print(f"The probability of winning the game is {p_win_given_counterfactual}。")