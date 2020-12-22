#Join Two or More Tables
#You can combine rows from two or more tables, based on a related column between them, by using a JOIN statement.

#Consider you have a "users" table and a "products" table:

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


  #LEFT JOIN
#In the example above, Hannah, and Michael were excluded from the result, that is because INNER JOIN only shows the records where there is a match.
#If you want to show all users, even if they do not have a favorite product, use the LEFT JOIN statement:

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"

#RIGHT JOIN
#If you want to return all products, and the users who have them as their favorite, even if no user have them as their favorite, use the RIGHT JOIN statement:

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"
