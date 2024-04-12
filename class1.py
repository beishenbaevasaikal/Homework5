class Hello:
    def __init__(self, str):
        self.str = str
class Hello2 (Hello):
    def __init__(self, str):
        super().__init__(str)

    def tptint(self):
        print('Hello everyone!')

