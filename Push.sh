# Newline added to make sure the server reloads content
echo "#" >> Backend/app.py
git add .
git commit -m "Automatic push cuz ya bois a lazy as heck"
git push
curl https://james.twelveoaksgroup.net/calgit/pull
