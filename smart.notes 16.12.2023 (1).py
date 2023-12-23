from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QTableWidget, QListWidget, QListWidgetItem,
QLineEdit, QFormLayout, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox, QTextEdit, QInputDialog)

import json

app=QApplication([])

notes = {
    "Ласкаво просимо!"   : {
        "текст" : "Це найкращий додаток для заміток у світі!",
        "теги"  : ["добро", "інструкція"]
    }
}
with open("notes_data.json", "w") as file:
    json.dump(notes, file)


window = QWidget()
window.setWindowTitle("Розумні замітки")

window.resize(900,600)
window.move(600,300)

text = QTextEdit()
text.setText("Це найкращий додаток")
text.setStyleSheet("background-color:yellow; color:black; border: 3px solid black; border-radius:20px")
notes1 = QLabel("Cписок заміток")
notes1.setStyleSheet("background-color:yellow; color:black; border: 3px solid black; border-radius:30px")

notes2 = QLabel("Список тегів")
notes2.setStyleSheet("background-color:yellow; color:black; border: 3px solid black; border-radius:30px")

but1 = QPushButton("Створити замітку")
but1.setStyleSheet("background-color:blue; color:white; border: 3px solid black; border-radius:30px")





but2 = QPushButton("Видалити замітку")
but2.setStyleSheet("background-color:blue; color:white; border: 3px solid black; border-radius:30px")
but3 = QPushButton("Зберегти замітки")
but3.setStyleSheet("background-color:blue; color:white; border: 3px solid black; border-radius:30px")
but4 = QPushButton("Додати до замітки")
but4.setStyleSheet("background-color:blue; color:white; border: 3px solid black; border-radius:30px")
but5 = QPushButton("Відкріпити від замітки")
but5.setStyleSheet("background-color:blue; color:white; border: 3px solid black; border-radius:30px")
but6 = QPushButton("Шукати замітки по тегу")
but6.setStyleSheet("background-color:blue; color:white; border: 3px solid black; border-radius:30px")


items1 = QListWidget()
items2  =QListWidget()
line = QLineEdit()
line.setPlaceholderText("Введіть тег...")
line.setStyleSheet("background-color:yellow; color:blac; border: 3px solid black; border-radius:30px")



line_mainH = QHBoxLayout()
line_V1 = QVBoxLayout()
line_V2 = QVBoxLayout()
line_H1 = QHBoxLayout()
line_H2 = QHBoxLayout()


line_V1.addWidget(text)
line_H1.addWidget(but1)
line_H1.addWidget(but2)
line_H2.addWidget(but4)
line_H2.addWidget(but5)

line_V2.addWidget(notes1)
line_V2.addWidget(items1)
line_V2.addLayout(line_H1)
line_V2.addWidget(but3)
line_V2.addWidget(notes2)
line_V2.addWidget(items2)
line_V2.addWidget(line)
line_V2.addLayout(line_H2)
line_V2.addWidget(but6)

line_mainH.addLayout(line_V1, stretch=2)
line_mainH.addLayout(line_V2, stretch=1)
window.setLayout(line_mainH)

def add_note():
    note_name, ok = QInputDialog.getText(window, "Додати замітку", "Назва замітки: ")
    if ok and note_name !="":
        notes[note_name] = {"текст" : "", "теги" :[]}
        items1.addItem(note_name)
        items2.addItems(notes[note_name]["теги"])
        print(notes)

def show_note():
    key = items1.selectedItems()[0].text()
    print(key)
    text.setText(notes[key]["текст"])
    items2.clear()
    items2.addItems(notes[key]["теги"])


def save_note():
    if items1.selectedItems():
        key = items1.selectedItems()[0].text()
        notes[key]["текст"] = text.toPlainText()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Замітка для збереження не вибрана!")


def del_note():
    if items1.selectedItems():
        key = items1.selectedItems()[0].text()
        del notes[key]
        items1.clear()
        items2.clear()
        text.clear()
        items1.addItems(notes)
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Замітка для вилучення не обрана!")


def add_tag():
    if items1.selectedItems():
        key = items1.selectedItems()[0].text()
        tag = line.text()
        if not tag in notes[key]["теги"]:
            notes[key]["теги"].append(tag)
            items2.addItem(tag)
            line.clear()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Замітка для збереження не обрана!")


def del_tag():
    if items2.selectedItems():
        key = items1.selectedItems()[0].text()
        tag = items2.selectedItems()[0].text()
        notes[key]["теги"].remove(tag)
        items2.clear()
        items2.addItems(notes[key]["теги"])
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print("Тег для вилучення не обраний!")

def search_tag():
    print(but6.text())
    tag = line.text()
    if but6.text() == "Шукати замітки по тегу" and tag:
        print(tag)
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]["теги"]:
                notes_filtered[note]=notes[note]
        but6.setText("Скинути пошук")
        items1.clear()
        items2.clear()
        items1.addItems(notes_filtered)
        print(but6.text())
    elif but6.text() == "Скинути пошук":
        line.clear()
        items1.clear()
        items2.clear()
        items1.addItems(notes)
        but6.setText("Шукати замітки по тегу")
        print(but6.text())
    else:
        pass







but1.clicked.connect(add_note)
items1.itemClicked.connect(show_note)
but3.clicked.connect(save_note)
but2.clicked.connect(del_note)
but4.clicked.connect(add_tag)
but5.clicked.connect(del_tag)
but6.clicked.connect(search_tag)





window.show()



with open("notes_data.json", "r") as file:
    notes = json.load(file)
items1.addItems(notes)

app.exec_()