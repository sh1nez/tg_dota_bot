from database.obj import Database
print('first')
conn = Database()
print('second')
conn1 = Database()
print(id(conn))
print(id(conn1))
