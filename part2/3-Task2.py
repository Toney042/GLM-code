class SimplifiedGenerativeLogicModel:
    def __init__(self, data, model, mu):
        self.data = data  
        self.model = model  
        self.mu = mu  
        self.K = len(data)  

    def p_D(self, d_k):
        return 1 / self.K  

    def p_M_given_D(self, d_k, m_n):
        if self.model == self.data[d_k]:  
            return 1  
        else:
            return 0  

    def p_alpha_given_M(self, alpha):
        if alpha == self.model:  
            return self.mu  
        else:
            return 1 - self.mu  

    def p_alpha_given_data(self, alpha):
        sum_numerator = 0  
        sum_denominator = 0  
        for d_k in range(self.K):
            p_M_given_d_k = self.p_M_given_D(d_k, self.model)  
            p_d_k = self.p_D(d_k)  
            p_alpha_given_M = self.p_alpha_given_M(alpha)  
            sum_numerator += p_alpha_given_M * p_M_given_d_k * p_d_k  
            sum_denominator += p_M_given_d_k * p_d_k  
        return sum_numerator / sum_denominator if sum_denominator != 0 else 0  

# Rerun the model using the function p_alpha_given_M
data = [0, 1]  
model = 0  
mu = 0.6  
glm = SimplifiedGenerativeLogicModel(data, model, mu)  
alpha = 0  
glm.p_alpha_given_M(alpha)  

# alpha=0
print("alpha=0：")
for model in [0, 1]:
    glm = SimplifiedGenerativeLogicModel(data, model, mu)
    print(f"p(alpha=0 | M={model}) = {glm.p_alpha_given_M(0)}")  

# alpha=1
print("alpha=1：")
for model in [0, 1]:
    glm = SimplifiedGenerativeLogicModel(data, model, mu)
    print(f"p(alpha=1 | M={model}) = {glm.p_alpha_given_M(1)}")  

    
