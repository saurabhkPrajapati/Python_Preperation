import textwrap


def wrap(string, max_width):
    wrapped_lines = textwrap.wrap(string, width=max_width)
    for line in wrapped_lines:
        print(line)


if __name__ == '__main__':
    wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4)

# ____________________________________________________________________________________


text = "Python is an amazing programming language that is simple yet powerful. It is widely used in various fields such as web development, data science, automation, and more."
wrapped_text = textwrap.fill(text, width=50)
print(wrapped_text)


# ____________________________________________________________________________________

def wrap(string, max_width):
    for i in range(0, len(string), max_width):
        print(string[i:i + max_width])


wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4)


# _____________________________________________________________________________________

def wrap(string, max_width):
    lst = ""
    for i in range(0, len(string), 4):
        lst = lst + string[i:i + 4] + "\n"
    return lst


result = wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4)
print(result)
