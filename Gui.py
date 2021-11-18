from graphics import *



def main():

    length = 500
    width = 500
    win = GraphWin("My Circle", width, length)

    board_width = 10
    board_length = 10

    delta_width = width / board_width
    delta_length = length / board_length
    x, y = 0, 0
    p1 = Point(x,y)
    p2 = Point(x + delta_width, y + delta_length)

    for i in range(board_length):
        for j in range(board_width):
            r = Rectangle(p1,p2)
            r.draw(win)
            x = x + delta_width
            p1 = Point(x,y)
            p2 = Point(x + delta_width, y + delta_length)
        x = 0
        y += delta_length
        p1 = Point(x,y)
        p2 = Point(x + delta_width, y + delta_length)


    win.getMouse() # pause for click in window

    win.close()



main()