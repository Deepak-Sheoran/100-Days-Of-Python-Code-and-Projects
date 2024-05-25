from turtle import Turtle, Screen  # Turtle is a class already created within the 'turtle' module

tonny = Turtle()
tonny.shape("square")
tonny.color("blue", "yellow")
tonny.forward(100)
window = Screen()
print(window.canvheight)  # Here 'canvheight' is an attribute associated with the object
window.exitonclick()  # The exitonclick is a method associated with the object. Its functionality is to stop the window
# from disappearing unless we click on it.
