# This server reloads the main server when a url "/pull"
# has been accessed, ensuring that the latest content is 
# served

python3 -m gunicorn.app.wsgiapp --daemon reload:app --bind=127.0.0.1:2001
