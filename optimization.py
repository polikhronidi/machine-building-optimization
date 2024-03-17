import numpy as np
from scipy.optimize import minimize

def objective_function(x, weights):
    """
    Objective function incorporating technical, economic, and environmental costs.

    Parameters:
    - x: array of variables
    - weights: array of weights for technical, economic, and environmental costs

    Returns:
    - Weighted sum of costs
    """
    technical_cost = x[0] ** 2 + x[1] ** 2
    economic_cost = 2 * x[0] + 3 * x[1]
    environmental_cost = 4 * x[0] + 5 * x[1]
    return weights[0] * technical_cost + weights[1] * economic_cost + weights[2] * environmental_cost

def constraint1(x):
    """
    Technical constraint: sum of variables <= 10

    Parameters:
    - x: array of variables

    Returns:
    - Constraint value
    """
    return x[0] + x[1] - 10

def constraint2(x):
    """
    Environmental constraint: 2*Variable1 + Variable2 <= 15

    Parameters:
    - x: array of variables

    Returns:
    - Constraint value
    """
    return 2*x[0] + x[1] - 15

def optimize():
    """
    Perform optimization based on user inputs.
    """
    print("Enter weights for each category (technical, economic, environmental):")
    weights = [float(input("Technical: ")), float(input("Economic: ")), float(input("Environmental: "))]
    
    print("Enter initial variable values:")
    x0 = [float(input("Variable 1: ")), float(input("Variable 2: "))]
    
    bounds = ((0, None), (0, None))
    con1 = {'type': 'ineq', 'fun': constraint1}
    con2 = {'type': 'ineq', 'fun': constraint2}
    constraints = [con1, con2]
    
    result = minimize(objective_function, x0, args=(weights,), bounds=bounds, constraints=constraints)
    
    print("\nOptimal variable values:", result.x)
    print("Minimum function value:", result.fun)

if __name__ == "__main__":
    optimize()
