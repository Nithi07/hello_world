import sqlite3

conn = sqlite3.connect('p_details.sqlite')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS data')

c.execute('''CREATE TABLE data ('name' TEXT, 'state' TEXT, 'email' TEXT)''')

values = [('nithi', 'tamilnadu', 'nithi@gmil.com'),
          ('elango', 'tamilnadu', 'elango@gmail.com'),
          ('vijay', 'karnataka', 'vijay@gmail.com')]

c.executemany('INSERT INTO data (name, state, email) VALUES (?,?,?)', values)

conn.commit()

a = c.fetchall()
print(a)
# HOW TO PRINT OUTPUT-------------------------
