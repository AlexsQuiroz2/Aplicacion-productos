
import sqlite3
from tkinter import ttk
from tkinter import *
from zlib import DEF_BUF_SIZE



class Product:
    
    db_name='database.db'
    
    def __init__(self, window):
        self.wind = window
        self.wind.title('Products Application')
        
        #Crear un contenedor
        frame = LabelFrame(self.wind, text = 'Registrar un nuevo producto')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)
        
        #Nombre del input
        Label(frame, text = 'Name: ').grid(row = 1, column = 0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)
        
        #Price input
        Label(frame, text = 'Precio: ').grid(row = 2, column = 0)
        self.price = Entry(frame)
        self.price.grid(row = 2, column = 1)
        
        #Button at product
        ttk.Button(frame, text ='Save product', command=self.add_product).grid(row=3, columnspan=2, sticky=W + E)
        
        #table
        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='Name', anchor=CENTER)
        self.tree.heading('#1', text='Price', anchor=CENTER)
        
        self.get_products()
        
    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result=cursor.execute(query, parameters)
            conn.commit()
        return result
    
    def get_products(self):
        #cleaning tables
        records=self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # quering dates
        query = 'SELECT * FROM  product ORDER BY name DESC'
        db_rows=self.run_query(query)
        for row in db_rows:
            self.tree.insert('', 0, text= row[1], values=row[2])
    
    
    def validations(self):
        return len(self.name.get()) != 0 and len(self.price.get()) != 0
            
    def add_product(self):
        if self.validations():
            print(self.name.get)
            print(self.price.get)
        else:
            print('Name and price is required')
    
if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
    