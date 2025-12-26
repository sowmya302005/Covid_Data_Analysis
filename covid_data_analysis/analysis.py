import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/covid_data.csv")

print("Dataset Head:")
print(df.head())
print("\nDataset Info:")
print(df.info())

# Filter for a state (e.g., KS)
state_name = 'KS'  # Change this to the state you want
state_data = df[df['state'] == state_name]

# Convert date column
state_data['submission_date'] = pd.to_datetime(state_data['submission_date'])

# Total Cases
plt.figure(figsize=(12,6))
plt.plot(state_data['submission_date'], state_data['tot_cases'], color='blue')
plt.title(f"Total COVID-19 Cases in {state_name}")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Daily New Cases
plt.figure(figsize=(12,6))
plt.plot(state_data['submission_date'], state_data['new_case'], color='orange')
plt.title(f"Daily New COVID Cases in {state_name}")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Total Deaths
plt.figure(figsize=(12,6))
plt.plot(state_data['submission_date'], state_data['tot_death'], color='red')
plt.title(f"Total Deaths Due to COVID in {state_name}")
plt.xlabel("Date")
plt.ylabel("Deaths")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 7-Day Rolling Average of New Cases
state_data['new_case_7day_avg'] = state_data['new_case'].rolling(7).mean()
plt.figure(figsize=(12,6))
plt.plot(state_data['submission_date'], state_data['new_case_7day_avg'], color='green')
plt.title(f"7-Day Rolling Avg of Daily New Cases in {state_name}")
plt.xlabel("Date")
plt.ylabel("7-Day Average")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Daily Growth Rate %
state_data['daily_growth_rate'] = state_data['tot_cases'].pct_change() * 100
plt.figure(figsize=(12,6))
plt.plot(state_data['submission_date'], state_data['daily_growth_rate'], color='purple')
plt.title(f"Daily Growth Rate (%) of Total Cases in {state_name}")
plt.xlabel("Date")
plt.ylabel("Growth Rate (%)")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Key insights
peak_cases_date = state_data.loc[state_data['new_case'].idxmax(), 'submission_date']
total_cases = state_data['tot_cases'].iloc[-1]
total_deaths = state_data['tot_death'].iloc[-1]

print(f"\n--- Key Insights for {state_name} ---")
print(f"Peak of daily new cases: {peak_cases_date.date()}")
print(f"Total cases till date: {int(total_cases)}")
print(f"Total deaths till date: {int(total_deaths)}")
