import turtle


def draw_pifagor_tree(branch_length, t, angle, level):
    if level == 0:
        return
    else:
        t.forward(branch_length)
        t.right(angle)
        draw_pifagor_tree(0.7 * branch_length, t, angle, level - 1)
        t.left(2 * angle)
        draw_pifagor_tree(0.7 * branch_length, t, angle, level - 1)
        t.right(angle)
        t.backward(branch_length)


if __name__ == "__main__":
    level = int(input("Enter the recursion level: ")) or 5

    screen = turtle.Screen()
    screen.bgcolor("grey")

    t = turtle.Turtle()
    t.speed(5)
    t.color("black")
    t.width(2)
    t.left(90)
    draw_pifagor_tree(100, t, 30, level)

    screen.exitonclick()
