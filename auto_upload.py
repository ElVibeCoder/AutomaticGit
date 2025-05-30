import schedule
import time
from github import Github

GITHUB_TOKEN = 'tu_token'
REPO_NAME = 'Pepehige/UploadDaily'
BRANCH = 'main'
PATH_LOCAL = 'txt/readme.txt'

def subir_archivo():
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)

    with open(PATH_LOCAL, 'r', encoding='utf-8') as f:
        content = f.read()

    path_in_repo = 'txt/readme.txt'

    try:
        contents = repo.get_contents(path_in_repo, ref=BRANCH)
        repo.update_file(contents.path, "Auto update daily", content, contents.sha, branch=BRANCH)
        print("Archivo actualizado en GitHub.")
    except:
        repo.create_file(path_in_repo, "Auto add daily", content, branch=BRANCH)
        print("Archivo subido a GitHub.")

# Ejecutar a una hora específica cada día (ejemplo: 13:00)
schedule.every().day.at("13:00").do(subir_archivo)

print("Esperando para subir automáticamente...")

while True:
    schedule.run_pending()
    time.sleep(60)
