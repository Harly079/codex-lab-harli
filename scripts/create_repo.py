import os
import base64
import requests

GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
REPO_NAME = os.getenv('REPO_NAME')
TOKEN = os.getenv('GITHUB_TOKEN')

README_CONTENT = """# QG IA STRATEGIQUE

Bienvenue dans le centre névralgique de l’orchestration IA signée Harli ∞ Mind. 🚀
Ce dépôt contient :
- L’arborescence Notion
- Les agents intelligents actifs
- Les templates & prompts
- Les dashboards (PNB, CIC, ALM)
"""

def create_repo():
    url = 'https://api.github.com/user/repos'
    headers = {'Authorization': f'token {TOKEN}',
               'Accept': 'application/vnd.github.v3+json'}
    data = {'name': REPO_NAME,
            'private': False,
            'auto_init': False}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print('\u2714\ufe0f Dépôt créé')
        return True
    else:
        print(response.json())
        return False

def create_readme():
    create_readme_url = f'https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}/contents/README.md'
    headers = {'Authorization': f'token {TOKEN}',
               'Accept': 'application/vnd.github.v3+json'}
    encoded_readme = base64.b64encode(README_CONTENT.encode('utf-8')).decode('utf-8')
    data = {
        'message': 'Ajout du README initial',
        'content': encoded_readme,
        'branch': 'main'
    }
    r = requests.put(create_readme_url, headers=headers, json=data)
    if r.status_code == 201:
        print('\ud83d\udcd8 README ajouté')
    else:
        print(r.json())

if __name__ == '__main__':
    if not all([GITHUB_USERNAME, REPO_NAME, TOKEN]):
        print('Configurez GITHUB_USERNAME, REPO_NAME et GITHUB_TOKEN en variables d\'environnement.')
    else:
        if create_repo():
            create_readme()
