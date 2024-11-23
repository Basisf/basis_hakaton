import sqlite3
a = 'https://mbkuban.ru/documents/gosudarstvennaya-programma/*https://xn--90aifddrld7a.xn--p1ai/anticrisis/*https://admkrai.krasnodar.ru/*https://moibiz93.ru/*https://mbkuban.ru/*https://dirmsp.krasnodar.ru/activity/msp*'
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Regions (
Krasnodarskiykray TEXT
)
''')
cursor.execute('INSERT INTO Regions (Krasnodarskiykray) VALUES (?)', (f'{a}',))
connection.commit()
connection.close()