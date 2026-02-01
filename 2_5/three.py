s = "python is easy and python is powerful"

def retfreq(s):
    freq ={

    }
    s_l = s.lower()

    a = s_l.split(" ")

    for word in a:
        if freq.get(word) is None:
            freq[word] = 1
        else:
            freq[word] += 1
            


    return freq

print(retfreq(s))
