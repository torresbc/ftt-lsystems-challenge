import math


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


def follow_rules(beginning, angle, actual_point, size):
    """
    Draw the stars
    :param beginning: Current compiled phrase
    """
    points = ""
    for letter in beginning:
        for i in range(5):
            if letter == "B":
                actual_point, angle, points = draw_square(actual_point, angle, points, size)
            if letter == "R":
                size += 5
            if letter == "U":
                actual_point += [actual_point[0] + (5 * math.cos(math.radians(angle))), actual_point[1] +
                                (5 * math.sin(math.radians(angle)))]
                angle -= 1
                points += f'{actual_point[0]}, {actual_point[1]} '

    return points


def draw_square(actual_point, angle, points, size):
    for i in range(4):
        actual_point = [actual_point[0] + (size * math.cos(math.radians(angle))), actual_point[1] +
                        (size * math.sin(math.radians(angle)))]
        angle -= 90
        points += f'{actual_point[0]}, {actual_point[1]} '
    angle -= 1
    return actual_point, angle, points


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


def export_svg(points):
    """
    Export the output_txt string into a SVG file
    :param points: Draw list of coordinates
    """
    size = 50000
    output_txt = f'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
      <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"
      "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
      <svg height="{size}" width="{size}" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve">
      <polyline points="'''

    output_txt += f'{points}"  style="fill:white;stroke:rgb(255,0,0);stroke-width:3" /></svg>'

    output = open("output.svg", "w")
    output.write(output_txt)
    output.close()


def main():
    rules, beginning = read_txt()
    angle = 300
    actual_point = [25000, 25000]
    size = 10
    points = ""

    for i in range(15):
        points += follow_rules(beginning, angle, actual_point, size) + ","
        beginning = replace_beginning(rules, beginning)

    export_svg(points)


if __name__ == '__main__':
    main()

