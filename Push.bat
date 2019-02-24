REM Newline added to make sure the server reloads content
echo # >> Backend/app.py
git add .
git commit -m "Automatic push cuz ya bois a lazy as heck"
git push
REM Curl is coming to Windows but BITS is a better bet for
REM compatibility
REM curl https://james.twelveoaksgroup.net/calgit/pull
bitsadmin /addfile GitPull https://james.twelveoaksgroup.net/calgit/pull result.txt
