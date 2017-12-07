 # app.py

from flask_cache import Cache
from flask import Flask

app = Flask()

# We'd normally include configuration settings in this call
cache = Cache(app)

@app.route('/')
@cache.cached(timeout=60)
def index():
    [...] # Make a few database calls to get the information we need
    return render_template(
        'index.html',
        latest_posts=latest_posts,
        recent_users=recent_users,
        recent_photos=recent_photos
    )
