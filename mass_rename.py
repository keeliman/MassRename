import os
import re
import configparser

# Charger les configurations depuis le fichier .ini
config = configparser.ConfigParser()
config.read('config.ini')

try:
    DIRECTORY_PATH = config['DEFAULT']['DIRECTORY_PATH']
    LAST_PUBLISHED = int(config['DEFAULT']['LAST_PUBLISHED'])
except KeyError:
    print("Erreur : Une clé manquante dans le fichier de configuration.")
    exit()

def is_fully_numeric(filename):
    """Vérifie si le nom du fichier (sans extension) est entièrement numérique."""
    name, _ = os.path.splitext(filename)
    return name.isdigit()

def extract_numeric(filename):
    """Extrait le numéro du nom du fichier."""
    name, _ = os.path.splitext(filename)
    numbers = re.findall(r'\d+', name)
    if numbers:
        return int(numbers[0])
    return None

def rename_files_in_directory(directory, last_published):
    """Renomme en masse les fichiers dans le répertoire donné."""
    # Liste des fichiers dans le répertoire
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # Vérification que tous les fichiers sont numériques
    for filename in files:
        if not is_fully_numeric(filename):
            num = extract_numeric(filename)
            if num is not None:
                new_name = str(num) + os.path.splitext(filename)[1]
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            else:
                print(f"Erreur : Impossible de parser le numéro du fichier {filename}")
                return

    # Vérification que les vidéos sont bien numérotées à partir de 1
    numbers = sorted([int(os.path.splitext(f)[0]) for f in files])
    if numbers[0] != 1:
        print("Erreur : Les vidéos ne sont pas numérotées à partir de 1.")
        return

    # Renommer les fichiers en incrémentant par le dernier numéro publié
    for filename in files:
        num = int(os.path.splitext(filename)[0])
        new_name = str(num + last_published) + os.path.splitext(filename)[1]
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

    print("Renommage terminé avec succès!")


if __name__ == "__main__":
    if not os.path.exists(DIRECTORY_PATH):
        print(f"Erreur : Le répertoire {DIRECTORY_PATH} n'existe pas.")
        exit()

    try:
        rename_files_in_directory(DIRECTORY_PATH, LAST_PUBLISHED)
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
