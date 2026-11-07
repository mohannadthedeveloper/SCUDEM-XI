#SCUDEM Model Code
import numpy as np
import matplotlib.pyplot as plt

#habitat rules
HABITAT_W = 1000
FOOD_LOCATION = 600

#parameters
a = 0.5
b = 0.5
I1, I2 = 1, 1
d = 0.1
v = 1
C = a*I1 + b*I2
t = np.linspace(0, 1200, 12001)
w0 = 20
x0 = 10
q = 0.1
k = 0.001 #narrowing rate
R = 1000 #max separation

#Analytical solutions to dW/dt and dx/dt for both animals, as well as the spread equation.
spread = np.clip(2*q*t, 0, R)
x_m1 = x0 + (C*(1-2*d*v))*t - (0.5*spread) #assuming they spread away at equal distances
x_m2 = x0 + (C*(1-2*d)*v)*t + (0.5*spread)
w1 = w0 * np.exp(-k*C*t)
w2 = w0 * np.exp(-k*C*t)

#Defining success
left1 = x_m1
right1 = x_m1 + w1
left2 = x_m2
right2 = x_m2 + w2
success = np.where(((left1 <= FOOD_LOCATION) & (right1 >= FOOD_LOCATION) | (left2 <= FOOD_LOCATION) & (right2 >= FOOD_LOCATION)), 1, 0)

#Modelling
#1. Both monkey positions over time
plt.plot(t, x_m1, label='Position of Animal 1', color='orange')
plt.plot(t, x_m2, label='Position of Animal 2', color='blue')
plt.xlabel("Time (t)")
plt.ylabel("Position (x)")
plt.axhline(R, color='red', linestyle='--', label='Maximum Communication Distance')
plt.axhline(FOOD_LOCATION, color='black', linestyle='--', label='Location of Food Source')
plt.title("Position of Both Animals at time t")
plt.legend()
plt.show()

#2. Search level widths over time
plt.plot(t, w1, label="Width of Animal 1's search level", color='green')
plt.plot(t, w2, label="Width of Animal 2's search level", color='gray')
plt.xlabel("Time (t)")
plt.ylabel("Search Interval Width W(t)")
plt.title("Search Interval Widths of Both Animals over time")
plt.legend()
plt.show()

#3. Information detail with time to success
info_levels = np.linspace(0.1, 1, 20)
times_to_success = []

#Calculate times to success using our varying info levels and eqautions
for I in info_levels:
    C_test = a*I + b*I

    spread_test = np.clip(2*q*t, 0, R)

    x1_test = x0 + (C_test*(1-2*d)*v)*t - 0.5*spread_test
    x2_test = x0 + (C_test*(1-2*d)*v)*t + 0.5*spread_test

    w_test = w0*np.exp(-k*C_test*t)

    success_test = (
        ((x1_test <= FOOD_LOCATION) & (FOOD_LOCATION <= x1_test+w_test)) |
        ((x2_test <= FOOD_LOCATION) & (FOOD_LOCATION <= x2_test+w_test))
    )

    success_idx = np.flatnonzero(success_test)
    if len(success_idx) > 0:
     times_to_success.append(t[success_idx[0]])
    else:
     times_to_success.append(np.nan)

plt.plot(info_levels, times_to_success, marker='o')
plt.xlabel("Information detail")
plt.ylabel("Time to success")
plt.title("Information Detail vs Time to Success")
plt.grid()
plt.show()

#4. Deception vs Times to success, basc we do the same thing
deception_levels = np.linspace(0.1, 1, 20)
times_to_success = []

#Calculate times to success using our varying info levels and eqautions
for I in deception_levels:
    C_test = a + b

    spread_test = np.clip(2*q*t, 0, R)

    x1_test = x0 + (C_test*(1-2*I)*v)*t - 0.5*spread_test
    x2_test = x0 + (C_test*(1-2*I)*v)*t + 0.5*spread_test

    w_test = w0*np.exp(-k*C_test*t)

    success_test = (
        ((x1_test <= FOOD_LOCATION) & (FOOD_LOCATION <= x1_test+w_test)) |
        ((x2_test <= FOOD_LOCATION) & (FOOD_LOCATION <= x2_test+w_test))
    )

    success_idx = np.flatnonzero(success_test)
    if len(success_idx) > 0:
     times_to_success.append(t[success_idx[0]])
    else:
     times_to_success.append(np.nan)

plt.plot(deception_levels, times_to_success, marker='o', color='orange')
plt.xlabel("Deception Level")
plt.ylabel("Time to success")
plt.title("Level of Deception/Misinformation vs Time to Success")
plt.grid()
plt.show()

#Sensitivity analysis: Which variables affect time to success more in foraging?
#Is it distance or communication detail and accuracy?
info_levels = np.linspace(0.1, 1, 30)
spread_levels = np.linspace(0.01, 0.5, 30)

heatmap = np.full((len(spread_levels), len(info_levels)), np.nan)
t_heat = np.linspace(0, 1200, 12000)
for i, q_test in enumerate(spread_levels):
    for j, I in enumerate(info_levels):

        C_test = a*I + b*I
        spread_test = 2*q_test*t_heat
        x1_test = x0 + C_test*(1-2*d)*v*t_heat - 0.5*spread_test
        x2_test = x0 + C_test*(1-2*d)*v*t_heat + 0.5*spread_test
        w_test = w0*np.exp(-k*C_test*t_heat)

        success_test = (
            ((x1_test <= FOOD_LOCATION) & (FOOD_LOCATION <= x1_test+w_test)) |
            ((x2_test <= FOOD_LOCATION) & (FOOD_LOCATION <= x2_test+w_test))
        )

        success_idx = np.flatnonzero(success_test)

        if len(success_idx) > 0:
            heatmap[i, j] = t_heat[success_idx[0]]

plt.figure(figsize=(9, 6))

plt.imshow(
    heatmap,
    origin='lower',
    aspect='auto',
    extent=[info_levels[0], info_levels[-1],
            spread_levels[0], spread_levels[-1]],
    cmap='viridis'
)

plt.colorbar(label='Time to First Success')
plt.xlabel('Information Detail (I)')
plt.ylabel('Spreading Rate (q)')
plt.title('Effect of Information Detail and Spreading Rate on Foraging Success')
plt.show()
