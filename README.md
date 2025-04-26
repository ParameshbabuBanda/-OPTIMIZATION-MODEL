# -OPTIMIZATION-MODEL

Company: CODTECH IT SOLUTION

NAME : PARAMESH BABU BANDA

INTERN ID : CT04WS27

DOMAIN : DATA SCIENCE

MENTOR : NEELA SANTHOSH KUMAR

One-Page Description: Optimization Model to Maximize Profit (Using PuLP)
This project uses Linear Programming (LP) techniques to maximize profit by deciding the best number of products to produce. It uses the PuLP library in Python, which is commonly used for solving optimization problems.

Step-by-Step Explanation
Import Required Libraries

LpMaximize, LpProblem, and LpVariable are imported from the pulp library.

These tools allow us to define decision variables, the objective function, and constraints.

Create the Optimization Problem

model = LpProblem(name="maximize-profit", sense=LpMaximize)

A new linear programming model is created, with the goal set to maximize the objective function.

Define Decision Variables

Two integer decision variables are created:

A: number of units for Product A.

B: number of units for Product B.

Both variables have a lower bound of 0 (they cannot be negative).

Set the Objective Function

The goal is to maximize profit:
Profit = 20 * A + 30 * B

Each unit of Product A contributes $20 to the profit, and each unit of Product B contributes $30.

Add Constraints

Material Constraint:
2A + 4B <= 100
(Each A uses 2 units of material, each B uses 4 units, and total material available is 100 units.)

Labor Constraint:
A + 2B <= 40
(Each A requires 1 unit of labor, each B requires 2 units, and total labor available is 40 units.)

Solve the Model

model.solve() solves the optimization problem.

PuLP internally uses solvers to find the values of A and B that maximize profit while satisfying all constraints.

Print the Results

A.value() prints the optimal quantity of Product A to produce.

B.value() prints the optimal quantity of Product B to produce.

model.objective.value() prints the maximum profit achieved with the optimal production plan.

Summary
This project models a business decision-making problem using Linear Programming.

![Image](https://github.com/user-attachments/assets/fd06b6a5-6db3-41c2-997b-5edcf9b2e4f6)


It finds the optimal combination of two products that will generate the highest profit, considering the limitations of materials and labor.

PuLP makes it easy to set up, solve, and interpret optimization models in Python.

✅ This method can be applied to manufacturing, logistics, finance, and many real-world fields where resources are limited and decisions must be optimized.

