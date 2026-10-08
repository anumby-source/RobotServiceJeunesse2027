##  Enregistrement des images pour l'apprentissage du modèle sur le K210

Ce répertoire contient les fichiers nécessaires pour faire la capture d'images avec le module M5Stack UnitV monté sur un robot.

La capture est déclenchée à partir de la télécommande.

- Copier _boot.py_ et _record_images_RGB565.py_ sur une carte micro-SD et insérer la carte dans le M5Stack UnitV
- Sur l'ESP32-S2 du robot, charger le script _record_images_robot.py_ et le lancer au démarrage ( "import record_images_robot" dans le fichier _boot.py_ du robot)
- Sur l'ESP32-S2 de la télécommande, charger le script _record_images_telecommande.py_ et le lancer au démarrage ( "import record_images_telecomande" dans le fichier _boot.py_ de la télécommande)

> ⚠️ **Attention !** 
Ne pas oublier d'indiquer le numéro du couple robot/telecommande dans les deux scripts précédents (au début du script)

Utilisation de la télécommande :

- le robot est piloté normalement avec le joystick. La vitesse est réduite pour pouvoir le positionner plus précisément,
- le bouton inférieur (à côté de la prise USB) permet de sélectionner le numéro du panneau ("Class" de 1 à 10),
- la capture d'image se fait avec le bouton supérieur de la télécommande.

Les images sont enregistrées sur la carte SD, en couleur (résolution 224x224), au format jpg, dans le répertoire "images":

📦 sd/

    ├📁 images/
 
       ├📁 1/              (panneau 1)
    
            ├1.jpg
         
            ├2.jpg
         
            ...
         
       ├📁 2/              (panneau 2)
    
            ├1.jpg
         
            ├2.jpg
         
            ...
         
       ...
 

L'écran de la télécommande affiche le numéro du panneau ("Class p") et le nom du fichier de la dernière image enregistrée ("/sd/image/p/n")
