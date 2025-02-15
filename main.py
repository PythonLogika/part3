from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

import json

notes = {
    "Ласкаво просимо": {
        "текст": "Це додаток для заміток",
        "теги": ["додаток", "замітка"]
    }
}

with open("notes_data.json", "w") as file:
    json.dump(notes, file)

app = QApplication([])

notes_win = QWidget()
notes_win.setWindowTitle("Smart Notes")
notes_win.resize(900, 600)

list_notes = QListWidget()
list_notes_label = QLabel("Список заміток")

button_note_create = QPushButton("Створити замітку")
button_note_save = QPushButton("Зберегти замітку")
button_note_del = QPushButton("Видалити замітку")

field_tag = QLineEdit("")
field_tag.setPlaceholderText("Введіть тег...")

field_text = QTextEdit()

button_tag_add = QPushButton("Додати тег")
button_tag_del = QPushButton("Видалити тег")
button_tag_search = QPushButton("Шукати по тегу")

list_tags = QListWidget()
list_tags_label = QLabel("Список тегів")

# створюємо лейаути
layout_notes = QHBoxLayout()

col_1 = QVBoxLayout()
col_1.addWidget(field_text)

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_save)

row_2 = QHBoxLayout()
row_2.addWidget(button_note_del)

col_2.addLayout(row_1)
col_2.addLayout(row_2)

col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)

row_3 = QHBoxLayout()
row_1.addWidget(button_tag_add)
row_1.addWidget(button_tag_del)

row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch=2)
layout_notes.addLayout(col_2, stretch=1)
notes_win.setLayout(layout_notes)

def add_note():
    note_name, ok = QInputDialog.getText(notes_win, "Додати замітку", "Назва замітки")

    if ok and note_name != "":
        notes[note_name] = {"текст": "", "теги": []}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]["теги"])
        print(notes) 

def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]["текст"])
    list_tags.clear()
    list_tags.addItems(notes[key]["теги"])

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["текст"] = field_text.toPlainText()

        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Замітка для збереження не вибрана!")

def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)

        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)

        print(notes)
    else:
        print("Замітка для видалення не вибрана")

list_notes.itemClicked.connect(show_note)
button_note_save.clicked.connect(save_note)
button_note_del.clicked.connect(del_note)
button_note_create.clicked.connect(add_note)

notes_win.show()

with open("notes_data.json", "r") as file:
    notes = json.load(file)

app.exec_()
