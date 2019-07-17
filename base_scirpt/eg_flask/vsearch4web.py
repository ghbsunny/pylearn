from flask import Flask, render_template,request,redirect

app = Flask(__name__)

def search4letters(phrase: str,letters: str='aeiou') -> set:
    """Return the set of 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))

@app.route('/test')
def hello() -> '302':
    return redirect('/entry')

@app.route('/search4',methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase,letters))
    title = 'Here are your results:'
    return render_template('results.html',
                           the_phrase = phrase,
                           the_letters = letters,
                           the_title = title,
                           the_results = results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title="welcome to search4letters on the web!")
if __name__ == '__main__':
    app.run(port=5002,debug=True)
