
def count():

    result = {"PASS":0 ,"FAIL":0}



    f = open("log.txt", "r")

    for line in f:

        line = line.strip()

        if line == "PASS":
            result["PASS"]+=1
        elif line == "FAIL":
            result["FAIL"]+=1

    return result

print(count())