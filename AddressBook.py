"""
Main Address Book application

Authors: Rozum Roman and Danil Yandiev, 16.05.2017
"""

import sys
sys.path.insert(0, 'GUI')

import tkinter as Tk
import gui
import db
import new

def get_contact(contact):
	"""Возвращает контакты

	Keyword arguments:
	contact --  имя и фамилия контактной записи
	"""
	entry = []

	try:
		if contact.split()[1]:
			entry.append(contact.split()[0])
			entry.append(contact.split()[1])
	except:
		entry.append('')
		entry.append(contact.split()[0])

	for row in db.get_entry(db.get_id(entry)):
		return row


def add_contact(contact):
	"""Добавляет контакт в базу данных

	Keyword arguments:
	contact -- список, содержащий контактную информацию
	"""
	db.insert_entry(contact)


def remove_contact(contact):
	"""Удаляет контакт

	Keyword arguments:
	contact -- имя и фамилия контактной записи
	"""
	entry = []
	try:
		entry.append(contact.split()[0])
	except:
		entry.append('')

	try:
		entry.append(contact.split()[1])
	except:
		entry.append('');
	
	db.delete_entry(db.get_id(entry))


def edit_contact(entry_id, contact):
	"""Редактирует контакт.

	Keyword arguments:
	entry_id -- id строки для записи контакта
	contact -- список, содержащий контактную информацию
	"""
	db.edit_entry(entry_id, contact)


def search(search_string, sort):
	"""Ищет базу данных и возвращает результаты

	Keyword arguments:
	search_string -- (str) Поисковый запрос
	sort -- (str) Способ сортировки(Фамилия или индекс)
	"""
	return db.search_entry(search_string, sort)


if __name__ == "__main__":
    root = Tk.Tk()
    new.New_AddBookWindow(root)
    root.mainloop()
	