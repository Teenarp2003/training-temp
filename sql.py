import mysql.connector
mydb1 = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
)
dbname=input("\nEnter default database:")
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database=dbname,
)
def main():
  a = int(input("\nEnter your choice:\n\n1.Create New Database.\n2.Drop Database.\n3.Create New Table\n4.Delete Table.\n5.Insert Data in Table.\n6.Delete Data from Table.\n7.List Elements in Table.\n8.Exit\n"))
  if a ==1:
    NewDatabase() 
  elif a ==2:
    DropDatabase()
  elif a ==3:
    sql.NewTable()
  elif a ==4:
    sql.DelTable()
  elif a ==5:
    sql.Insert()
  elif a ==6:
    sql.Delete()
  elif a ==7:
     sql.List()
  elif a ==8:
    exit(1)

def NewDatabase(): 
  mycursor = mydb1.cursor()
  newdb=input("\nEnter database Name: ")
  var=(newdb,)
  mycursor.execute("CREATE DATABASE %s"%var)
  print("\nDatabase Created!")
  main()

def DropDatabase():
  database_name = input("\nEnter the name of the database to delete: ")
  cursor = mydb.cursor()
  query = f"DROP DATABASE IF EXISTS {database_name}"
  cursor.execute(query)
  mydb.commit()
  print(f"\nThe database {database_name} has been deleted.")
  main()

class sql:
    def NewTable():
      table_name = input("\nEnter the name of the table: ")
      num_columns = int(input("\nEnter the number of columns: "))
      columns = []
      for i in range(num_columns):
          column_name = input(f"\nEnter the name of column {i+1}: ")
          data_type = input(f"\nEnter the data type of column {i+1} (e.g. VARCHAR(255), INT, FLOAT, etc.): ")
          columns.append(f"{column_name} {data_type}")

      cursor = mydb.cursor()
      query = f"CREATE TABLE {table_name} ({', '.join(columns)})"
      cursor.execute(query)
      mydb.commit()
      main()
    
    def DelTable():
      cursor = mydb.cursor()
      query = "DROP TABLE table_name;"
      cursor.execute(query)
      mydb.commit()
      main()
    
    def Insert():
      table_name = input("\nEnter the name of the table: ")
      cursor = mydb.cursor()
      cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'")
      column_names = [row[0] for row in cursor.fetchall()]
      values = []
      for column_name in column_names:
          value = input(f"\nEnter a value for {column_name}: ")
          values.append(value)
      query = f"INSERT INTO {table_name} ({', '.join(column_names)}) VALUES ({', '.join(['%s']*len(column_names))})"
      cursor.execute(query, tuple(values))
      mydb.commit()
      print(f"Values ({', '.join(values)}) have been inserted into {table_name}.")
      main()
            
    def Delete():
      table_name = input("\nEnter the name of the table: ")
      condition_column = input("\nEnter the name of the column to use as the condition: ")
      cursor = mydb.cursor()
#     cursor.execute(f"DESCRIBE {table_name}")
#     columns = [column[0] for column in cursor.fetchall()]
      condition_value = input(f"\nEnter the value of the condition for column {condition_column}: ")
      query = f"DELETE FROM {table_name} WHERE {condition_column} = %s"
      values = (condition_value,)
      cursor.execute(query, values)
      mydb.commit()
      print(f"\n{cursor.rowcount} rows have been deleted from table {table_name} where {condition_column} = {condition_value}.")
      main()
    
    def List():
      cursor = mydb.cursor()
      table_name=input("\nEnter table name: ")
      query = f"SELECT * FROM {table_name}"
      cursor.execute(query)
      rows = cursor.fetchall()
      for row in rows:
          print(row)
      main()

main()