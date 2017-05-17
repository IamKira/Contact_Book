"""
Address Book Database

Этот файл создает, изменяет(вставляет, удаляет, обновляет) и запрашивает базу SQLite, которая заполнена (или будет заполнена) записями адресной книги.
"""

import sqlite3 as sql
import os.path as path
import config as cfg


def db_init(db_name):
	"""Создать/Открыть и инициализировать базу данных

	Keyword arguments:
	db_name -- имя нового файла бд
	"""	

	if db_exists(db_name) == True:
		cfg.DB = sql.connect(db_name + '.ab')
		cfg.C = cfg.DB.cursor()
		print('Database already exists')

	else:
		cfg.DB = sql.connect(db_name + '.ab')
		cfg.C = cfg.DB.cursor()
		create_table = '''CREATE TABLE Contacts(First TEXT, 
					Last TEXT, Street1 TEXT, Street2 TEXT, City TEXT, State TEXT,
					Zip TEXT, Home TEXT, Mobile TEXT, Email TEXT, Birthday TEXT, 
					Notes TEXT) '''	
		cfg.C.execute(create_table)
		cfg.DB.commit()
		print('New table created')
	

def db_exists(db_name):
	"""Проверяет, существует ли бд

	Keyword arguments:
	db_name -- имя файла бд
	"""

	if (path.isfile(db_name + '.ab')):
		return True
	else:
		return False


def get_id(entry):
	"""Получает идентификатор бд из записи

	Keyword arguments:
	entry - Объект списка
	"""

	entry_id = "SELECT rowid, * FROM Contacts WHERE First = ? AND Last = ?"
	cfg.C.execute(entry_id, [entry[0], entry[1]])

	for row in cfg.C:
		return row[0]


def insert_entry(entry):
	"""Вставляет новую запись в бд

	Keyword arguments:
	entry -- объект списка
	"""

	cfg.C.execute('INSERT INTO Contacts VALUES (?,?,?,?,?,?,?,?,?,?,?,?)',
		entry)

	cfg.DB.commit()


def delete_entry(entry_id):
	"""Удаляет запись из бд

	Keyword arguments:
	entry_id -- соответствующий идентификационный номер для записи
	"""

	cfg.C.execute("DELETE FROM Contacts WHERE rowid = ?", [entry_id])


def get_entry(entry_id):
	"""Запрос на чтение записи из дб

	Keyword arguments:
	entry_id -- соответствующий идентификационный номер для записи
	"""

	cfg.C.execute("SELECT * FROM Contacts WHERE rowid = ?", [entry_id])

	return cfg.C


def db_commit():
	"""Фиксирует все изменения в бд"""
	cfg.DB.commit()


def edit_entry(entry_id, entry):
	"""Обновляет запись в бд

	Keyword arguments:
	entry_id -- соответствующий идентификационный номер для записи
	entry -- объект списка
	"""
	entry_update = '''UPDATE Contacts SET First = ?, Last = ?, Street1 = ?,
			Street2 = ?, City = ?, State = ?, Zip = ?, Home = ?, Mobile = ?, 
			Email = ?, Birthday = ?, Notes = ? WHERE rowid = ? '''

	cfg.C.execute(entry_update, [entry[0], entry[1], entry[2], entry[3], 
		entry[4], entry[5], entry[6], entry[7], entry[8], entry[9], entry[10],
		entry[11], '{}'.format(entry_id)])


def query_entrylist(sort):
	"""Вывод полного списка записей в бд

	Keyword arguments:
	sort -- Строка, содержащая способ сортировки
	"""
	if sort == 'Last Name':
		last_name = '''SELECT * FROM Contacts ORDER BY Last ASC, First ASC'''
		cfg.C.execute(last_name)

	elif sort == 'Zip':
		zip_code = '''SELECT * FROM Contacts ORDER BY Zip ASC, Last ASC'''
		cfg.C.execute(zip_code)

	return cfg.C


def search_entry(str, sort):
	"""Сортировка записей

	Keyword arguments:
	str -- строка, содержащая поисковый запрос
	sort -- сортировка по строкам
	"""
	if sort == 'Last Name':
		search_last = '''SELECT * FROM Contacts WHERE (First || Last || Street1 || 
				Street2 || City || State || Zip || Home || Mobile || Email || 
				Birthday || Notes) LIKE '%' || ? || '%' ORDER BY Last ASC, First ASC'''
		cfg.C.execute(search_last, [str]) 

	elif sort == 'Zip':
		search_zip = '''SELECT * FROM Contacts WHERE (First || Last || Street1 || 
				Street2 || City || State || Zip || Home || Mobile || Email || 
				Birthday || Notes) LIKE '%' || ? || '%' ORDER BY Zip ASC, Last ASC'''
		cfg.C.execute(search_zip, [str]) 

	return cfg.C