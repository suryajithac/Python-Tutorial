import csv
people = [
    [1, 'Linus Torvalds', 'Finland', 'Linux Kernel', 1991],
    [2, 'Tim Berners-Lee', 'England', 'World Wide Web', 1990],
    [3, 'Guido van Rossum', 'Netherlands', 'Python', 1991]
]
with open('famous_people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['SN', 'Name', 'Country', 'Contribution', 'Year'])
    writer.writerows(people)
print("CSV file created successfully.")