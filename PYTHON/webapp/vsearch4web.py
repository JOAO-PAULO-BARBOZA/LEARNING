from flask import Flask, render_template, request, escape
from vsearch import search4letters

app = Flask(__name__)
# Nesse caso 'log' é a variável que estou definindo
# req = request e res = response, que são as solicitações e respostas do server respectivamente.

def log_request(req: 'flask_request', res: str) -> None:
    """Cria e abre um aquivo na extensão .log. O 'a' significa appende. """
    with open('vsearch.log', 'a') as log:
#Com esse print o req e o res vão ser adcionados ao arquivo vsearch.log
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep=' | ')

@app.route('/search4', methods=['POST'])
def go_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html', the_phrase = phrase, the_title = title,the_letters= letters, the_results= results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search for letters on the web!')

@app.route('/viewlog')                                                 
def view_the_log() -> str:
    with open('vsearch.log') as log:
        contents = log.read()
    return escape(contents)

if __name__ == '__main__':
    app.run(debug=True)
