import sys
import Werset
from BibleStats import biblia, books
from PyQt6.QtWidgets import QApplication, QComboBox, QLabel, QWidget, QGridLayout , QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import math

chapters = []
verses = []


BibliaPL = Werset.Biblia("PolishBible.xml")
BibliaEN = Werset.Biblia("EnglishNKJBible.xml")
BibliaUK = Werset.Biblia("UkrainianBible.xml")

title = BibliaPL.returnTitle()

app = QApplication(sys.argv)
versesWindow = QWidget()
versesWindowLayout = QGridLayout()

blindButton = QPushButton()
showButton = QPushButton()

nextButton = QPushButton()
prevButton = QPushButton()

versesWindow.setStyleSheet("background-color: black;")

def adjust_font_size(label, text, base_height, base_width):
    min_font_size = 12  # większe minimum
    max_font_size = int(base_height * 0.35)  # większe maksimum
    k = 1.2  # mniejszy współczynnik, czcionka będzie większa
    c = 10   # większa stała, mniej wpływu długości tekstu
    avg_char_width = 0.8  # większa szerokość znaku, czcionka będzie większa

    font_size_h = int(base_height * k / (math.log(len(text) + c)))
    font_size_w = int(base_width / (len(text) * avg_char_width)) if len(text) > 0 else max_font_size

    font_size = max(min_font_size, min(max_font_size, min(font_size_h, font_size_w)))
    label.setFont(QFont("Arial", font_size))
    label.setText(text)


#stworzenie trzymadła an wersety
qVerseP = QLabel(BibliaPL.returnVerses(),versesWindow) 
qVerseE = QLabel(BibliaEN.returnVerses(),versesWindow)
qVerseU = QLabel(BibliaUK.returnVerses(),versesWindow)

qTitle = QLabel(title, versesWindow)
qTitle.setFont(QFont("Arial", int(versesWindow.height() * 0.05)))  # Stały, większy rozmiar czcionki dla tytułu
#zmiana rozmiaru 
qVerseP.setFont(QFont("Arial",int(versesWindow.height() * 0.05)))
qVerseE.setFont(QFont("Arial",int(versesWindow.height() * 0.05)))
qVerseU.setFont(QFont("Arial",int(versesWindow.height() * 0.05)))
for label in [qVerseP, qVerseE, qVerseU, qTitle]:
    label.setStyleSheet("color: white; background-color: transparent;")
#wysrodkowanie
qVerseP.setAlignment(Qt.AlignmentFlag.AlignCenter)
qVerseE.setAlignment(Qt.AlignmentFlag.AlignCenter)
qVerseU.setAlignment(Qt.AlignmentFlag.AlignCenter)
qTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
#zawijanie wersetu 
qVerseP.setWordWrap(True)
qVerseE.setWordWrap(True)
qVerseU.setWordWrap(True)
#umiejscowienie
versesWindowLayout.addWidget(qVerseP, 0, 0 )
versesWindowLayout.addWidget(qVerseE, 1, 0)
versesWindowLayout.addWidget(qVerseU, 2, 0)
versesWindowLayout.addWidget(qTitle, 3, 0)

# Przechwytywanie wydarzeń klawiatury

show = True
def keyPressEvent(event):
    global show
    if event.key() == Qt.Key.Key_Right:  # Strzałka w prawo
        nextVerse()
    if event.key() == Qt.Key.Key_Left:  # Strzałka w lewo
        prevVerse()
    if event.key() == Qt.Key.Key_B and show:  # blind
        blind()
        show = False
    elif event.key() == Qt.Key.Key_B and not show:
        updateVerses()
        show = True
    if event.key() == Qt.Key.Key_Escape:  # Escape
        app.quit()
    if event.key() == Qt.Key.Key_F:
        if versesWindow.isFullScreen():
            versesWindow.showNormal()
        else:
            versesWindow.showFullScreen()
       
def updateVerses():
    verse_num = BibliaPL.currentVerse
    verse_num_en = BibliaEN.currentVerse
    verse_num_uk = BibliaUK.currentVerse

    pl_text = f"{verse_num}. {BibliaPL.returnVerses()}"
    en_text = f"{verse_num_en}. {BibliaEN.returnVerses()}"
    uk_text = f"{verse_num_uk}. {BibliaUK.returnVerses()}"

    adjust_font_size(qVerseP, pl_text, versesWindow.height(), versesWindow.width())
    adjust_font_size(qVerseE, en_text, versesWindow.height(), versesWindow.width())
    adjust_font_size(qVerseU, uk_text, versesWindow.height(), versesWindow.width())

    qVerseP.setText(pl_text)
    qVerseE.setText(en_text)
    qVerseU.setText(uk_text)
    qTitle.setText(BibliaPL.returnTitle())
    qTitle.setFont(QFont("Arial", int(versesWindow.height() * 0.05)))

