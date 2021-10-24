class Point(object):
    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set_coord(self, x, y):
        self._x = x
        self._y = y
