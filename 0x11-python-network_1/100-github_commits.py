import os

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    
    token = os.getenv('GITHUB_TOKEN')
    headers = {}
    
    if token:
        headers['Authorization'] = f'token {token}'
    
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url, headers=headers)
    
    commits = response.json()
    
    for commit in commits[:10]:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author}")

