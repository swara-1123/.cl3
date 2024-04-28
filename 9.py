import pandas as pd

data_url = "C:/Users/Dell/Downloads/weather.csv"
df = pd.read_csv(data_url)
years = df['Year'].unique()

def find_extreme_year(years, data, is_hottest=True):
   extreme_year = None
   extreme_temp = float('-inf') if is_hottest else float('inf')
   for year in years:
    year_data = data[data['Year'] == year]
    avg_temp = year_data['Temperature'].mean()
    if (is_hottest and avg_temp > extreme_temp) or (not is_hottest and avg_temp < extreme_temp):
      extreme_year = year
      extreme_temp = avg_temp
      return extreme_year
# Find hottest year
hottest_year = find_extreme_year(years.copy(), df.copy())
# Find coolest year
coolest_year = find_extreme_year(years.copy(), df.copy(), False)
print(f"Hottest Year: {hottest_year}")
print(f"Coolest Year: {coolest_year}")