import os
import csv
import pandas as pd

#file = 'web_starter.csv'

#udemy_df = pd.read_csv(file, encoding="ISO-8859-1")
#udemy_df.columns = ["id", "title", "url", "isPaid", "price", "numSubscribers", "numReviews",
 #                   "numPublishedLectures", "instructionalLevel", "contentInfo", "publishedTime"]
#organized_df = udemy_df[["title","price","numSubscribers","numReviews", "publishedTime"]]
#print(organized_df.head())


#quotient = [i / j for i, j in zip(organized_df['numReviews'], organized_df['numSubscribers'])]
#print(quotient)

#organized_df['publishedTime'].split(" ")
#print(organized_df['publishedTime'])

#organized_df[['numReviews']] = organized_df[['numReviews']]/organized_df['numSubscribers']
#print()
#quotient = []
#for i in range(organized_df['numReviews']):
 #   for j in range(organized_df['numSubscribers']):
#        quotient[i][j] = 
udemy_csv = os.path.join("web_starter.csv")

# Lists to store data
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []

with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
#with open(udemy_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add title
        # YOUR CODE HERE
        title.append(row[1])
        # Add price
        # YOUR CODE HERE
        price.append(row[4])
        # Add number of subscribers
        # YOUR CODE HERE
        subscribers.append(row[5])
        # Add amount of reviews
        # YOUR CODE HERE
        reviews.append(row[6])
        # Determine percent of review left to 2 decimal places
        # YOUR CODE HERE
        per = round(int(row[6]) / int(row[5]), 2)
        review_percent.append(per)
        # Get length of the course to just a number
        # YOUR CODE HERE
        course_length = row[9].split(" ")
        length.append(float(course_length[0]))
# Zip lists together
# YOUR CODE HERE
zip_data = zip(title, price, subscribers, reviews, review_percent, length)

clean_csv = zip_data
for x in clean_csv:
    print(x)
# Set variable for output file
output_file = os.path.join("web_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])

    # Write in zipped rows
    # YOUR CODE HERE
    writer.writerows(zip_data)