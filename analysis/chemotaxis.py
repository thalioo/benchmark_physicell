import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')


p_data = pd.read_csv("/home/thalia/BSC/NEW_BENCH/Physicell_template/out_chemotaxis/position_step.csv")
c_data = pd.read_csv("/home/thalia/BSC/observatory_benchmark/multiscale_benchmark/2022_09_hackathon/Biodynamo/unit_test_chemotaxis/marenostrum_results/position.csv",header=None)




p_start = p_data.iloc[0,1:4]
p_end = p_data.iloc[-1,1:4]

zline = p_data['z']
xline = p_data['x']
yline = p_data['y']
ax.plot3D(xline, yline, zline,alpha = 0.33 ,color = 'green')
czline = c_data[4]
cxline = c_data[2]
cyline = c_data[3]
# ax.plot3D(czline, cyline, czline,alpha = 0.33 ,color = 'blue')

c_start = c_data.iloc[0,2:5]
c_end = c_data.iloc[-1,2:5]
print(c_data)
print(c_start)
ax.scatter3D(p_start['x'], p_start['y'], p_start['z'],color='green');
ax.scatter3D(p_end['x'], p_end['y'], p_end['z'],color='green');
ax.scatter3D(c_start[2], c_start[3], c_start[4],color='blue',alpha = 0.3);
ax.scatter3D(c_end[2], c_end[3], c_end[4],color='blue');
plt.show()