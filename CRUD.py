# CRUD - CREATE, REMOVE, UPDATE, DELETE

import mysql.connector
try:

    conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="mysql",
    database="crud_python"
    )

    mycursor = conn.cursor()
    print("Connection Established");
except:
    print("Connection Error")

#CREATE DATABASE

# mycursor.execute("CREATE DATABASE crud_python")
# conn.commit()
#
# print("DATABASE CREATED")

# CREATE TABLE
# mycursor.execute(
#
#     """
#     CREATE TABLE customers(
#     id INTEGER PRIMARY KEY,
#     name VARCHAR(50) NOT NULL,
#     email VARCHAR(50) NOT NULL,
#     age INTEGER
#     )
#     """)
# conn.commit()
# print("Table is created")

# INSERT RECORDS INTO CUSTOMER TABLE

# mycursor.execute(
#     """
#     INSERT INTO customers VALUES
#     (1,"Anil", "anil@gmail.com",40),
#     (2,"Snil", "snil@gmail.com",20),
#     (3,"Mohan", "mohan@gmail.com",37)
#
#     """)
# conn.commit()
# print("Rows are inserted")

# READ: SELECT DATA FROM A TABLE

# mycursor.execute("select * from customers")
# myresult = mycursor.fetchall()
#print(myresult)
# for x in myresult:
#     print(x)

#UPDATE: UPDATE A DATA IN TABLE

# mycursor.execute("update customers set age=50 where id=1")
# conn.commit()
# print("update the record")

#DELETE

# mycursor.execute("delete from customers where id=1")
# conn.commit()
# print("Deleted")

import streamlit as st

#CREATE STREAMLITE WEB APP

def main():
    st.title("CRUD Operations with MYSQL")
    # Display Options for CRUD Operations
    option = st.sidebar.selectbox("Select an Operation", ("Create", "Read", "Update", "Delete"))
    # Perform Selected CRUD Operations
    if option == "Create":
        st.subheader("Create a Record")
        name = st.text_input("Enter Name")
        email = st.text_input("Enter Email")
        if st.button("Create"):
            sql = "insert into customers(name,email) values(%s,%s)"
            val = (name, email)
            mycursor.execute(sql, val)
            conn.commit()
            st.success("Record Created Successfully!!!")



    elif option == "Read":
        st.subheader("Read Records")
        st.subheader("Update a Record")
        mycursor.execute("select * from customers")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)




    elif option == "Update":
        st.subheader("Update a Record")
        id = st.number_input("Enter ID", min_value=1)
        name = st.text_input("Enter New Name")
        email = st.text_input("Enter New Email")
        if st.button("Update"):
            sql = "update customers set name=%s, email=%s where id =%s"
            val = (name, email, id)
            mycursor.execute(sql, val)
            conn.commit()
            st.success("Record Updated Successfully!!!")





    elif option == "Delete":
        st.subheader("Delete a Record")
        id = st.number_input("Enter ID", min_value=1)
        if st.button("Delete"):
            sql = "delete from customers where id =%s"
            val = (id,)
            mycursor.execute(sql, val)
            conn.commit()
            st.success("Record Deleted Successfully!!!")


if __name__ == "__main__":
    main()



