# This file starts the server properly
#
# The backend should be hidden by a proxy like nginx which
# will handle the SSL

# Main app
python3 -m gunicorn.app.wsgiapp --reload --workers=1 --bind=127.0.0.1:2000 --chdir web app:app

# Reloader
python3 -m gunicorn.app.wsgiapp --daemon reload:app --bind=127.0.0.1:2001
