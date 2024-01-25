To run our app for the first time, you have to read this .txt.
First, go in git bash in the file "Tykz" and write the following lines :
rm -rf migrations
rm -rf instance
flask db init
flask db migrate -m "a"
flask db upgrade
All those commands are useful to reset the database on your computer.
Next, you just have to write :
flask run
in the file "Tykz" in git bash. Then it runs our app, and you can open it in a browser such as chrome.
As you can notice, we put CI, especially Black and Flake8 tests, that are verified in the current code each time we push. We removed some conditions in flake8 that were incompatible with a flask app, and in both tests, the folders env.py and the folder in instance are not checked,
because they are created each time we create a new database (as you will do with the lines rm -rf and flask db), and we can't change them on computer of other people.
