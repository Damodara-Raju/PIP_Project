import requests

TOKEN = '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'
GIT_HUB_URL = {
    'github_api_root': 'https://api.github.com/',
    'get_github_meta_information': 'https://api.github.com/meta',
    'get_octocat': ' https://api.github.com/octocat',
    'get_all_api_versions': 'https://api.github.com/versions',
    'get_the_zen_of_github': ' https://api.github.com/zen'
}


def get_github_api_root():
    response = requests.get(url=GIT_HUB_URL.get('github_api_root'), headers=get_headers())
    response.raise_for_status()
    if response.status_code == 200:
        return response.json()


def get_github_meta_information():
    response = requests.get(url=GIT_HUB_URL.get('get_github_meta_information'), headers=get_headers())
    response.raise_for_status()
    if response.status_code == 200:
        return response.json()


def get_octocat():
    response = requests.get(url=GIT_HUB_URL.get('get_octocat'), headers=get_headers())
    response.raise_for_status()
    if response.status_code == 200:
        return response.text


def get_all_api_versions():
    response = requests.get(url=GIT_HUB_URL.get('get_all_api_versions'), headers=get_headers())
    response.raise_for_status()
    if response.status_code == 200:
        return response.json()


def get_the_zen_of_github():
    response = requests.get(url=GIT_HUB_URL.get('get_the_zen_of_github'), headers=get_headers())
    response.raise_for_status()
    if response.status_code == 200:
        return response.text


def get_headers():

    headers = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'Authorization': f'Bearer {TOKEN}',
    }

    return headers


root_data = get_github_api_root()
meta_data = get_github_meta_information()
octo_data = get_octocat()
api_versions_data = get_all_api_versions()
zen_data = get_the_zen_of_github()

print(root_data)
print(meta_data)
print(octo_data)
print(api_versions_data)
print(zen_data)
