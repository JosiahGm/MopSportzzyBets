# myapp/views.py

from . import app

@app.route('/r/<list:subreddits>')
def subreddit_home(subreddits):
    """Show all of the posts for the given subreddits."""
    posts = []
    for subreddit in subreddits:
        posts.extend(subreddit.posts)

    return render_template('/r/index.html', posts=posts)

profile = Blueprint('profile', __name__,
                    template_folder='templates',
                    static_folder='static')
