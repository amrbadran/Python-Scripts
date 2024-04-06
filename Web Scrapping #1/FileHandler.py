class FileHandler:
    def __init__(self, path, news=None):
        self.path = path
        self.news = news

    def write(self):
        with open(self.path, 'w') as file:
            for i, new in enumerate(self.news):
                file.write(str(i) + " :" + new + "\n")

    def read(self):
        with open(self.path, 'r') as file:
            print(file.read())
