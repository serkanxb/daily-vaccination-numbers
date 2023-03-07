import pandas as pd

# Read the input file
df = pd.read_csv('daily_vaccination_number.csv')

# Group the data by country
grouped = df.groupby('country')

# Calculate the minimum daily vaccination number for each country
min_daily_vaccinations = grouped['daily_vaccinations'].min()

# Impute missing values in the daily_vaccinations column with the minimum daily vaccination number of relevant countries
df['daily_vaccinations'] = df.apply(lambda x: min_daily_vaccinations[x['country']] if pd.isna(x['daily_vaccinations']) else x['daily_vaccinations'], axis=1)

# Fill remaining NaN values with 0
df = df.fillna(0)


