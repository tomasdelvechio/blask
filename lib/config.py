from datetime import datetime

def version():
    ver = file('version.txt')
    return ver.read().strip()

def fecha():
    return datetime.today().strftime('%Y')

def author():
    return "Tomas Delvechio"

def license():
    return "GPLv3"
