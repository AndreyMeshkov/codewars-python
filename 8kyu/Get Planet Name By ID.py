# Get Planet Name By ID
#
# https://www.codewars.com/kata/515e188a311df01cba000003
#
# The function is not returning the correct values. Can you figure out why?
#
# Example (Input --> Output ):
#
# 3 --> "Earth"

def get_planet_name(id):
    switcher = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune"}
    return switcher[id]

# Best practice:
#
# def get_planet_name(id):
#     return {
#         1: "Mercury",
#         2: "Venus",
#         3: "Earth",
#         4: "Mars",
#         5: "Jupiter",
#         6: "Saturn",
#         7: "Uranus",
#         8: "Neptune",
#     }.get(id, None)

# Clever solution:
#
# def get_planet_name(id):
#     return ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"][id-1]