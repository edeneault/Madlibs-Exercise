from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

from stories import story, story_2, story_3
app = Flask(__name__)

STORIES = {"story": story, "story_2": story_2, "story_3": story_3}

app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    """Return homepage."""
    return render_template("form.html")

@app.route('/form')
def form():
    """Return Selected Form."""
    stories = request.args.get("story")
    return render_template("form.html", story=stories)

@app.route('/answer/<stories>')
def answer(stories):
    """Return Answer to Selected Story """
    print(stories)
    story = STORIES[stories]
    text = story.generate(request.args)

    return render_template("answer.html", text=text)
