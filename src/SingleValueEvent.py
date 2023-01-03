class SingleValueEvent:
    def __init__(self):
        self.handlers = []

    def addListener(self, handler):
        if not callable(handler):
            return

        self.handlers.append(handler)

    def removeListener(self, handler):
        if self.handlers.__contains__(handler):
            self.handlers.remove(handler)

    def invoke(self, value):
        for handler in self.handlers:
            handler(value)
