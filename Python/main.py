import getpass
from optparse import Values
import sqlite3

conn = sqlite3.connect('miaplicacion.db')

cursor = conn.cursor()

def main():
    createUser(4, "Julio", "Iglesias")
    createUser(5, "Fernando", "Ortiz")
    createUser(6, "Roseanne", "Park")
    createUser(7, "Lisa", "Manoban")
    createUser(8, "Kim", "Jisoo")
    cursor.close()
    conn.close()
    

def createUser(id, name, surname):

    rows = cursor.execute(f'insert into Alumnos(id, name, surname) Values({id}, "{name}", "{surname}")')
    
    data = rows.fetchone()
    conn.commit()
    if data == None:
        return False
    
    return True


def SearchUser(name):
    
    rows = cursor.execute(f'SELECT * from Alumnos WHERE name="{name}"')
    for row in rows:
        print(row)
    
    
        
    
if __name__ == '__main__':
    SearchUser("Leonel");
    main()

    
    
    

