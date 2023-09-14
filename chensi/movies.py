import sqlite3

# Read the file and copy its content to a list
with open("stephen_king_adaptations.txt", "r") as file:
    stephen_king_adaptations_list = file.readlines()

# Establish a connection with the SQLite database
connection = sqlite3.connect("stephen_king_adaptations.db")
cursor = connection.cursor()

# # Create the table in the database
# cursor.execute('''CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table (
#                     movieID TEXT PRIMARY KEY,
#                     movieName TEXT,
#                     movieYear TEXT,
#                     imdbRating REAL
#                 )''')
#
# # Insert the content from the list into the table
# for adaptation in stephen_king_adaptations_list:
#     try:
#         movie_id, movie_name, movie_year, imdb_rating = adaptation.strip().split(",")
#         cursor.execute('''INSERT INTO stephen_king_adaptations_table (movieID, movieName, movieYear, imdbRating)
#                           VALUES (?, ?, ?, ?)''', (movie_id, movie_name, movie_year, float(imdb_rating)))
#     except ValueError:
#         print("Skipping line:", adaptation.strip(), "- Invalid format")


# Commit the changes and close the connection
connection.commit()
connection.close()
# Search for movies in the database based on user input
while True:
    print("Please select an option:")
    print("1. Search by movie name")
    print("2. Search by movie year")
    print("3. Search by movie rating")
    print("4. STOP")

    option = input("Enter your choice: ")

    if option == "1":
        movie_name = input("Enter the name of the movie: ")
        connection = sqlite3.connect("stephen_king_adaptations.db")
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM stephen_king_adaptations_table WHERE movieName = ?''', (movie_name,))
        result = cursor.fetchone()
        connection.close()

        if result:
            print("Movie details:")
            print("ID:", result[0])
            print("Name:", result[1])
            print("Year:", result[2])
            print("Rating:", result[3])
        else:
            print("No such movie exists in our database")

    elif option == "2":
        movie_year = input("Enter the year of the movie: ")
        connection = sqlite3.connect("stephen_king_adaptations.db")
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM stephen_king_adaptations_table WHERE movieYear = ?''', (movie_year,))
        results = cursor.fetchall()
        connection.close()

        if results:
            print("Movies released in", movie_year, ":")
            for result in results:
                print("ID:", result[0])
                print("Name:", result[1])
                print("Year:", result[2])
                print("Rating:", result[3])
        else:
            print("No movies were found for that year in our database.")

    elif option == "3":
        rating_limit = input("Enter the minimum rating: ")
        connection = sqlite3.connect("stephen_king_adaptations.db")
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?''', (float(rating_limit),))
        results = cursor.fetchall()
        connection.close()

        if results:
            print("Movies with a rating of", rating_limit, "or above:")
            for result in results:
                print("ID:", result[0])
                print("Name:", result[1])
                print("Year:", result[2])
                print("Rating:", result[3])
        else:
            print("No movies at or above that rating were found in the database.")

    elif option == "4":
        break

    else:
        print("Invalid option. Please try again.")