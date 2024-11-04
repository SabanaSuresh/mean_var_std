import pandas as pd

# Load the dataset
df = pd.read_csv('path_to_your_dataset.csv')  # Remplacez par le chemin de votre fichier CSV

# 1. How many people of each race are represented in this dataset?
race_counts = df['race'].value_counts()

# 2. What is the average age of men?
average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

# 3. What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

# 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
percentage_high_salary_advanced = round((df[advanced_education]['salary'] == '>50K').mean() * 100, 1)

# 5. What percentage of people without advanced education make more than 50K?
non_advanced_education = ~advanced_education
percentage_high_salary_non_advanced = round((df[non_advanced_education]['salary'] == '>50K').mean() * 100, 1)

# 6. What is the minimum number of hours a person works per week?
min_hours_per_week = df['hours-per-week'].min()

# 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
min_hours_high_salary_percentage = round((df[df['hours-per-week'] == min_hours_per_week]['salary'] == '>50K').mean() * 100, 1)

# 8. What country has the highest percentage of people that earn >50K and what is that percentage?
country_salary_percentage = df[df['salary'] == '>50K']['native-country'].value_counts(normalize=True) * 100
highest_country = country_salary_percentage.idxmax()
highest_percentage = round(country_salary_percentage.max(), 1)

# 9. Identify the most popular occupation for those who earn >50K in India.
popular_occupation_india = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]['occupation'].mode()[0]

# Print the results
print("Race counts:\n", race_counts)
print("Average age of men:", average_age_men)
print("Percentage of people with Bachelor's degree:", percentage_bachelors)
print("Percentage of people with advanced education earning >50K:", percentage_high_salary_advanced)
print("Percentage of people without advanced education earning >50K:", percentage_high_salary_non_advanced)
print("Minimum hours per week:", min_hours_per_week)
print("Percentage of minimum hour workers earning >50K:", min_hours_high_salary_percentage)
print("Country with highest percentage earning >50K:", highest_country, "with percentage:", highest_percentage)
print("Most popular occupation for those earning >50K in India:", popular_occupation_india)
