from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/stories')
def stories():
    stories = [
    {
        "id": 1,
        "title": "The Night the Stars Spoke in Lut Desert",
        "excerpt": "I turned off my headlamp. For the first time in my life, I saw the entire Milky Way with my naked eyes. The silence was so deep I could hear my own heartbeat...",
        "author": "Léa from France",
        "date": "November 2025",
        "image": "/static/images/stories/lut-stars.jpg"
    },
    {
        "id": 2,
        "title": "Tea with Haj Mirza – The 92-Year-Old Poet of Yazd",
        "excerpt": "He still brews tea the old way every morning and tells stories of caravans that passed through the Silk Road. I sat there for 4 hours and forgot about time...",
        "author": "Alex from Australia",
        "date": "October 2025",
        "image": "/static/images/stories/haj-mirza.jpg"
    },
    {
        "id": 3,
        "title": "I Accidentally Crashed a Persian Wedding in Shiraz",
        "excerpt": "They saw me taking photos outside, grabbed my hand and pulled me in. 3 hours later I was dancing with the bride’s grandfather. Best night of my life.",
        "author": "Sofia from Spain",
        "date": "September 2025",
        "image": "/static/images/stories/wedding.jpg"
    },
    {
        "id": 4,
        "title": "Sleeping in a 400-Year-Old Caravanserai",
        "excerpt": "No electricity, no Wi-Fi, just candles and the sound of wind in the courtyard. I woke up at 4 AM and felt like I traveled back in time.",
        "author": "Daniel from Germany",
        "date": "November 2025",
        "image": "/static/images/stories/caravanserai.jpg"
    },
    {
        "id": 5,
        "title": "Dinner with a Family in Kashan",
        "excerpt": "They invited me for tea. 5 hours and 7 dishes later, I was part of the family. The mother packed me food for 3 days when I left.",
        "author": "Aisha from Malaysia",
        "date": "October 2025",
        "image": "/static/images/stories/family-dinner.jpg"
    }
]
    return render_template('stories.html', stories=stories)