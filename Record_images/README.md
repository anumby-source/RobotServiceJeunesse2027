##  Enregistrement des images pour l'apprentissage du modèle sur le K210

Ce répertoire contient les fichiers nécessaires pour faire la capture d'images avec le module M5Stack UnitV monté sur un robot et déclenchée à partir de la télécommande.

- Copier _boot.py_ et _record_images.py_ sur une carte micro-SD et insérer la carte SD dans le M5Stack UnitV
- Sur l'ESP32-S2 du robot, charger le script _record_images_robot.py_ et le lancer au démarrage ( "import record_images_robot" dans le fichier _boot.py_ du robot).

Sur l'ESP32-S2 de la télécommande, charger le script _record_images_telecommande.py_ et le lancer au démarrage ( "import record_images_telecomande" dans le fichier _boot.py_ de la télécommande)

> ⚠️ **Attention !** 
Ne pas oublier d'indiquer le numéro du couple robot/telecommande dans les deux scripts _record_images.py_ (au début du script)

Le robot est piloté normalement avec la télécommande. Le déclenchement de la capture de l'image se fait avec le clic supérieur de la télécommande.

L'image est enregistrée sur la carte SD, le nom du fichier est affiché sur l'écran de la télécommande.

L'image est capturée en niveau de gris (8 bits), sa résolution est 320x240.

Le format du nom de fichier est _img_xxxx.dat_ , où _xxxx_ est le numéro de l'image, incrémenté après chaque capture.

Si des fichiers image sont déjà présents sur la carte au moment du démarrage, le numéro est incrémenté à partir de celui la dernière image déja présente afin de ne pas effacer les images déjà présentes.
