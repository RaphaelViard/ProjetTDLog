To run our app for the first time, you have to read this .txt.
First, go in git bash in the file "Tykz"
Check if you have the folders migrations and instance in Tykz. if no, write the following commands in the terminal :
flask db init
flask db migrate -m "a"
flask db upgrade
All those commands are useful to reset the database on your computer. The two first lines "rm -rf" are only useful if the corresponding folders are in the folder when you clone it. If not, just do the 3 last lines.
Next, you just have to write :
flask run
in the file "Tykz" in git bash. Then it runs our app, and you can open it in a browser such as chrome.
If you had the folders migrations and instance in Tykz and it doesn't work, write the following commands :
rm -rf migrations
rm -rf instance
flask db init
flask db migrate -m "a"
flask db upgrade
in the Tykz folder. Then, you can flask run and it will works.
As you can notice, we put CI, especially Black and Flake8 tests, that are verified in the current code each time we push.
