class StringVar:

    def __init__(self, some_string):
        self.some_string = some_string

    def set(self, new_string):
        self.some_string = new_string

    def get(self):
        return self.some_string


a = StringVar('First string')
print(a.some_string)
a.set('Second string')
print(a.some_string)
b = a.get()
print(b)
