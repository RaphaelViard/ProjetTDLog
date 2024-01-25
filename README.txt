To run our app for the first time, you have to read this .txt.
First, go in git bash in the file "Tykz"
then put in your terminal the following commands :
rm -rf migrations
rm -rf instances
flask db init
flask db migrate -m "a"
flask db upgrade

All those commands are useful to reset the database on your computer. The two first lines "rm -rf" are only useful if the corresponding folders are in the folder when you clone it. If not, just do the 3 last lines.
Next, you just have to write :
flask run
in the file "Tykz" in git bash. Then it runs our app, and you can open it in a browser such as chrome.

As you can notice, we put CI, especially Black and Flake8 tests, that are verified in the current code each time we push.
