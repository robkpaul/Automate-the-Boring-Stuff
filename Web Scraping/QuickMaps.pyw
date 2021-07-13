import webbrowser,sys,pyperclip
mapURL = "https://www.google.com/maps/place/"
if(len(sys.argv) > 1):
    for seg in sys.argv[1:]:
        mapURL += '+' + seg
    webbrowser.open(mapURL)
