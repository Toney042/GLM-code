from itertools import combinations   


models = {
    ("rain", "wet"): 0.25,
    ("rain", "not wet"): 0.25,
    ("not rain", "wet"): 0.25,
    ("not rain", "not wet"): 0.25
}

# Converting models to dictionaries
models = {tuple({formula if model[i] == "rain" else f"not {formula}" for i, formula in enumerate(["rain", "wet"])}): probability for model, probability in models.items()}


# Define the necessary functions

# A function to calculate the conditional probability
def calculate_conditional_probability(formula: str, formula_set: list, data: list):
    p_delta = calculate_probability(formula_set, data)
    p_alpha_and_delta = calculate_probability(formula_set + [formula], data)
    return p_alpha_and_delta / p_delta if p_delta != 0 else 0

# Functions for calculating probability
def calculate_probability(formula_set: list, data: list):
    total_probability = 0
    for model in data:
        model_probability = p_m[data.index(model)]
        for formula in formula_set:
            if model[formula] is False:
                model_probability = 0
        total_probability += model_probability
    return total_probability

# Checking whether a set of formulas implies a function of a formula
def entails_check(formula_set: list, formula: str):
    for model in data:
        model_satisfies_formula_set = all(model[formula] for formula in formula_set)
        if model_satisfies_formula_set and model[formula] is False:
            return False
    return True

# Check whether all maximal consistent subsets of a set of formulas imply a function of a formula
def all_maximal_consistent_subsets_entail_alpha(formula: str, formula_set: list, data: list):
    all_subsets = generate_all_subsets(formula_set)
    for subset in all_subsets:
        if not entails_check(subset, formula):
            return False
    return True

# A function that generates all subsets of a set
def generate_all_subsets(formula_set: list):
    all_subsets = []
    for i in range(0, len(formula_set)+1):
        all_subsets.extend(list(combinations(formula_set, i)))
    return all_subsets




def theorem_3(formula: str, formula_set: list, data: list):
    p_alpha_given_delta = calculate_conditional_probability(formula, formula_set, data)
    entails = entails_check(formula_set, formula)
    result = p_alpha_given_delta == 1 if entails else "Undefined"
    print(f"Theorem 3 Statement: Given a formula set Delta and a formula alpha, the probability of alpha given Delta is 1 if and only if Delta entails alpha. In this instance, the formula alpha is '{formula}', and the formula set Delta is {formula_set}. According to our model, the probability of alpha given Delta is {p_alpha_given_delta}. This suggests that, based on the data, it is {result} that Delta entails alpha.\n")
    return result

def theorem_4(formula: str, formula_set: list, data: list):
    p_alpha_given_delta = calculate_conditional_probability(formula, formula_set, data)
    entails = entails_check(formula_set, formula)
    result = p_alpha_given_delta == 1 if entails else "Undefined"
    print(f"Theorem 4 Statement: Given a formula set Delta and a formula alpha, the probability of alpha given Delta is 1 if and only if Delta entails alpha. In this instance, the formula alpha is '{formula}', and the formula set Delta is {formula_set}. According to our model, the probability of alpha given Delta is {p_alpha_given_delta}. This suggests that, based on the data, it is {result} that Delta entails alpha.\n")
    return result

def theorem_5(formula: str, formula_set: list, data: list):
    p_alpha_given_delta = calculate_conditional_probability(formula, formula_set, data)
    all_subsets_entail_alpha = all_maximal_consistent_subsets_entail_alpha(formula, formula_set, data)
    result = p_alpha_given_delta == 1 if all_subsets_entail_alpha else "Undefined"
    print(f"Theorem 5 Statement: Given a formula set Delta and a formula alpha, the probability of alpha given Delta is 1 if and only if all maximal consistent subsets of Delta entail alpha. In this instance, the formula alpha is '{formula}', and the formula set Delta is {formula_set}. According to our model, the probability of alpha given Delta is {p_alpha_given_delta}. This suggests that, based on the data, it is {result} that all maximal consistent subsets of Delta entail alpha.\n")
    return result



# Define a function to get all maximal consistent subsets
def get_maximal_consistent_subsets(delta, models):
    # Starting with all subsets
    subsets = [frozenset(subset) for i in range(1, len(delta) + 1) for subset in combinations(delta, i)]
    
    # Filter out inconsistent subsets
    consistent_subsets = [subset for subset in subsets if all(formula in model for formula in models for subset in subsets for model in models)]
    
    # Filter out subsets that are not the largest
    maximal_consistent_subsets = [subset for subset in consistent_subsets if not any(other_subset > subset for other_subset in consistent_subsets)]
    
    return maximal_consistent_subsets



data = [
    {"model": "model1", "rain": True, "wet": True, "not rain": False, "rain -> wet": True, "not wet": False},
    {"model": "model2", "rain": True, "wet": False, "not rain": False, "rain -> wet": False, "not wet": True},
    {"model": "model3", "rain": False, "wet": True, "not rain": True, "rain -> wet": True, "not wet": False},
    {"model": "model4", "rain": False, "wet": False, "not rain": True, "rain -> wet": True, "not wet": True},
]

p_m = [0.25, 0.25, 0.25, 0.25]  


theorem3_result = theorem_3("rain", ["rain", "wet"], data)
theorem4_result = theorem_4("rain", ["rain", "wet", "not rain"], data)
theorem5_result = theorem_5("rain", ["rain", "wet", "rain -> wet", "not wet"], data)



theorem3_statement = """
Theorem 3 states: Given a set of formulas, Delta, and a formula, alpha, the probability of alpha given Delta is 1 if and only if Delta entails alpha.
In this example, the formula alpha is "{}", and the set of formulas Delta is {}.
According to our model, the probability that alpha is true given Delta is {}.
This suggests that, according to the data, it is {} that Delta implies alpha.
"""

theorem4_statement = """
Theorem 4 states: Given a set of formulas, Delta, and a formula, alpha, the probability of alpha given Delta is 1 if and only if Delta entails alpha.
In this example, the formula alpha is "{}", and the set of formulas Delta is {}.
According to our model, the probability that alpha is true given Delta is {}.
This suggests that, according to the data, it is {} that Delta implies alpha.
"""

theorem5_statement = """
Theorem 5 states: Given a set of formulas, Delta, and a formula, alpha, the probability of alpha given Delta is 1 if and only if for all maximal consistent subsets, Delta', of Delta, Delta' entails alpha.
In this example, the formula alpha is "{}", and the set of formulas Delta is {}.
According to our model, the probability that alpha is true given Delta is {}.
This suggests that, according to the data, it is {} that for all maximal consistent subsets of Delta, the subset implies alpha.
"""


# Print the theorems' results
print(theorem3_statement.format("rain", ["rain", "wet"], theorem3_result, "true" if theorem3_result == 1 else "not necessarily true"))
print(theorem4_statement.format("rain", ["rain", "wet", "not rain"], theorem4_result, "true" if theorem4_result == 1 else "not necessarily true"))
print(theorem5_statement.format("rain", ["rain", "wet", "rain -> wet", "not wet"], theorem5_result, "true" if theorem5_result == 1 else "not necessarily true"))
