import sqlite3 as sql
# Tablo Oluşturma         ->  CREATE TABLE tablo-ismi (kolon1 TEXT, kolon2 İNT, kolon3 TEXT)
# Tablo Oluşturma         ->  CREATE TABLE IF NOT EXISTS tablo-ismi (kolon1 TEXT, kolon2 İNT, kolon3 TEXT)
# Tabloya Kayıt Atma      ->  INSERT INTO tablo-ismi VALUES (val1, val2, val3)
# Tablodan Veri Çekme     ->  SELECT * FROM tablo-ismi
# Tablodan Veri Çekme     ->  SELECT kolon1, kolon2, kolon3 FROM tablo-ismi
# Tablodan Veri Çekme     ->  SELECT kolon1, kolon2, kolon3 FROM tablo-ismi WHERE kolon1 = value1
# Tablo Veri Güncelleme   ->  UPDATE tablo-ismi SET kolonx = valx WHERE kolon1 = val1
# Tablodan Veri Silme     -> DELETE FROM tablo-ismi WHERE kolon1 = val1



con = sql.connect('student.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS grades (name TEXT, lesson TEXT, grade INT)')




# cur.execute("INSERT INTO grades VALUES ('Burak', 'Matematik', 95)")
# cur.execute("INSERT INTO grades VALUES ('veysel', 'Matematik', 47)")
# cur.execute("INSERT INTO grades VALUES ('özlem', 'fizik', 67)")
# cur.execute("INSERT INTO grades VALUES ('ömür', 'kimya', 15)")
# cur.execute("INSERT INTO grades VALUES ('tuğberk Ok', 'türkçe', 78)")
#
# cur.execute("SELECT * FROM grades")
# data = cur.fetchall()
# for line in data:
#     print(line)




# cur.execute('SELECT * FROM grades')
# data = cur.fetchall()
#
# print(data)
# print(type(data))
#
# for val in data:
#     print(val)
#     print(type(val))





# cur.execute("SELECT name, grade FROM grades")
# data = cur.fetchall()

# for val1 in data:
#     print(val1)





# cur.execute("SELECT * FROM grades WHERE lesson = 'Matematik' ")
# data = cur.fetchall()
#
# for val1 in data:
#     print(val1)





# cur.execute(" SELECT * FROM grades WHERE grade >= 90")
# data = cur.fetchall()
#
# for val5 in data:
#     print(val5)






# cur.execute("UPDATE grades SET grade = 88 WHERE lesson = 'Matematik' ")
# cur.execute("UPDATE grades SET grade = 12 where name = 'ömür' ")
# cur.execute("SELECT * FROM grades")
# data = cur.fetchall()
#
# for satir in data:
#     print(satir)






# cur.execute("DELETE FROM grades WHERE lesson = 'türkçe' ")
#
# cur.execute("SELECT * FROM grades")
# data = cur.fetchall()
#
# for satir in data:
#     print(satir)


# cur.execute("DELETE FROM grades")    # bütün değerleri siler





con.commit()
con.close()
