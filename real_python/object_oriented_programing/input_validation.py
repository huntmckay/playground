class Rectangle:
    def __init__(self, width, heigh):
        if not (isinstance(width, (int, float)) and width > 0):
            raise ValueError(f"positive width expected, got {width}")
        self.width = width
        if not (isinstance(height, (int, float)) and height> 0):
            raise ValueError(f"positive width expected, got {height}")
