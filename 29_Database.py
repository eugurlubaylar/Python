import sqlite3

db = sqlite3.connect("Arabalar.db")

db.execute("drop table if exists modeller")

db.execute("create table modeller(id int, marka str, model_yili date, rengi str)")

db.execute("insert into modeller(id, marka, model_yili, rengi) values(001, 'Renault', 2002, 'kırmızı')")
db.execute("insert into modeller(id, marka, model_yili, rengi) values(002, 'Opel', 2011, 'mavi')")
db.execute("insert into modeller(id, marka, model_yili, rengi) values(003, 'Mercedes', 2009, 'beyaz')")
db.execute("insert into modeller(id, marka, model_yili, rengi) values(004, 'BMV', 2005, 'bej')")
db.execute("insert into modeller(id, marka, model_yili, rengi) values(005, 'Chervolet', 2014, 'siyah')")

db.commit()

sorgu = db.execute("select * from modeller order by id")
for satir in sorgu:
    print(*satir)


db.execute("update modeller set rengi = 'MOKKA' where marka = 'Mercedes'")
db.commit()

print("-" * 50)
sorgu = db.execute("select * from modeller order by id")
for satir in sorgu:
    print(*satir)

db.execute("delete from modeller where id = 004")
db.commit()

print("-" * 50)
sorgu = db.execute("select * from modeller order by id")
for satir in sorgu:
    print(*satir)
