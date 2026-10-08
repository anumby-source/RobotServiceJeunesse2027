## Reconnaissance des panneaux

Une fois le modèle entrainé sur Maixhub :

- retirer la carte SD du UnitV avant de le brancher sur un port USB et lancer _Kflash_gui_.

  Charger le modèle (fichier _model-322136.kmodel_) à l'adresse 0X300000.
- lancer Maixpy IDE, connecter le UnitV et charger le fichier _boot.py_ ci dessus.
- dans l'ESP32-S2 du robot, charger _robot.py_ et le lancer au démarrage ("import robot" dans _boot.py_)
- dans l'ESP32-S2 de la télécommande, charger _telecommande.py_ et le lancer au démarrage ("import telecommande" dans _boot.py_)


C'est fini !

Alummer le robot et la télécommande.

Le click bas de la télécommande permet de réduire la vitesse de déplacement du robot (appui maintenu).

Le click haut lance l'identification. Si le panneau est reconnu (probabilité > 0.7), son image s'affiche sur l'écran de la télécommande.
