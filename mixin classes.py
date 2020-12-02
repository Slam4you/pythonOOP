import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, arg):
        list.append(self, arg)
        Loggable.log(self, arg)

x = LoggableList([1, 2, 3, 5, -10])
print(x)
x.append(11)
print(x)

"""class LoggableList(list, Loggable):
    def append(self, item):
        super().append(item)
        self.log(item)"""
