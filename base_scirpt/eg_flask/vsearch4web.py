from flask import Flask, render_template,request,redirect,escape
import mysql.connector

app = Flask(__name__)

def search4letters(phrase: str,letters: str='aeiou') -> set:
    """Return the set of 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))

@app.route('/test')
def hello() -> '302':
    return redirect('/entry')

def log_request(req: 'flask_request',res:str) -> None:
    """log the results to mysql DB"""

    dbconfig = {'host': '212.64.16.9', 'user': 'vsearch', 'password': 'pass1234i56', 'database': 'vsearchlogDB', }
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()

    _SQL = """insert into log (phrase,letters,ip,browser_string,results) values (%s,%s,%s,%s,%s)"""

    cursor.execute(_SQL, (req.form['phrase'],req.form['letters'],req.remote_addr,req.user_agent.browser,res,))
    conn.commit()

# def log_request(req: 'flask_request',res:str) -> None:
#     """log result to txt"""
#     with open('vsearch.log','a') as log:
#         print(req.form,req.remote_addr,req.user_agent,res,file=log,sep='|')
# @app.route('/viewlog')
# def view_the_log() -> 'html':
#     """show log from vsearch.log with html"""
#     contents = []
#     with open('vsearch.log') as log:
#         for line in log:
#             contents.append([])
#             for item in line.split('|'):
#                 contents[-1].append(escape(item))
#     titles = ('FOrm Data','Remote_addr','User_agent','Results')
#     return render_template('viewlog.html',
#                            the_title='View Log',
#                            the_row_titles=titles,
#                            the_data=contents,)

@app.route('/search4',methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase,letters))
    log_request(request,results)
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

