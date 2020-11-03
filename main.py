"""
alphabet: B, R, U
beginning: BRU
rules: (B -> RU), (R -> BU), (U -> R)
        - B -> Draw the biggest star
        - R -> Draw the smallest star
        - U -> Move forward 5
"""
import turtle


def read_txt():
    """
    Reads the txt file at the project root
    :return: The initial sentence to be compiled and the rules of grammar
    """
    rules = []
    with open("grammar.txt", 'r') as txt:
        for index, line in enumerate(txt):
            if index > 0:
                rules.append(line.rstrip())
            else:
                beginning = line

    return rules, beginning


def draw_star(beginning):
    """
    Draw the stars
    :param beginning: Current compiled phrase
    """
    for letter in beginning:
        for i in range(5):
            if letter == "B":
                turtle.forward(120)
                turtle.left(216)
                turtle.end_fill()
            if letter == "R":
                turtle.forward(60)
                turtle.left(216)
                turtle.end_fill()
            if letter == "U":
                turtle.forward(5)


def replace_beginning(rules, beginning):
    """
    Compiles the current phrase according to grammar
    :param rules: Grammar rules stipulated in the txt
    :param beginning: Current compiled phrase
    :return: New phrase to compile
    """
    aux_beginning = []

    for letter in list(beginning):
        for rule in rules:
            rule = rule.split(">")
            if letter == rule[0]:
                aux_beginning.append(rule[1].split(">"))

    final_beginning = "".join(str(x) for x in aux_beginning)
    final_beginning = final_beginning.replace("[", "").replace("]", "").replace("'", "")
    return final_beginning


def main():
    rules, beginning = read_txt()

    for i in range(5):
        draw_star(beginning)
        beginning = replace_beginning(rules, beginning)

    turtle.done()


if __name__ == '__main__':
    star = turtle.Turtle()
    star.getscreen().bgcolor("gray")
    star.speed(10)
    main()


