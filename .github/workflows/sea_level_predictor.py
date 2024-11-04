import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 1. Import the data
df = pd.read_csv('epa-sea-level.csv')

# 2. Create a scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

# 3. Create first line of best fit (using all data)
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years_extended = pd.Series(range(1880, 2051))
best_fit_line = slope * years_extended + intercept
plt.plot(years_extended, best_fit_line, color='red', label='Best Fit Line (1880-2050)')

# 4. Create second line of best fit (from 2000 to present)
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
best_fit_line_recent = slope_recent * years_extended + intercept_recent
plt.plot(years_extended, best_fit_line_recent, color='green', label='Best Fit Line (2000-2050)')

# 5. Labeling the plot
plt.title('Rise in Sea Level')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.legend()
plt.grid()
plt.xlim(1880, 2050)
plt.ylim(bottom=0)  # Optional: Set a lower limit for y-axis
plt.tight_layout()

# Save the plot
plt.savefig('sea_level_plot.png')
plt.show()
