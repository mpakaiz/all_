class Square():
    squares = []
    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.squares.append((self.width, self.len))
    def square_list (self):
        print ("""{} on {}""".format(self.width, self.len))

s1 = Square (10,10)
s2 = Square (20,20)
s3 = Square (30,30)

print(Square.squares)
    
    
