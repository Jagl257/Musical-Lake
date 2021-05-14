soundmap = {
    'brr':"fiu",
    'birip':"trri-trri",
    'brrah':"null",
    'croac':"null",
    'fiu': "cric-cric",
    'plop': "cric-cric",
    'pep': "birip",
    'cric-cric':"brrah",
    'trri-trri':"croac",
    'bri-bri': "plop",
}

def singsong(sound):
    if soundmap.get(sound,"null") == "null":
        return "\n"
    else:
        nextSound = soundmap.get(sound,"croac")
        return (nextSound + ", " + singsong(nextSound))
