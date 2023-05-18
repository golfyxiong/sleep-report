import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('body_movement.csv')

# Define the threshold for movement detection
threshold = 0.05

# Calculate the standard deviation of the movement data
std_dev = np.std(data['movement'])

# Create a binary column indicating whether there was movement above the threshold
data['movement_binary'] = (data['movement'] > threshold).astype(int)

# Calculate the rolling sum of movement in 10-second windows
rolling_sum = data['movement_binary'].rolling(window=100).sum()

# Define the threshold for sleep onset detection
onset_threshold = 3

# Find the first 10-second window with a rolling sum above the onset threshold
onset_index = np.where(rolling_sum > onset_threshold)[0][0]

# Plot the movement data and the rolling sum
fig, ax = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

ax[0].plot(data['time'], data['movement'])
ax[0].set_ylabel('Movement')

ax[1].plot(data['time'], rolling_sum)
ax[1].axhline(y=onset_threshold, color='r', linestyle='--')
ax[1].set_xlabel('Time')
ax[1].set_ylabel('Rolling Sum')

plt.show()

# Print the sleep onset time
print('Sleep onset time:', data.loc[onset_index, 'time'])
