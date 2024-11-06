import os
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Get database connection parameters from environment variables
host = os.getenv('DB_HOST', 'localhost')
port = os.getenv('DB_PORT', '5432')
database = os.getenv('DB_NAME', 'graph')
user = os.getenv('DB_USER', 'postgres')
password = os.getenv('DB_PASSWORD', 'docker')

# Define connection string and create an engine
connection_string = f'postgresql://{user}:{password}@{host}:{port}/{database}?sslmode=disable'
engine = create_engine(connection_string)

# Define the query to select the data
query = f'SELECT x, y FROM points'

# Load the data into a DataFrame
try:
    data = pd.read_sql(query, engine)
except Exception as e:
    print(f"An error occurred while fetching data: {e}")
finally:
    engine.dispose()

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(data['x'], data['y'], marker='o', linestyle='-', color='b')

# Customize the plot
plt.title('Line Graph from PostgreSQL Data')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.grid(True)

# Save the plot as a file
plt.savefig('plot.png')

