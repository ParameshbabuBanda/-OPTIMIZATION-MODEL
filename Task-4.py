####TASK 4 -  OPTIMIZATION  MODEL

from pulp import LpMaximize, LpProblem, LpVariable  # PuLP components
 
 # Create a linear programming problem to maximize profit
model = LpProblem(name="maximize-profit", sense=LpMaximize)

 # Decision variables for products A and B
A = LpVariable(name="A", lowBound=0, cat='Integer')
B = LpVariable(name="B", lowBound=0, cat='Integer')
 
 # Objective function: Maximize 20A + 30B
model += 20 * A + 30 * B, "Profit"

# Constraints
model += 2 * A + 4 * B <= 100, "Material Constraint"  # Material limit
model += A + 2 * B <= 40, "Labor Constraint"  # Labor limit
 
 # Solve the problem
model.solve()
 
# Output the results
print(f"Optimal number of A: {A.value()}")
print(f"Optimal number of B: {B.value()}")
print(f"Maximum Profit: ${model.objective.value()}")