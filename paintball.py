import menu, mainwindow
import sys
from PyQt5.QtWidgets import QApplication

class PaintBall:
    def __init__(self):
        pass

    def menu(self):
        self.menu_ui = menu.Ui_Menu()
        self.menu_ui.show()
        self.menu_ui.jouer.clicked.connect(self.main)

    def main(self):
        print('main')
        self.main_ui = mainwindow.Main(self.menu_ui.level.value())
        self.menu_ui.close()
        self.main_ui.show()


if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    pb = PaintBall()
    pb.menu()

    sys.exit(app.exec())

