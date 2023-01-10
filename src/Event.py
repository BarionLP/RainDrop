class Event:
    def __init__(self):
        self.handlers = []

    def addListener(self, handler):
        if not callable(handler):
            raise TypeError()

        self.handlers.append(handler)

    def removeListener(self, handler):
        if self.handlers.__contains__(handler):
            self.handlers.remove(handler)

    def invoke(self):
        for handler in self.handlers:
            handler()
