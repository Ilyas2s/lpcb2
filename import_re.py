import re

def lire_fichier(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def afficher(message):
    print(message)

def interpreter_lpcb(code):
    lignes = code.split('\n')
    for ligne in lignes:
        if ligne.startswith('afficher'):
            message = re.findall(r'\"(.+?)\"', ligne)
            if message:
                afficher(message[0])

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python import_re.py <fichier.lpcb>")
        sys.exit(1)

    fichier_lpcb = sys.argv[1]
    code = lire_fichier(fichier_lpcb)
    interpreter_lpcb(code)