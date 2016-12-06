from app import app

def read_kjv_verse():
    verses = []
    with open('kjv.tsv') as rfp:
        for line in rfp:
            line = line.strip()
            if line:
                verses.append(line.split('\t'))
    for verse in verses:
        verse[1] = int(verse[1])
        verse[2] = int(verse[2])
    return verses

@app.route('/')
@app.route('/index')
def index():
    verses = read_kjv_verses()
    page = ''
    for verse in verses[100]:
        page += '<p>Book: {} Chapter: {} Verse: {} Text: {}<p>\n'.format(verse[1], verse[2], verse[3]
        )
    return page