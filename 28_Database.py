import sqlite3

db = sqlite3.connect("Ogrenci.db")

db.execute("drop table if exists notlar")

db.execute("create table notlar(id int, isim text, dersnot int)")

db.execute("insert into notlar(id, isim, dersnot) values(100, 'Hasan', 80)")
db.execute("insert into notlar(id, isim, dersnot) values(101, 'Ali', 90)")
db.execute("insert into notlar(id, isim, dersnot) values(102, 'Ayşe', 95)")
db.execute("insert into notlar(id, isim, dersnot) values(103, 'Metin', 87)")
db.execute("insert into notlar(id, isim, dersnot) values(104, 'Selin', 100)")

db.commit()

sorgu = db.execute("Select * from notlar order by id")
for satir in sorgu: print(satir)

print("*" * 30)
sorgu = db.execute("select * from notlar where isim = 'Metin'")
for satir in sorgu: print(satir)

print("*" * 30)
sorgu = db.execute("select * from notlar where dersnot >=90")
for satir in sorgu: print(satir)

print("*" * 30)
sorgu = db.execute("select isim, dersnot from notlar order by dersnot desc")
for satir in sorgu: print(satir)

print("*" * 30)
sorgu = db.execute("select isim, dersnot from notlar order by dersnot")
for satir in sorgu: print(satir)

