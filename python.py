import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, t
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
laliga_df = pd.read_csv("Laliga.csv")
golf_df = pd.read_csv("Golf.csv")

# Clean La Liga Data
laliga_df_clean = laliga_df.iloc[1:].reset_index(drop=True)
laliga_df_clean.columns = laliga_df.iloc[0]
laliga_df_clean = laliga_df_clean.loc[:, ~laliga_df_clean.columns.str.contains('^Unnamed')]

numeric_cols = ['Seasons', 'Points', 'GamesPlayed', 'GamesWon', 'GamesDrawn', 'GamesLost',
                'GoalsFor', 'GoalsAgainst', 'Champion', 'Runner-up', 'Third', 'Fourth',
                'Fifth', 'Sixth', 'T', 'BestPosition']
laliga_df_clean[numeric_cols] = laliga_df_clean[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Analysis 1: Teams Started Between 1930 and 1980
teams_started_1930_1980 = laliga_df_clean[laliga_df_clean['Debut'].astype(str).str[:4].astype(int).between(1930, 1980)][['Team', 'Debut']]

# Analysis 2: Top 5 Teams by Points
top_5_teams_points = laliga_df_clean[['Team', 'Points']].sort_values(by='Points', ascending=False).head(5)

# Analysis 3: Winning Percentage
laliga_df_clean['WinningPercentage'] = (laliga_df_clean['GamesWon'] / laliga_df_clean['GamesPlayed']) * 100
top_5_winning_percentage = laliga_df_clean[['Team', 'WinningPercentage']].sort_values(by='WinningPercentage', ascending=False).head(5)

# Hypothesis Test for Winning Percentage
group_1_3 = laliga_df_clean[laliga_df_clean['BestPosition'].between(1, 3)]['WinningPercentage']
group_4_7 = laliga_df_clean[laliga_df_clean['BestPosition'].between(4, 7)]['WinningPercentage']
t_stat, p_value = ttest_ind(group_1_3, group_4_7, nan_policy='omit')

# Golf Analysis
current_mean = golf_df['Current'].mean()
new_mean = golf_df['New'].mean()
t_stat_golf, p_value_golf = ttest_ind(golf_df['Current'], golf_df['New'])

# Confidence Intervals
n_current, n_new = len(golf_df['Current']), len(golf_df['New'])
se_current = golf_df['Current'].std() / np.sqrt(n_current)
se_new = golf_df['New'].std() / np.sqrt(n_new)
ci_current = t.interval(0.95, n_current - 1, loc=current_mean, scale=se_current)
ci_new = t.interval(0.95, n_new - 1, loc=new_mean, scale=se_new)

def print_results():
    print("\n🏆 La Liga Analysis")
    print("Teams Started Between 1930 and 1980:\n", teams_started_1930_1980)
    print("\nTop 5 Teams by Points:\n", top_5_teams_points)
    print("\nTop 5 Winning Percentages:\n", top_5_winning_percentage)
    print("\nHypothesis Test: T-stat:", round(t_stat, 2), "P-value:", round(p_value, 5))
    
    print("\n⛳ Golf Hypothesis Test")
    print("T-stat:", round(t_stat_golf, 2), "P-value:", round(p_value_golf, 5))
    print("95% CI for Current Model:", ci_current)
    print("95% CI for New Model:", ci_new)
    
print_results()
