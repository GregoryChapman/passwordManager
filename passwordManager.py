import mysql.connector

def create_connection():
    # Establishing a connection to the MySQL server
    connection = mysql.connector.connect(
        host= "passwordbase.cxlyg1lkoyjt.us-east-2.rds.amazonaws.com",
        user= "admin",
        password= "Something23",
        database= "passwordBase"
    )
    return connection

# Create a connection
# connection = mysql.connector.connect(**db_config)
# cursor = connection.cursor()

# Creating a sample table
def create_table(connection):
    cursor = connection.cursor()
    cursor.execute = """
    CREATE TABLE IF NOT EXISTS passwords (
        id INT AUTO_INCREMENT PRIMARY KEY,
        website VARCHAR(255) NOT NULL,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    );
    """

# Inserting data
def insert_record(connection, website, username, password):
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO passwords (website, username, password)
    VALUES (%s, %s, %s)
    """
    cursor.execute(insert_query, (website, username, password))
    connection.commit()

# data_to_insert = ("example.com", "user123", "password123")
# cursor.execute(insert_query, data_to_insert)
# connection.commit()

# Updating data
def update_record(connection, website, username, password):
    cursor = connection.cursor()
    update_query = """
    UPDATE passwords
    SET password = %s
    WHERE website = %s AND username = %s
    """
    cursor.execute(update_query, (website, username, password))
    connection.commit()


# new_password = "newpassword456"
# update_data = (new_password, "example.com", "user123")
# cursor.execute(update_query, update_data)
# connection.commit()

# Deleting data
def delete_record(connection, website, username, password):
    cursor = connection.cursor()
    delete_query = """
    DELETE FROM passwords
    WHERE website = %s AND username = %s
    """
    cursor.execute(delete_query, (website, username, password))
    connection.commit()

# delete_data = ("example.com", "user123")
# cursor.execute(delete_query, delete_data)
# connection.commit()

# Selecting data
def select_record(connection):
    cursor = connection.cursor()
    select_query = """
    SELECT * FROM passwords
    """
    cursor.execute(select_query)
    connection.commit()

# cursor.execute(select_query)
# selected_data = cursor.fetchall()

# for row in selected_data:
    # print(row)

connection = create_connection()
print(connection)

# Closing the connection
# cursor.close()
connection.close()

def main():
    connection = create_connection()
    print(connection)
    i = 0

    while i == 0:
        print("Welcome to Password Manager v.1")
        i = -1


if __name__ == "__main__":
    main()
