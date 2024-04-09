import numpy as np

# Parameters
total_time = 10  # seconds
sampling_frequency = 100  # Hz
num_samples = total_time * sampling_frequency
time = np.linspace(0, total_time, num_samples)

# Generate voltage signal
voltage = np.ones_like(time) * 12  # Initially at 12V
drop_index = int(2 * sampling_frequency)  # 2 seconds
voltage[:drop_index] = np.linspace(12, 10, drop_index)  # Sudden drop from 12V to 10V
# Oscillations between 10.8V and 9.4V
for i in range(4):
    oscillation_start = drop_index + i * int(0.5 * sampling_frequency)  # Every 0.5 seconds
    oscillation_end = oscillation_start + int(0.2 * sampling_frequency)  # Lasts 0.2 seconds
    voltage[oscillation_start:oscillation_end] = np.linspace(10.8, 9.4, oscillation_end - oscillation_start)
# Sudden rise to 14V after 2 seconds
rise_index = drop_index + 2 * int(sampling_frequency)
voltage[rise_index:] = 14

# Save data to a CSV file
import csv

with open('voltage_dataset.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Time (s)', 'Voltage (V)'])
    for t, v in zip(time, voltage):
        writer.writerow([t, v])

print("Dataset generated and saved as 'voltage_dataset.csv'.")
