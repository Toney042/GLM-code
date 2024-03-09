'''
    1. 10 samples
'''

# Initialisation data
data = [
    {"bird": 0, "fly": 0, "count": 5},
    {"bird": 0, "fly": 1, "count": 2},
    {"bird": 1, "fly": 0, "count": 1},
    {"bird": 1, "fly": 1, "count": 3}
]

def calculate_probability(data):
    """
    Calculate the probability that "bird" means "fly" given the data.
    """
    total_count = sum(item["count"] for item in data)  
    bird_implies_fly_count = sum(item["count"] for item in data if item["bird"] == 1 and item["fly"] == 1)  
    return bird_implies_fly_count / total_count  
 

p_k = calculate_probability(data)
print(f"p_k = {p_k}")   


'''
    2. Add new data, 11th sample
'''

new_data = {"bird": 1, "fly": 0, "count": 1}
data.append(new_data)


p_k_plus_1 = calculate_probability(data)
print(f"p_k_plus_1 = {p_k_plus_1}")   # p_k_plus_1 = 0.25
