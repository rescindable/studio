# This server reloads the main server when a url "/pull"
# has been accessed, ensuring that the latest content is 
# served

python3 -m gunicorn.app.wsgiapp --workers=1 reload:app --bind=localhost:2001
