

---

# Bulk File Renamer

Ce script permet de renommer en masse des fichiers dans un répertoire donné en se basant sur un numéro de départ spécifié dans un fichier de configuration.

## Prérequis

- Python installé sur votre machine. Si ce n'est pas le cas, vous pouvez le télécharger et l'installer depuis [le site officiel de Python](https://www.python.org/downloads/).

## Configuration

1. **Fichier de configuration** : Avant d'exécuter le script, assurez-vous d'avoir un fichier nommé `config.ini` dans le même répertoire que le script. Ce fichier doit contenir les informations suivantes :

   ```ini
   [DEFAULT]
   DIRECTORY_PATH = chemin_vers_votre_dossier
   LAST_PUBLISHED = dernier_numero_publié
   ```

   - `chemin_vers_votre_dossier` : Remplacez cette partie par le chemin complet du répertoire contenant les fichiers que vous souhaitez renommer. Par exemple : `C:/Users/utilisateur/Downloads/Dev All`.
   - `dernier_numero_publié` : Remplacez cette partie par le dernier numéro de fichier publié. Par exemple : `10`.

2. **Fichiers à renommer** : Assurez-vous que les fichiers que vous souhaitez renommer sont numérotés à partir de `1` (par exemple : `1.mp4`, `2.mp4`, etc.).

## Utilisation

1. Ouvrez une invite de commande ou un terminal.
2. Naviguez vers le répertoire contenant le script et le fichier `config.ini` en utilisant la commande `cd`. Par exemple :

   ```bash
   cd C:/chemin/vers/le/script
   ```

3. Exécutez le script en utilisant la commande suivante :

   ```bash
   python nom_du_script.py
   ```

   Remplacez `nom_du_script.py` par le nom réel de votre script si nécessaire.

4. Si tout se passe bien, vous devriez voir un message indiquant que le renommage a été effectué avec succès. Sinon, des messages d'erreur vous aideront à identifier le problème.

## Problèmes courants

- **Erreur de clé manquante** : Assurez-vous que votre fichier `config.ini` contient bien les clés `DIRECTORY_PATH` et `LAST_PUBLISHED`.
- **Erreur de répertoire inexistant** : Vérifiez que le chemin spécifié dans `DIRECTORY_PATH` est correct et que le répertoire existe bien.
- **Erreur de numéro de fichier** : Assurez-vous que les fichiers sont bien numérotés à partir de `1`.

---

Vous pouvez copier-coller ce README dans votre dépôt GitHub. Assurez-vous de remplacer `nom_du_script.py` par le nom réel de votre script si nécessaire.
