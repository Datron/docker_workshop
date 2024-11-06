import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'data.csv'  # Replace 'data.csv' with the path to your file
data = pd.read_csv(file_path)

# Plotting
plt.figure(figsize=(10, 6))

# Assuming the CSV file has two columns: 'x' for x-axis and 'y' for y-axis
plt.plot(data['x'], data['y'], marker='o', linestyle='-', color='b')

# Customize the plot
plt.title('Line Graph from CSV Data')
plt.xlabel('X-axis Label')  # Customize label based on your data
plt.ylabel('Y-axis Label')  # Customize label based on your data
plt.grid(True)
plt.savefig('plot.png')

