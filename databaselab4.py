import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

data = {
    "Traveler_ID": range(1, 21),
    "Destination": np.random.choice(["Paris", "Tokyo", "Rome", "Istanbul", "New York", "Dubai"], 20),
    "Days_Spent": np.random.randint(2, 14, 20),
    "Total_Cost": np.random.randint(500, 5000, 20),
    "Age": np.random.randint(18, 60, 20),
    "Travel_Type": np.random.choice(["Solo", "Family", "Friends", "Couple"], 20),
    "Transport_Mode": np.random.choice(["Plane", "Train", "Car", "Bus"], 20),
    "Satisfaction_Rating": np.random.randint(1, 6, 20)
}

df = pd.DataFrame(data)

# Part 1

print("Part 1: Data Exploration")

# 1. Display the first and last 5 rows of the dataset.
print("Task 1: First 5 Rows")
print(df.head())
print("Task 1: Last 5 Rows")
print(df.tail())

# 2. Show the total number of travelers and unique destinations.
print(f"Task 2: Total Travelers & Unique Destinations")
print(f"Total number of travelers: {len(df)}")
print(f"Number of unique destinations: {df['Destination'].nunique()}")

# 3. Find the average number of days spent and total cost per travel type.
print("Task 3: Avg Days & Cost by Travel Type")
avg_by_travel_type = df.groupby('Travel_Type')[['Days_Spent', 'Total_Cost']].mean()
print(avg_by_travel_type)

# 4. Which destination had the highest average satisfaction rating?
print("Task 4: Destination with Highest Avg Rating")
avg_rating_by_dest = df.groupby('Destination')['Satisfaction_Rating'].mean()
highest_rated_dest = avg_rating_by_dest.idxmax()
print(f"Destination with highest avg rating: {highest_rated_dest}")
print(avg_rating_by_dest.sort_values(ascending=False))

# 5. Find the traveler who spent the most money and their travel details.
print("Task 5: Traveler with Max Spending")
max_spender = df.loc[df['Total_Cost'].idxmax()]
print(max_spender)

# Part 2

print("Part 2 and 3")

# 6. Create a bar chart showing the average total cost for each destination.
plt.figure(figsize=(10, 6))
avg_cost_by_dest = df.groupby('Destination')['Total_Cost'].mean().sort_values()
sns.barplot(x=avg_cost_by_dest.index, y=avg_cost_by_dest.values)
plt.title('Task 6: Average Total Cost by Destination')
plt.xlabel('Destination')
plt.ylabel('Average Total Cost')
plt.show()

# 7. Plot a histogram of satisfaction ratings.
plt.figure(figsize=(10, 6))
sns.histplot(df['Satisfaction_Rating'], bins=5, discrete=True, kde=False) 
plt.title('Task 7: Histogram of Satisfaction Ratings')
plt.xlabel('Satisfaction Rating (1-5)')
plt.ylabel('Number of Travelers')
plt.xticks(range(1, 6))
plt.show()

# 8. Draw a scatter plot of days spent vs total cost.
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Days_Spent', y='Total_Cost', hue='Travel_Type', size='Age', sizes=(50, 200))
plt.title('Task 8: Scatter Plot of Days Spent vs Total Cost')
plt.xlabel('Days Spent')
plt.ylabel('Total Cost')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left') #
plt.tight_layout() 
plt.show()

# 9. Create a box plot comparing total cost by travel type.
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Travel_Type', y='Total_Cost')
plt.title('Task 9: Box Plot of Total Cost by Travel Type')
plt.xlabel('Travel Type')
plt.ylabel('Total Cost')
plt.show()

# 10. Plot a correlation heatmap for numerical variables.
plt.figure(figsize=(10, 6))
numerical_cols = ['Days_Spent', 'Total_Cost', 'Age', 'Satisfaction_Rating']
corr_matrix = df[numerical_cols].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Task 10: Correlation Heatmap of Numerical Variables')
plt.show()


# Part 3

# 11. Make a pie chart showing the proportion of travelers by transport mode.
plt.figure(figsize=(8, 8))
transport_counts = df['Transport_Mode'].value_counts()
plt.pie(transport_counts, labels=transport_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Task 11: Proportion of Travelers by Transport Mode')
plt.ylabel('')
plt.show()

# 12. Create a line plot showing total cost in order of traveler IDs.
plt.figure(figsize=(10, 6))
df_sorted = df.sort_values('Traveler_ID')
sns.lineplot(data=df_sorted, x='Traveler_ID', y='Total_Cost', marker='o')
plt.title('Task 12: Total Cost by Traveler ID')
plt.xlabel('Traveler ID')
plt.ylabel('Total Cost')
plt.show()

# 13. Use seaborn's pairplot to explore relationships among numeric variables.
sns.pairplot(df[numerical_cols])
plt.suptitle('Task 13: Pairplot of Numerical Variables', y=1.02) 
plt.show()

# 14. Create a count plot of travel types per destination.
plt.figure(figsize=(12, 7))
sns.countplot(data=df, x='Destination', hue='Travel_Type')
plt.title('Task 14: Count Plot of Travel Types per Destination')
plt.xlabel('Destination')
plt.ylabel('Count')
plt.xticks(rotation=45) 
plt.legend(title='Travel Type')
plt.tight_layout()
plt.show()
