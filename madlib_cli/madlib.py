import re
intro =  """
****************************************
**       Words, They mean things      **
** Unfortunately you have to use them **
**         This is a madlib           **
**     put the words in the holes     **
**      Wait, that sounds weird       ** 
**       You knew what I meant        **
**     We all know how madlibs work   **
**                                    **
****************************************
"""
# open and read the file
def read_template(file):
    try:
        with open(file) as d:
            return d.read()
    except FileNotFoundError as fnf_error:
        raise fnf_error

# parse the template txt file
def parse_template(string):
    pieces = tuple(re.findall(r"{([^{}]*)}", string))
    for x in pieces:
        string = string.replace(x, "")
    return string, pieces


def merge(stripped, inputs):
    return stripped.format(*inputs)


print(intro)
script = read_template("tests/test.txt")
empty_string, parts = parse_template(script)
filled_list = []
for i in parts:
    user_input = input(f" Enter {i} > ")
    filled_list.append(user_input)
result = merge(empty_string, filled_list)
print(result)
with open('output.txt', 'w') as writer:
    writer.write(result)

