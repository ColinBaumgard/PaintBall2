import model
from old import controller, view


class Main:
    def __init__(self):
        # initialisation model
        self.model = model.Model()

        # initialisation vue
        self.view = view.View()

        # intialisation controller
        self.controller = controller.Controller()

    def run(self):
        self.view.print(self.model)




if __name__ == '__main__':
    paintBall = Main()
    paintBall.run()