def nextVerse():
    BibliaEN.next()
    BibliaPL.next()
    BibliaUK.next()
    updateVerses()
    setMenuVerses(BibliaPL.currentBook,BibliaPL.currentChapter,BibliaPL.currentVerse)

def prevVerse():
    BibliaEN.prev()
    BibliaPL.prev()
    BibliaUK.prev()
    updateVerses()
    setMenuVerses(BibliaPL.currentBook,BibliaPL.currentChapter,BibliaPL.currentVerse)

    
versesWindow.keyPressEvent = keyPressEvent

#okno 2
menu = QWidget()
menuLayout = QGridLayout()
menu.keyPressEvent = keyPressEvent
comboBoxBooks = QComboBox()
comboBoxChapters = QComboBox()
comboBoxVerses = QComboBox()



comboBoxBooks.addItems(books)

previewCurrent = QLabel("",menu)
previewPrev = QLabel("",menu)
previewNext = QLabel("",menu)

previewCurrent.setWordWrap(True)
previewPrev.setWordWrap(True)
previewNext.setWordWrap(True)

menuLayout.addWidget(comboBoxBooks,1,1)
menuLayout.addWidget(comboBoxChapters,1,2)
menuLayout.addWidget(comboBoxVerses,1,3)

menuLayout.addWidget(previewPrev,3,0,1,4)
menuLayout.addWidget(previewCurrent,4,0,1,4)
menuLayout.addWidget(previewNext,5,0,1,4)


def updateComboBoxes():
    updateComboBoxChapters()
    updateComboBoxVerses()
    BibliaEN.setVerse(comboBoxBooks.currentIndex(),comboBoxChapters.currentIndex(),comboBoxVerses.currentIndex())
    BibliaPL.setVerse(comboBoxBooks.currentIndex(),comboBoxChapters.currentIndex(),comboBoxVerses.currentIndex())
    BibliaUK.setVerse(comboBoxBooks.currentIndex(),comboBoxChapters.currentIndex(),comboBoxVerses.currentIndex())

def updateComboBoxChapters():
      
    chapters.clear()
    for x in range(1,biblia[comboBoxBooks.currentText()]['chapters']+1):
        chapters.append(str(x))
    comboBoxChapters.clear()  
    comboBoxChapters.addItems(chapters)
    

def updateComboBoxVerses():
    if comboBoxChapters.currentText() != "":
        verses.clear()
        for x in range(1,biblia[comboBoxBooks.currentText()]['verses'][int(comboBoxChapters.currentText())]+1):
            verses.append(str(x))
        comboBoxVerses.clear() 
        comboBoxVerses.addItems(verses)
def blind():
    qVerseP.setText("")
    qVerseE.setText("")
    qVerseU.setText("")
    qTitle.setText("")

def setMenuVerses(book,chapter,verse):
    comboBoxBooks.setCurrentIndex(book - 1)
    comboBoxChapters.setCurrentIndex(chapter - 1)
    comboBoxVerses.setCurrentIndex(verse - 1)

def updateVerse():
    BibliaEN.setVerse(comboBoxBooks.currentIndex(),comboBoxChapters.currentIndex(),comboBoxVerses.currentIndex())
    BibliaPL.setVerse(comboBoxBooks.currentIndex(),comboBoxChapters.currentIndex(),comboBoxVerses.currentIndex())
    BibliaUK.setVerse(comboBoxBooks.currentIndex(),comboBoxChapters.currentIndex(),comboBoxVerses.currentIndex())
    
    previewCurrent.setText(str(comboBoxVerses.currentIndex()+ 1) +". "+ BibliaPL.returnVerses())
    previewNext.setText(str(comboBoxVerses.currentIndex() + 2) +". "+ BibliaPL.returnNextVerses())
    previewPrev.setText(str(comboBoxVerses.currentIndex() ) +". "+ BibliaPL.returnPrevVerses())

updateComboBoxes()
comboBoxBooks.currentIndexChanged.connect(updateComboBoxes)
comboBoxChapters.currentIndexChanged.connect(updateComboBoxVerses)
comboBoxVerses.currentIndexChanged.connect(updateVerse)
blindButton.setText("Blind")
blindButton.clicked.connect(blind)
menuLayout.addWidget(blindButton,2,3)

showButton.setText("Show")
showButton.clicked.connect(updateVerses)
menuLayout.addWidget(showButton,2,1)


nextButton.setText("-->")
nextButton.clicked.connect(nextVerse)
menuLayout.addWidget(nextButton,2,4)

prevButton.setText("<--")
prevButton.clicked.connect(prevVerse)
menuLayout.addWidget(prevButton,2,0)


screen_geometry = app.primaryScreen().geometry()  
menu.setGeometry(int(screen_geometry.width() / 2), int(screen_geometry.height() / 2), 600, 200)
menu.setWindowTitle("BibleVerses")

menu.setLayout(menuLayout)
menu.show()

def closeEvent(event):
    app.quit()
versesWindow.setLayout(versesWindowLayout)
versesWindow.show()
app.exec()