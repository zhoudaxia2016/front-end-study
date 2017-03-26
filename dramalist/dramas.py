import sqlite3

def createTable():
  conn = sqlite3.connect('dramas.db')
  cu = conn.cursor()

  cu.execute('''create table dramas
          (name text not null,
          isSeen int not null,
          type int not null)''')
  conn.commit()
  conn.close()
  
def delete():
  conn = sqlite3.connect('dramas.db')
  cu = conn.cursor()
  cu.execute('delete  from dramas')
  conn.commit()
  conn.close()

if __name__ == '__main__':
  createTable()
