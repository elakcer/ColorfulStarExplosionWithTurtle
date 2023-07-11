import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()

turtle_colors = ["red","purple","green","blue","orange","yellow"]
while True:
       for i in range(15):
           turtle_instance.color(turtle_colors[i % 5])
           turtle_instance.forward(10 * i)
           turtle_instance.forward(-10 * i)
           turtle_instance.right(i)

