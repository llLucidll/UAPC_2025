"""
Many recipes call for preheating an oven followed by putting food in the oven once the oven reaches the desired temperature. Thomas considers this process remarkably inefficient since energy is expended while preheating without cooking the food. To be more energy-efficient, he decides to put the food in the oven right when he turns it on.

Thomas’s food requires 
 minutes of cooking at the oven’s desired temperature. The amount of energy transferred to the food by the oven in a certain amount of time is linearly correlated with its temperature. When the oven is off, no energy is transferred to the food, and it would take forever to finish cooking. If the oven was set to a temperature that is halfway to the desired temperature, the food would need 
 minutes to finish cooking. Thomas knows that his oven will take 
 minutes to reach the desired temperature, with the temperature increasing linearly over time. For example, after 
 
 minutes, the oven will be halfway to the desired temperature.

Your task is to determine how long it will take for Thomas’s food to be fully cooked when he puts the food in immediately, rather than preheating the oven first.

Input
The first line contains two integers 
 and 
 (
) as described above.

Output
Output a single floating-point number representing the total time in minutes required for Thomas’s food to cook. Your answer will be considered correct if it has an absolute or relative error of at most 
.
"""

# if T > H/2 total = T + H/2
# if T <= H/2 total = root(2HT)

T, H = input().split(" ")

T = int(T)
H = int(H)

if T > H/2:
    print(T + H/2)
else:
    print((2*H*T)**(1/2))
