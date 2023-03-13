class Board:
    fields = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
    def getNeighbours(self, x, y):
        ret_val=list()
        for x_offset, y_offset in ([-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]):
            new_x, new_y = x + x_offset, y + y_offset
            if 0<=new_x<=3 and 0<=new_y<=3:
                ret_val.append([new_x, new_y])
        return ret_val


class Board2:
    fields = [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
    def getNeighbours(self, x, y):
        for x_offset, y_offset in ([-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]):
            new_x, new_y = x + x_offset, y + y_offset
            if 0<=new_x<=3 and 0<=new_y<=3:
                yield([new_x, new_y])

b = Board()
for n in b.getNeighbours(2,3):
    print("neighbour = ", end=" ")
    print(n)

b2 =Board2()
print("neighbour = ",b.getNeighbours(2,3))