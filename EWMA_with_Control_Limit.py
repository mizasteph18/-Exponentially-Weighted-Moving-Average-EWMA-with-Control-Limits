import pandas as pd
import numpy as np

# Assuming your dataframe is called 'df' with columns 'date' and 'stress_test'
df['ewma'] = df['stress_test'].ewm(alpha=0.2).mean() # Example alpha value
df['ewma_std'] = df['stress_test'].ewm(alpha=0.2).std() # Exponentially weighted std

# Set control limits (e.g., +/- 2 standard deviations)
df['upper_limit'] = df['ewma'] + 2 * df['ewma_std']
df['lower_limit'] = df['ewma'] - 2 * df['ewma_std']

latest_stress_test = df['stress_test'].iloc[-1]
latest_upper_limit = df['upper_limit'].iloc[-1]
latest_lower_limit = df['lower_limit'].iloc[-1]

if latest_stress_test > latest_upper_limit or latest_stress_test < latest_lower_limit:
    print("The latest stress test figure is a potential outlier.")
else:
    print("The latest stress test figure is within the expected range.")

print(df[['date', 'stress_test', 'ewma', 'upper_limit', 'lower_limit']].tail())
