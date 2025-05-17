import sys
import Werset
from BibleStats import biblia, books
from PyQt6.QtWidgets import QApplication, QComboBox, QLabel, QWidget, QGridLayout , QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

chapters = []
verses = []


BibliaPL = Werset.Biblia("PolishBible.xml")
BibliaEN = Werset.Biblia("EnglishNKJBible.xml")
BibliaUK = Werset.Biblia("UkrainianBible.xml")

title = BibliaPL.returnTitle()

app = QApplication(sys.argv)
screen = QWidget()
screenLayout = QGridLayout()

blindButton = QPushButton()
showButton = QPushButton()

nextButton = QPushButton()
prevButton = QPushButton()





#stworzenie trzymadła an wersety
qVerseP = QLabel(BibliaPL.returnVerses(),screen) 
qVerseE = QLabel(BibliaEN.returnVerses(),screen)
qVerseU = QLabel(BibliaUK.returnVerses(),screen)
qTitle = QLabel(title,screen)
#zmiana rozmiaru 
qVerseP.setFont(QFont("Arial",int(screen.height() * 0.05)))
qVerseE.setFont(QFont("Arial",int(screen.height() * 0.05)))
qVerseU.setFont(QFont("Arial",int(screen.height() * 0.05)))
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
screenLayout.addWidget(qVerseP, 0, 0 )
screenLayout.addWidget(qVerseE, 1, 0)
screenLayout.addWidget(qVerseU, 2, 0)
screenLayout.addWidget(qTitle, 3, 0)

# Przechwytywanie wydarzeń klawiatury

#TODO blind na b
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
       
def updateVerses():
    qVerseP.setFont(QFont("Arial",int(screen.height() * 0.05)))
    qVerseE.setFont(QFont("Arial",int(screen.height() * 0.05)))
    qVerseU.setFont(QFont("Arial",int(screen.height() * 0.05)))
    qVerseP.setText(BibliaPL.returnVerses())
    qVerseE.setText(BibliaEN.returnVerses())
    qVerseU.setText(BibliaUK.returnVerses())
    title = BibliaPL.returnTitle()
    qTitle.setText(title)

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

    
screen.keyPressEvent = keyPressEvent

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





menu.setLayout(menuLayout)
menu.show()
#wyswietlanie okien
screen.setLayout(screenLayout)
screen.show()
app.exec()