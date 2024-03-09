import numpy as np

models = {
    "model_1": np.array([1, 0]),
    "model_2": np.array([1, 1]),
    "model_3": np.array([0, 1]),
}

beliefs = {
    "model_1": 0.5,
    "model_2": 0.3,
    "model_3": 0.2, 
}


def implies(model_1, model_2):
    """
    Determine whether model 1 implies model 2.
    """
    return np.all(models[model_1] <= models[model_2])  

def p_alpha_given_delta(alpha, delta):
    """
    Calculate the probability of model alpha given model delta.
    """
    if not implies(delta, alpha):  
        return 0
    return beliefs[delta] / sum(belief for model, belief in beliefs.items() if implies(model, alpha))  # 计算概率


def test_theorem_1(alpha, delta):
    p = p_alpha_given_delta(alpha, delta)  
    if p == 1:  
        print(f"Given the model '{delta}', the model '{alpha}' is implied with probability 1.")
    else:  
        print(f"Given the model '{delta}', the model '{alpha}' is not necessarily implied. The probability is {p}.")


def test_theorem_2(alpha, delta):
    p = p_alpha_given_delta(alpha, delta)  
    if p == 1:  
        print(f"Given the model '{delta}' (which is an empty set), the model '{alpha}' is implied with probability 1.")
    else:  
        print(f"Given the model '{delta}' (which is an empty set), the model '{alpha}' is not necessarily implied. The probability is {p}.")


# Define a new model "model_0", representing an empty set.
models["model_0"] = np.array([0, 0])
beliefs["model_0"] = 0.1  # Suppose we believe the model to be true with a probability of 10 per cent


test_theorem_1("model_2", "model_1")  # Given the model 'model_1', the model 'model_2' is not necessarily implied. The probability is 0.5.
test_theorem_1("model_3", "model_1")  # Given the model 'model_1', the model 'model_3' is not necessarily implied. The probability is 0.
test_theorem_2("model_2", "model_0")  # Given the model 'model_0' (which is an empty set), the model 'model_2' is not necessarily implied. The probability is 0.0.
test_theorem_2("model_3", "model_0")  # Given the model 'model_0' (which is an empty set), the model 'model_3' is not necessarily implied. The probability is 0.0.