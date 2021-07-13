import pyperclip, shelve, sys

multiClipboardShelf = shelve.open('multiClipboard')
if len(sys.argv) == 3:
    if sys.argv[1] == 'save':
        multiClipboardShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1] == 'load':
        pyperclip.copy(multiClipboardShelf[sys.argv[2]])
    elif sys.argv[1] == 'del':
        del multiClipboardShelf[sys.argv[2]]
elif len(sys.argv) == 2 and sys.argv[1] == 'list':
    for k in multiClipboardShelf.keys():
        print(k)

multiClipboardShelf.close()