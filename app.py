from flask import Flask, render_template, request, flash
from github import Github
import os

app = Flask(__name__)
app.secret_key = 'MiClaveSuperSecreta123!'  # Puedes cambiarla

# CONFIGURA ESTO:
GITHUB_TOKEN = 'tu_token_aqui'  # <-- pon aquí tu token de GitHub
REPO_NAME = 'Usuario/carpeta'
BRANCH = 'main'

g = Github(GITHUB_TOKEN)
repo = g.get_repo(REPO_NAME)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            content = file.read().decode('utf-8')
            path_in_repo = f'txt/{file.filename}'

            try:
                contents = repo.get_contents(path_in_repo, ref=BRANCH)
                repo.update_file(contents.path, f'Update {file.filename}', content, contents.sha, branch=BRANCH)
            except Exception:
                repo.create_file(path_in_repo, f'Add {file.filename}', content, branch=BRANCH)

            flash(f'Archivo "{file.filename}" subido a GitHub en la carpeta txt.', 'success')
        else:
            flash('No se seleccionó ningún archivo.', 'error')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
