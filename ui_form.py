from random import randint
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Japonais")
        MainWindow.setFixedWidth(1100)
        MainWindow.setFixedHeight(600)

        # La couleur de fond de la fenetre
        MainWindow.setAutoFillBackground(True)
        p = MainWindow.palette()
        p.setColor(MainWindow.backgroundRole(), QColor(246, 247, 242))
        MainWindow.setPalette(p)



        self.mButtonKanji = QCheckBox(MainWindow)
        self.mButtonKanji.setText("Kanji")
        self.mButtonKanji.move(100, 500)
        self.mButtonKanji.setToolTip("Raccourci : K")
        self.mButtonKanji.clicked.connect(MainWindow.Kanji)

        self.mButtonHiragana = QCheckBox(MainWindow)
        self.mButtonHiragana.setText("Hiragana")
        self.mButtonHiragana.move(100, 530)
        self.mButtonHiragana.setToolTip("Raccourci : H")
        self.mButtonHiragana.clicked.connect(MainWindow.Hiragana)

        self.mButtonPrononciation = QCheckBox(MainWindow)
        self.mButtonPrononciation.setText("Prononciation")
        self.mButtonPrononciation.move(200, 500)
        self.mButtonPrononciation.setToolTip("Raccourci : P")
        self.mButtonPrononciation.clicked.connect(MainWindow.Prononciation)

        self.mButtonTraduction = QCheckBox(MainWindow)
        self.mButtonTraduction.setText("Traduction")
        self.mButtonTraduction.move(200, 530)
        self.mButtonTraduction.setToolTip("Raccourci : T")
        self.mButtonTraduction.clicked.connect(MainWindow.Traduction)
        self.mButtonTraduction.setChecked(True)

        self.mButtonNombre = QCheckBox(MainWindow)
        self.mButtonNombre.setText("Nombre")
        self.mButtonNombre.move(320, 515)
        self.mButtonNombre.setToolTip("Raccourci : N")
        self.mButtonNombre.clicked.connect(MainWindow.Nombre)

        self.mButtonRandom = QPushButton(MainWindow)
        self.mButtonRandom.setText("Aléatoire")
        self.mButtonRandom.move(550, 515)
        self.mButtonRandom.setToolTip("Raccourci : A")
        self.mButtonRandom.clicked.connect(MainWindow.Aleatoire)



        self.searchInput = QLineEdit(MainWindow)
        self.searchInput.move(470, 60)
        self.searchInput.resize(330, 30)
        self.searchInput.setPlaceholderText("Rechercher...")
        self.searchInput.textChanged.connect(MainWindow.AfficheMotRecherche)
        self.searchInput.installEventFilter(MainWindow)

        self.mButtonRecherche = QPushButton(MainWindow)
        self.mButtonRecherche.setText("Rechercher")
        self.mButtonRecherche.move(800, 60)
        self.mButtonRecherche.clicked.connect(MainWindow.Recherche)

        self.mLabelRechercheMot = QListWidget(MainWindow)
        self.mLabelRechercheMot.move(470, 95)
        self.mLabelRechercheMot.setFixedWidth(330)
        self.mLabelRechercheMot.setMinimumHeight(100)
        # si on clique sur un item, on le met dans la barre de recherche
        self.mLabelRechercheMot.itemClicked.connect(MainWindow.itemClicked)
        self.mLabelRechercheMot.hide()
        


        font = QFont("Arial", 14)
        font.setBold(True)
        font.setUnderline(True)

        self.mLabelLongeur = QLabel(MainWindow)
        self.mLabelLongeur.move(175, 50)
        self.mLabelLongeur.setFont(QFont("Arial", 14))

        self.mLabelEcritKanji = QLabel(MainWindow)
        self.mLabelEcritKanji.setText("Kanji :")
        self.mLabelEcritKanji.move(40, 50)
        self.mLabelEcritKanji.setFont(font)
        self.mLabelEcritKanji.adjustSize()

        self.mLabelEcritHiragana = QLabel(MainWindow)
        self.mLabelEcritHiragana.setText("Hiragana :")
        self.mLabelEcritHiragana.move(550, 120)
        self.mLabelEcritHiragana.setFont(font)
        self.mLabelEcritHiragana.adjustSize()
        self.mLabelHiragana = QLabel(MainWindow)
        self.mLabelHiragana.move(600, 150)
        self.mLabelHiragana.setFont(QFont("Arial", 14))

        self.mLabelEcritPrononciation = QLabel(MainWindow)
        self.mLabelEcritPrononciation.setText("Prononciation :")
        self.mLabelEcritPrononciation.move(550, 210)
        self.mLabelEcritPrononciation.setFont(font)
        self.mLabelEcritPrononciation.adjustSize()
        self.mLabelPrononciation = QLabel(MainWindow)
        self.mLabelPrononciation.move(600, 240)
        self.mLabelPrononciation.setFont(QFont("Arial", 14))

        self.mLabelEcritTraduction = QLabel(MainWindow)
        self.mLabelEcritTraduction.setText("Traduction :")
        self.mLabelEcritTraduction.move(550, 300)
        self.mLabelEcritTraduction.setFont(font)
        self.mLabelEcritTraduction.adjustSize()
        self.mLabelTraduction = QLabel(MainWindow)
        self.mLabelTraduction.move(600, 330)
        self.mLabelTraduction.setFont(QFont("Arial", 14))

        self.mLabelEcritNombre = QLabel(MainWindow)
        self.mLabelEcritNombre.setText("Nombre :")
        self.mLabelEcritNombre.move(550, 390)
        self.mLabelEcritNombre.setFont(font)
        self.mLabelEcritNombre.adjustSize()
        self.mLabelNombre = QLabel(MainWindow)
        self.mLabelNombre.move(600, 420)
        self.mLabelNombre.setFont(QFont("Arial", 14))

        self.mLabelRaccourci = QLabel(MainWindow)
        self.mLabelRaccourci.setText("Raccourci (tout): W")
        self.mLabelRaccourci.move(400, 580)
        self.mLabelRaccourci.setFont(QFont("Arial", 10))
        self.mLabelRaccourci.adjustSize()
