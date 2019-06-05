import menu_v2 as menu
import jeu
import map_editor_v2 as map_editor

import sys
from PyQt5.QtWidgets import QApplication

class PaintBall:
    def __init__(self):
        pass

    def menu(self):
        self.menu_ui = menu.Ui_Menu()
        self.menu_ui.show()
        self.menu_ui.jouer.clicked.connect(self.main)
        self.menu_ui.creer_map.clicked.connect(self.map_editor)

    def main(self):
        print('main')
        if self.menu_ui.radioBtnMap.isChecked():
            self.main_ui = jeu.PathPB(self.menu_ui.liste_maps[self.menu_ui.i_map])
        else:
            self.main_ui = jeu.RandomPB(self.menu_ui.level.value())
            
        #self.menu_ui.close()
        self.main_ui.show()
        #self.menu()

    def map_editor(self):
        self.map_editor_ui = map_editor.Editor()
        #self.menu_ui.close()
        self.map_editor_ui.show()

if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    pb = PaintBall()
    pb.menu()

    sys.exit(app.exec())

