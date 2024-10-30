import xml.etree.ElementTree as ET 
from BibleStats import biblia,ksiegi
class Biblia:
    def __init__(self, biblexml):
        self.biblia = biblia
        self.ksiegi = ksiegi

        self.parse = ET.parse(biblexml)
        self.bible = self.parse.getroot()

        self.currentVerse = 1
        self.currentChapter = 1
        self.currentBook = 1

    def returnVerses(self):
        bookN = 'book[@number="{}"]'.format(self.currentBook)
        chapterN = 'chapter[@number="{}"]'.format(self.currentChapter)
        verseN = 'verse[@number="{}"]'.format(self.currentVerse)
        for testament in self.bible.findall('testament'):
            for book in testament.findall(bookN):
                for chapter in book.findall(chapterN): 
                    verse = chapter.find(verseN)
                    if verse is not None: 
                        return verse.text
                
         
    def next(self):
        self.currentVerse +=1
        if self.biblia[self.ksiegi[self.currentBook]]["verses"][self.currentChapter] < self.currentVerse:
            self.currentChapter+=1
            self.currentVerse = 1
        if  self.biblia[self.ksiegi[self.currentBook]]["chapters"] < self.currentChapter:
            self.currentBook +=1
            self.currentChapter = 1
            self.currentVerse = 1
        self.returnVerses()

#TODO cofanie do poprzedniego rozdziału ostatni werset 
#cofajnie do osatniego wersetu
    def prev(self):
        
        self.currentVerse -=1
        if self.currentVerse <=0:
            self.currentChapter-=1
            self.currentVerse = 1
        if  self.currentChapter <=0:
            self.currentBook -=1
            self.currentChapter = 1
            self.currentVerse = 1
        if self.currentBook <=0:
            self.currentBook =1
        self.returnVerses()

    def returnTitle(self):
        title = "{} {},{}".format(self.ksiegi[self.currentBook],self.currentChapter,self.currentVerse)
        return title
    
    def setVerse(self,book,chapter,verse):
        self.currentBook = book + 1
        self.currentChapter = chapter + 1
        self.currentVerse = verse + 1 
