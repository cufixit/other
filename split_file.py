LINES_PER_FILE = 300

file = None
fileno = 0
with open("311_data.json") as big_file:
    for lineno, line in enumerate(big_file):
        if lineno % LINES_PER_FILE == 0:
            if file:
                file.close()
            filename = "311_data/part_{}.txt".format(fileno)
            fileno += 1
            file = open(filename, "w")
        file.write(line)
    if file:
        file.close()
