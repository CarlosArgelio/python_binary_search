"""
text
"""

objective = int(input("Choose a number: "))
EPSILON = 0.01
limit_infer = 0.0
limit_superior = max(1.0, objective)
response = (limit_infer + limit_superior) / 2

while abs(response**2 - objective) >= EPSILON:
    if response**2 < objective:
        limit_infer = response
    else:
        limit_superior = response
    response = (limit_infer + limit_superior) / 2

print(f"The square root of {objective} is {response}")
