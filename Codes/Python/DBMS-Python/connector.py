import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="Dipen3",
    password="hellodipen",
    #database="your_database_name"
)
#class(to store):
    #mycursor.execute("USE tables_practice_1")
    #mycursor.execute("SHOW TABLES")

    # Fetch all the tables
    #tables = mycursor.fetchall()
    #for table in tables:
        #print(table)

    #mycursor.execute("SELECT * FROM emp")
    #tables = mycursor.fetchall()

    #print(type(tables))
    #print(tables)
    #x = tables[0][0]
    #print(f"x:{x}")
    #print("print :")
    #for table in tables:
        #print(table[0])
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
mycursor.execute("SELECT * FROM emp")
tables1 = mycursor.fetchall()
print("table 1:")
print_list_as_sql_table(tables1)
mycursor.execute("SELECT * FROM dept")
tables2 = mycursor.fetchall()
print("table 2")
print_list_as_sql_table(tables2)

#join
mycursor.execute(" SELECT e.ename, e.empno, e.job, d.deptno, d.loc FROM emp e INNER JOIN dept d ON e.deptno = d.deptno;")
innerjointable =  mycursor.fetchall()
print_list_as_sql_table(innerjointable)

mycursor.close()
mydb.close()
