import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="Dipen3",
    password="hellodipen",
)
def print_sql_table(cursor, sql):
    cursor.execute(sql)
    conn.commit()
    results = cursor.fetchall()

    widths = []
    columns = []
    tavnit = '|'
    separator = '+'

    for cd in cursor.description:
        widths.append(max(cd[2], len(cd[0])))
        columns.append(cd[0])

    for w in widths:
        tavnit += " %-" + "%ss |" % (w,)
        separator += '-' * w + '--+'

    print(separator)
    print(tavnit % tuple(columns))
    print(separator)
    for row in results:
        print(tavnit % row)
    print(separator)
def print_list_as_sql_table(rows):
    if not rows:
        print("Empty result set.")
        return

    if isinstance(rows[0], dict):
        columns = list(rows[0].keys())
    else:
        columns = [f"Column_{i+1}" for i in range(len(rows[0]))]

    widths = [max(len(str(col)), max(len(str(row[i])) for row in rows)) for i, col in enumerate(columns)]

    tavnit = '|'
    separator = '+'

    for w in widths:
        tavnit += " %-" + "%ss |" % (w,)
        separator += '-' * w + '--+'

    print(separator)
    print(tavnit % tuple(columns))
    print(separator)
    
    for row in rows:
        print(tavnit % tuple(str(cell) for cell in row))
    
    print(separator)

mycursor = mydb.cursor()
mycursor.execute("USE tables_practice_1")
#mycursor.execute("CREATE TABLE Country(Country varchar(40),Population int(10))")
#mycursor.execute("INSERT INTO Country VALUES ('India',100),('China',200),('Japan',400),('USA',300),('UK',200)")
#mycursor.execute("SELECT * FROM Country")
tables1 = mycursor.fetchall()
print("table 1:")
print_list_as_sql_table(tables1)
mycursor.execute("select * from emp")
out =  mycursor.fetchall()
print_list_as_sql_table(out)
print("table 2:")
print_list_as_sql_table(tables1)
mycursor.execute("select * from dept")
out =  mycursor.fetchall()
print_list_as_sql_table(out)

print("table 1:")
print_list_as_sql_table(tables1)
while True:
    i = str(input())
    #i = ""
    mycursor.execute(i)
    out =  mycursor.fetchall()
    print("Result:")
    print_list_as_sql_table(out)

mycursor.close()
mydb.close()