# Shadow-Strike
ShadowStrike est une suite d'outils de pentest développée en Python, qui permet d'effectuer des audits de sécurité sur des cibles spécifiques, de lancer des exploits et de générer des rapports détaillés des résultats obtenus.
# Fonctionnalités
- Audit : Effectue une série de scans pour identifier les vulnérabilités potentielles sur la cible, y compris les scans Nmap, Nikto et Dirb.
- Exploit : Lance des exploits contre la cible pour tester les failles de sécurité identifiées lors de l'audit. Actuellement, les exploits supportés incluent Hydra (pour les attaques par force brute) et SQLMap (pour les injections SQL).
- Génération de rapports : Génère un rapport détaillé des résultats de l'audit et des exploits sous forme de fichier PDF.
# Installation
Clonez ce dépôt vers votre machine locale :
 - git clone https://github.com/Gheorghe-RESETNIC/Shadow-Strike
Accédez au répertoire du projet :
 - cd ShadowStrike
Assurez-vous d'avoir les dépendances requises installées. Vous pouvez les installer en exécutant :
 - pip install -r requirements.txt
# Utilisation
Exécutez le script principal main.py avec l'option -t pour spécifier la cible :
 - python3 main.py -t <adresse_IP_cible>
Suivez les instructions du menu pour effectuer des audits, lancer des exploits ou générer un rapport.
