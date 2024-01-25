Pour lancer notre application pour la première fois, vous devez lire ce .txt.

1.Python

Assurez-vous que Python est installé. Sinon, allez sur https://www.python.org/downloads/. Lors du développement de l'application, nous avons utilisé la version 3.11.4

1.2 Commande pip

Assurez-vous également que vous pouvez utiliser la commande "pip". C'est généralement le cas des versions récentes de Python. Cependant, si ce n’est pas le cas, assurez-vous-en en installant la version de Python utilisée lors du développement.

2. Environnement virtuel

Pour mettre en place un environnement virtuel, dans le répertoire 'Tykz', exécutez les commandes :
source venv/Scripts/activate # WINDOWS
source venv/bin/activate # MAC
Vous pouvez le désactiver dans le répertoire associé avec :
deactivate

3. Dépendances

Dans le répertoire 'Tykz' contenant 'requirements.txt', exécutez la commande suivante :
pip install -r requirements.txt

4. Configuration de la base de données

Si votre répertoire 'Tykz' ne contient pas les fichiers 'migrations' et 'instance', ou si vous les avez intentionnellement supprimés pour réinitialiser la base de données, soit manuellement, soit dans le répertoire 'Tykz' en utilisant les commandes :
rm -rf migrations
rm -rf instance
Ensuite vous devez exécuter les commandes suivantes :
flask db init
flask db migrate -m "initial migration"
flask db upgrade

5. Lancement de l'application

Ensuite, dans le répertoire 'Tykz', vous devez exécuter la commande suivante :
flask run
Cela exécute l'application et vous pouvez l'ouvrir dans un navigateur tel que Chrome, avec l'URL indiquée à l'écran.

# Remarques

Comme vous pouvez le constater, nous mettons des tests CI, notamment Black et Flake8, qui sont vérifiés dans le code actuel à chaque poussée. Nous avons supprimé certaines conditions dans flake8 qui étaient incompatibles avec une application flask, et dans les deux tests, les dossiers env.py et le dossier instance ne sont pas vérifiés, car ils sont créés à chaque fois que nous créons une nouvelle base de données, et nous ne pouvons pas les modifier sur l'ordinateur d'autres personnes.