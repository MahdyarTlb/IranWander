iranWander project for Cs50

put html files in: \IranWander\templates
put static files(css, js and pictures) in: \IranWander\static

this is the project structure:

    IranWander/
    ├──
        IranWander/
        ├── __init__.py         # main file    
        ├── config.py           # settings
        ├── models.py           # database models
        ├── migrations/         database migrations
        │   └── env.py          → target_metadata = db.metadata
        ├── templates/          # html files
        │   ├── index.html
        │   ├── login.html
        │   └── ...
        ├── static/             # css, js and pictures
        │   ├── css/style.css
        │   ├── js/main.js

    ├── run.py              # for fast running
    ├── requirements.txt    # needed packages
    ├── iranWander.db     # database
    └── README.md           # details

for first edit       -->    1. make a venv and activate it on folder 'IranWander'(top dir) 2. pip install -r requirements.txt
for see the result   -->    python run.py