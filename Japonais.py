import csv
import sys
import os
from random import randint
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from ui_form import Ui_MainWindow


class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.image_list = []
        self.current_image = 0
        self.fichier = []
        self.hiragana = []
        self.prononciation = []
        self.traduction = []
        self.traits = []
        
        self.image_list_used = []
        self.fichier_used = []
        self.hiragana_used = []
        self.prononciation_used = []
        self.traduction_used = []
        self.traits_used = []

        self.visible = False
        self.random_button_clicked = False

        self.Images()
        self.previous_image = None
        self.image_actuel = self.RandomImage()
        self.FichierCSV()
        self.Traduction()
    

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        if self.visible:
            # définit la zone cible et la zone source de l'image
            target = QRect(50, 80, 400, 400)
            source = QRect(0, 0, self.image_actuel.width(), self.image_actuel.height())
                
            # dessine l'image courante dans la fenêtre
            qp.drawImage(target, self.image_actuel, source)
            
        qp.end()


    def Images(self):
        self.path = str("Images")
        val = os.listdir(self.path)
        if(self.path != ""):
            for file in val:
                if(file.endswith(".jpg")):
                    self.image_list.append(file)
        # Tri de la liste
        self.image_list = sorted(self.image_list)
    

    def RandomImage(self):
        if not self.random_button_clicked:
            # Nombre de Kanji déja fait
            self.ui.mLabelLongeur.setText(str(len(self.image_list_used)+1) + "/" + str(len(self.image_list_used)+len(self.image_list)))
            
            # Sélectionnez une image au hasard dans la liste
            self.img = randint(0, len(self.image_list) - 1)
            random_image = self.image_list[self.img]

            #print(self.image_list_used)
            #print(self.image_list)

            image_path = self.path + "\\" + random_image
            random_image = QImage(image_path)

            self.current_image = self.img
            return random_image

        else:
            # Stocker l'image précédente
            self.previous_image = self.image_list[self.current_image]

            # Ajouter l'image précédente à la nouvelle liste
            self.image_list_used.append(self.previous_image)
            #print(self.image_list_used)

            # Enlever l'image de la liste principale
            self.image_list.remove(self.previous_image)
            #print(self.image_list)

            if self.image_list == []:
                QMessageBox.information(self, "Aucun élément trouvé", "Vous êtes arrivé à la fin de la séries. Commencer une nouvelle série ?", QMessageBox.Yes)
                self.image_list = self.image_list_used
                self.image_list_used = []
                self.random_button_clicked = False
                self.RandomImage()
            else:
                # Nombre de Kanji déja fait
                self.ui.mLabelLongeur.setText(str(len(self.image_list_used)+1) + "/" + str(len(self.image_list_used)+len(self.image_list)))
            
            # Sélectionnez une image au hasard dans la liste
            self.img = randint(0, len(self.image_list) - 1)
            random_image = self.image_list[self.img]

            image_path = self.path + "\\" + random_image
            random_image = QImage(image_path)

            self.current_image = self.img

            return random_image
    

    def FichierCSV(self):
        # Ouvre le fichier CSV en lecture
        with open("Kanji_Hiragana_Traduction.csv", "r", encoding="utf-8") as f:
            # Création d'un lecteur CSV
            reader = csv.reader(f)
            
            # Parcours des lignes du fichier
            for row in reader:
                # On ajoute les données dans les listes
                self.fichier.append(row[0])
                self.hiragana.append(row[1])
                self.prononciation.append(row[2])
                self.traduction.append(row[3])
                self.traits.append(row[4])

    
    def Kanji(self):
        self.ui.mLabelRechercheMot.hide()
        if(self.ui.mButtonKanji.isChecked()):
            self.visible = True
            self.update()
        else:
            self.visible = False
            self.update()
        
        if self.ui.mButtonRecherche.isChecked():
            self.Recherche()
    

    def Hiragana(self):
        self.ui.mLabelRechercheMot.hide()
        if(self.ui.mButtonHiragana.isChecked()):
            if(self.image_list[self.current_image] in self.fichier):
                self.ui.mLabelHiragana.setText(self.hiragana[self.fichier.index(self.image_list[self.current_image])])
                self.ui.mLabelHiragana.setFont(QFont("Arial", 14))
                self.ui.mLabelHiragana.adjustSize()
        else:
            self.ui.mLabelHiragana.setText("")
        
        if self.ui.mButtonRecherche.isChecked():
            self.Recherche()
    

    def Prononciation(self):
        self.ui.mLabelRechercheMot.hide()
        if(self.ui.mButtonPrononciation.isChecked()):
            if(self.image_list[self.current_image] in self.fichier):
                self.ui.mLabelPrononciation.setText(self.prononciation[self.fichier.index(self.image_list[self.current_image])])
                self.ui.mLabelPrononciation.setFont(QFont("Arial", 14))
                self.ui.mLabelPrononciation.adjustSize()
        else:
            self.ui.mLabelPrononciation.setText("")
        
        if self.ui.mButtonRecherche.isChecked():
            self.Recherche()


    def Traduction(self):
        self.ui.mLabelRechercheMot.hide()
        if(self.ui.mButtonTraduction.isChecked()):
            if(self.image_list[self.current_image] in self.fichier):
                self.ui.mLabelTraduction.setText(self.traduction[self.fichier.index(self.image_list[self.current_image])])
                self.ui.mLabelTraduction.setFont(QFont("Arial", 14))
                self.ui.mLabelTraduction.adjustSize()
        else:
            self.ui.mLabelTraduction.setText("")
        
        if self.ui.mButtonRecherche.isChecked():
            self.Recherche()
    

    def Nombre(self):
        self.ui.mLabelRechercheMot.hide()
        if(self.ui.mButtonNombre.isChecked()):
            if(self.image_list[self.current_image] in self.fichier):
                self.ui.mLabelNombre.setText(self.traits[self.fichier.index(self.image_list[self.current_image])])
                self.ui.mLabelNombre.setFont(QFont("Arial", 14))
                self.ui.mLabelNombre.adjustSize()
        else:
            self.ui.mLabelNombre.setText("")
        
        if self.ui.mButtonRecherche.isChecked():
            self.Recherche()
    

    def Aleatoire(self):
        self.random_button_clicked = True

        self.ui.searchInput.clear()

        # On met à jour self.image_actuel avec une nouvelle image aléatoire
        self.image_actuel = self.RandomImage()
        
        # On met à jour les labels
        self.Kanji()
        self.Hiragana()
        self.Prononciation()
        self.Traduction()
        self.Nombre()
        
        # On rafraîchit la fenêtre pour afficher l'image
        self.update()


    def Recherche(self):
        # Stocker l'image précédente
        self.previous_image = self.image_list[self.current_image]

        # Ajouter l'image précédente à la nouvelle liste
        self.image_list_used.append(self.previous_image)
        #print(self.image_list_used)

        # Enlever l'image de la liste principale
        self.image_list.remove(self.previous_image)
        #print(self.image_list)

        # On récupère la valeur de l'entrée
        self.motRecherche = self.ui.searchInput.text()
        self.ui.mLabelRechercheMot.hide()

        if self.motRecherche != "":
            found = False

            if self.motRecherche in self.hiragana:
                self.Check(self.hiragana.index(self.motRecherche))

                found = True
                self.update()

            if self.motRecherche in self.prononciation:
                self.Check(self.prononciation.index(self.motRecherche))

                found = True
                self.update()

            if self.motRecherche in self.traduction:
                self.Check(self.traduction.index(self.motRecherche))

                found = True
                self.update()
            
            if self.motRecherche in self.traits:
                self.Check(self.traits.index(self.motRecherche))

                found = True
                self.update()

            if(not found):
                self.ShowNotFoundMessage()
    

    def Check(self, i):
        self.image_actuel = QImage(self.path + "\\" + self.fichier[i])
        self.current_image = i
        self.Kanji()
                    
        if self.ui.mButtonHiragana.isChecked():
            self.ui.mLabelHiragana.setText(self.hiragana[i])
            self.ui.mLabelHiragana.setFont(QFont("Arial", 14))
            self.ui.mLabelHiragana.adjustSize()
        else:
            self.ui.mLabelHiragana.setText("")

        if self.ui.mButtonPrononciation.isChecked():
            self.ui.mLabelPrononciation.setText(self.prononciation[i])
            self.ui.mLabelPrononciation.setFont(QFont("Arial", 14))
            self.ui.mLabelPrononciation.adjustSize()
        else:
            self.ui.mLabelPrononciation.setText("")
                    
        if self.ui.mButtonTraduction.isChecked():
            self.ui.mLabelTraduction.setText(self.traduction[i])
            self.ui.mLabelTraduction.setFont(QFont("Arial", 14))
            self.ui.mLabelTraduction.adjustSize()
        else:
            self.ui.mLabelTraduction.setText("")
                    
        if self.ui.mButtonNombre.isChecked():
            self.ui.mLabelNombre.setText(self.traits[i])
            self.ui.mLabelNombre.setFont(QFont("Arial", 14))
            self.ui.mLabelNombre.adjustSize()
        else:
            self.ui.mLabelNombre.setText("")
    

    def AfficheMotRecherche(self):
        query = self.ui.searchInput.text()
        found_items = []
        self.ui.mLabelRechercheMot.clear()

        if query :
            self.ui.mLabelRechercheMot.show()
            self.ui.mLabelRechercheMot.raise_()
            for item in self.hiragana:
                if query in item:
                    found_items.append(item)

            for item in self.prononciation:
                if query in item:
                    found_items.append(item)

            for item in self.traduction:
                if query in item:
                    found_items.append(item)
            
            for item in self.traits:
                if query in item:
                    found_items.append(item)

            self.ui.mLabelRechercheMot.addItems(found_items)
            if len(found_items) == 0:
                self.ui.mLabelRechercheMot.addItem("Aucun élément trouvé")
        else:
            self.ui.mLabelRechercheMot.hide()
    

    def itemClicked(self, item):
        self.ui.searchInput.setText(item.text())
        self.ui.mLabelRechercheMot.hide()
        self.Recherche()
    

    def eventFilter(self, source, event):
        if self.ui.searchInput.text() != "":
            # On vérifie si l'événement est un bouton de la souris
            if event.type() == QEvent.MouseButtonPress:
                # On verifie si le bouton est le bouton gauche
                if event.button() == Qt.LeftButton:
                    # On verifie si la source de l'evenement est la barre de recherche
                    if source is self.ui.searchInput:
                        self.AfficheMotRecherche()
        return super().eventFilter(source, event)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.ui.mLabelRechercheMot.hide()
            self.ui.searchInput.clearFocus()
            self.ui.mButtonKanji.clearFocus()
            self.ui.mButtonHiragana.clearFocus()
            self.ui.mButtonPrononciation.clearFocus()
            self.ui.mButtonTraduction.clearFocus()
            self.ui.mButtonNombre.clearFocus()
            self.ui.mButtonRecherche.clearFocus()
            self.ui.mButtonRandom.clearFocus()
    

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_K:
            self.ui.mButtonKanji.click()
        elif event.key() == Qt.Key_H:
            self.ui.mButtonHiragana.click()
        elif event.key() == Qt.Key_P:
            self.ui.mButtonPrononciation.click()
        elif event.key() == Qt.Key_T:
            self.ui.mButtonTraduction.click()
        elif event.key() == Qt.Key_N:
            self.ui.mButtonNombre.click()
        elif event.key() == Qt.Key_A:
            self.Aleatoire()
        
        elif event.key() == Qt.Key_W:
            self.ui.mButtonKanji.click()
            self.ui.mButtonHiragana.click()
            self.ui.mButtonPrononciation.click()
            self.ui.mButtonTraduction.click()
            self.ui.mButtonNombre.click()
    

    def ShowNotFoundMessage(self):
        QMessageBox.information(self, "Aucun élément trouvé", "Aucun élément ne correspond à la chaîne de recherche '" + self.motRecherche + "'.", QMessageBox.Ok)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    app.exec_()
