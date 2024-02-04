# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:04:07 2024

@author: Mashala
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:/movieproject/movieproject/movie_dataset.csv")

print(df)

print(df.info())

print(df.describe())

# print(df.info())


#Q1 highest rated movie Q1

high_movie = df.loc[df["Rating"].idxmax()]
print(high_movie)

#Q2 Remove Nans 
# df.columns= df.columns.str.replace("","")
# df.dropna(inplace = True)
# df = df.reset_index(drop=True)

#average
print(df['Revenue (Millions)'].mean())

#filtering Q3

filter_year = df[(df['Year'] >=2015) & (df['Year'] <=2017)]
# print(filter_year)
# avg_Revenue__Year = filter_year['Revenue (Millions)'].mean()
# print(avg_Revenue__Year)

# Filter data for 2016 movies Q4
movies_2016 = len(df[df['Year']==2016])


print(movies_2016)
#filter director Christoper Nolan Q5
Director_Chris =len(df[df['Director']=='Christopher Nolan'])
print(Director_Chris)

#Q6

movies_rating = len(df[df['Rating']>= 8])
print(movies_rating)

#Q7 median of Chris Nolan movies
median_Chris_Nolan = df[df['Director']=='Christopher Nolan']
print(median_Chris_Nolan.median)

#Q8 average rating of the year
Avg_rating_year = df.groupby('Year')['Rating'].mean()
print(Avg_rating_year)

#Q9 increase percentage
movies_2006 =len(df[df['Year']==2006])
movies_2016 =len(df[df['Year']==2016])
Percent_inc =((movies_2016-movies_2006)/movies_2006)*100

print(Percent_inc)

#Q10 common actors

actors = df['Actors'].str.split(', ').explode()
actors_count =actors.value_counts()
common_actors=actors_count.idxmax()
print(common_actors)


#Q11 Movie Genre

Genre = df['Genre'].str.split(', ').explode()
Genre_count =Genre.nunique()
print(Genre_count)


# Calculate the correlation matrix for the numerical values in the dataset
correlation_matrix = df[['Year', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)', 'Metascore']].corr()

correlation_matrix

# Plotting the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix of Movie Dataset')
plt.show()

#df.to_csv("C:/movieproject/movieproject/movie_dataset.csv")
