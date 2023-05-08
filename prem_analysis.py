import pandas as pd
import matplotlib.pyplot as plt

seasons = ['1011', '1112', '1213', '1314', '1415', '1516', '1617', '1718', '1819', '1920']

dfs = []
for season in seasons:
    filename = f'{season}.csv'
    df = pd.read_csv(filename)
    dfs.append(df)

matches = pd.concat(dfs)

# Remove duplicate rows
matches = matches.drop_duplicates()

# Convert the date column to datetime format
matches['Date'] = pd.to_datetime(matches['Date'], format='%d/%m/%Y')

# Calculate the total number of goals scored in each season
total_goals = matches.groupby('Season')['FTHG', 'FTAG'].sum().reset_index()

# Calculate the average number of goals scored by the home and away teams
avg_goals = matches.groupby('Season')['FTHG', 'FTAG'].mean().reset_index()

# Calculate the percentage of matches that end in a win, loss, or draw
results = matches.groupby('Season')['Result'].value_counts(normalize=True).reset_index(name='Percentage')

# Calculate the total number of goals scored by each team over the past 10 seasons
team_goals = matches.groupby('HomeTeam')['FTHG', 'FTAG'].sum().reset_index()
team_goals['Total Goals'] = team_goals['FTHG'] + team_goals['FTAG']
top_scorers = team_goals.nlargest(10, 'Total Goals')

# Create a bar chart of the total number of goals scored in each season
plt.bar(total_goals['Season'], total_goals['FTHG'] + total_goals['FTAG'])
plt.xlabel('Season')
plt.ylabel('Total Goals')
plt.title('Total Goals Scored in Each Premier League Season')
plt.show()

# Create a line chart of the average number of goals scored by the home and away teams
plt.plot(avg_goals['Season'], avg_goals['FTHG'], label='Home Goals')
plt.plot(avg_goals['Season'], avg_goals['FTAG'], label='Away Goals')
plt.xlabel('Season')
plt.ylabel('Average Goals')
plt.title('Average Number of Goals Scored by Home and Away Teams')
plt.legend()
plt.show()

# Create a pie chart of the percentage of matches that end in a win, loss, or draw
plt.pie(results['Percentage'], labels=results['Result'], autopct='%1.1f%%')
plt.title('Percentage of Premier League Matches by Result')
plt.show()

# Create a bar chart of the total number of goals scored by each team over the past 10 seasons
plt.bar(top_scorers['HomeTeam'], top_scorers['Total Goals'])
plt.xlabel('Team')
plt.ylabel('Total Goals')
plt.title('Premier League Top Scorers')
plt.show()
