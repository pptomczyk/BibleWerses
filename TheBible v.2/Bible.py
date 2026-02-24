import sys
import Werset
from BibleStats import biblia, books
from PyQt6.QtWidgets import QApplication, QCheckBox, QComboBox, QLabel, QWidget, QGridLayout , QPushButton
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

def bigerFontSize(label):
    current_font = label.font()
    current_size = current_font.pointSize()
    new_size = max(12, current_size + 2)  # Minimalna wielkość to 12
    label.setFont(QFont(current_font.family(), new_size))

def smallerFontSize(label):
    current_font = label.font()
    current_size = current_font.pointSize()
    new_size = max(12, current_size - 2)  # Minimalna wielkość to 12
    label.setFont(QFont(current_font.family(), new_size))

showEnglish = True;
showUkrainian = True;

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

def rebuildWindow():
    versesWindowLayout.removeWidget(qVerseP)
    versesWindowLayout.removeWidget(qVerseE)    
    versesWindowLayout.removeWidget(qVerseU)
    versesWindowLayout.removeWidget(qTitle)
    versesWindowLayout.setRowStretch(0, 1)
    versesWindowLayout.setRowStretch(1, 0)
    versesWindowLayout.setRowStretch(2, 0)
    if showEnglish and showUkrainian:
        versesWindowLayout.addWidget(qVerseP, 0, 0)
        versesWindowLayout.addWidget(qVerseE, 1, 0)
        versesWindowLayout.addWidget(qVerseU, 2, 0)
        versesWindowLayout.setRowStretch(0, 1)
        versesWindowLayout.setRowStretch(2, 1)
    elif showEnglish and not showUkrainian:
        versesWindowLayout.addWidget(qVerseP, 0, 0)
        versesWindowLayout.addWidget(qVerseE, 1, 0)
        versesWindowLayout.setRowStretch(0, 1)
        versesWindowLayout.setRowStretch(1, 1)
    elif not showEnglish and showUkrainian:
        versesWindowLayout.addWidget(qVerseP, 0, 0)
        versesWindowLayout.addWidget(qVerseU, 1, 0)
        versesWindowLayout.setRowStretch(0, 1)
        versesWindowLayout.setRowStretch(1, 1)
    elif not showEnglish and not showUkrainian:
        versesWindowLayout.addWidget(qVerseP, 0, 0)
        versesWindowLayout.setRowStretch(0, 2)
    versesWindowLayout.addWidget(qTitle, 3, 0)
    #layout rozciagnac na całe okno
        

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
    if event.key() == Qt.Key.Key_Plus:
        bigerFontSize(qVerseP)
        bigerFontSize(qVerseE)
        bigerFontSize(qVerseU)
    if event.key() == Qt.Key.Key_Minus:
        smallerFontSize(qVerseP)
        smallerFontSize(qVerseE)
        smallerFontSize(qVerseU)    
       
def updateVerses():
    verse_num = BibliaPL.currentVerse
    verse_num_en = BibliaEN.currentVerse
    verse_num_uk = BibliaUK.currentVerse

    pl_text = f"{verse_num}. {BibliaPL.returnVerses()}"
    en_text = f"{verse_num_en}. {BibliaEN.returnVerses()}"
    uk_text = f"{verse_num_uk}. {BibliaUK.returnVerses()}"


    qVerseP.setText(pl_text)
    if showEnglish: qVerseE.setText(en_text) 
    else: qVerseE.setText("")
    if showUkrainian: qVerseU.setText(uk_text) 
    else: qVerseU.setText("")

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
showEnglishCheckBox = QCheckBox("Angielski")
showUkrainianCheckBox = QCheckBox("Ukraiński")

bigerfontButton = QPushButton("+")
lowerfontButton = QPushButton("-")

fullscreenButton = QPushButton("FullScreen")

bigerfontButton.clicked.connect(lambda: bigerFontSize(qVerseP))
bigerfontButton.clicked.connect(lambda: bigerFontSize(qVerseE))
bigerfontButton.clicked.connect(lambda: bigerFontSize(qVerseU))
lowerfontButton.clicked.connect(lambda: smallerFontSize(qVerseP)) 
lowerfontButton.clicked.connect(lambda: smallerFontSize(qVerseE))
lowerfontButton.clicked.connect(lambda: smallerFontSize(qVerseU))
fullscreenButton.clicked.connect(lambda: versesWindow.showFullScreen() if not versesWindow.isFullScreen() else versesWindow.showNormal())

showEnglishCheckBox.setChecked(True)
showUkrainianCheckBox.setChecked(True)

def toggleLanguage():
    global showEnglish, showUkrainian
    showEnglish = showEnglishCheckBox.isChecked()
    showUkrainian = showUkrainianCheckBox.isChecked()
    rebuildWindow()
    updateVerses()

showUkrainianCheckBox.stateChanged.connect(lambda: toggleLanguage())    
showEnglishCheckBox.stateChanged.connect(lambda: toggleLanguage())

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

menuLayout.addWidget(showEnglishCheckBox,0,0)
menuLayout.addWidget(showUkrainianCheckBox,0,1)

menuLayout.addWidget(bigerfontButton,0,2)
menuLayout.addWidget(lowerfontButton,0,3)

menuLayout.addWidget(fullscreenButton,0,4)


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