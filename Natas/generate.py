string = ""

with open("PHPSESSIDs.txt", "w") as filey:

    for i in range(1,641):

        string += (str(i) + "-admin").encode("hex") + "\n"

    filey.write(string)
