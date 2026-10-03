class Game:
    def __init__(self):
        self.score = 0

    def get_command(self):
        return input("> ")

    def process_command(self, command):
        if command == "":
            self.score += 1
            print(f"Puan: {self.score}")

    def run(self):
        while True:
            command = self.get_command()
            self.process_command(command)


game = Game()
game.run()
