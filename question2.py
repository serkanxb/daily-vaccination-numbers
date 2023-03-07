import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('vaccinations.csv')

# Fill missing values with 0
df['daily_vaccinations'].fillna(0, inplace=True)

# Group by country and calculate the median daily vaccinations
country_stats = df.groupby('country')['daily_vaccinations'].median().reset_index()

# Sort by median daily vaccinations in descending order and get the top 3
top_countries = country_stats.sort_values('daily_vaccinations', ascending=False).head(3)

# Print the top 3 countries
print(top_countries[['country', 'daily_vaccinations']])
