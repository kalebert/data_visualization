import requests

# Make an API call and store the response. 
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {
	'Accept': 'application/json', 
	'Content-Type': 'application/json'
	}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repo
repo_dict = repo_dicts[0]

# Code used to examine all keys in dictonary
# print(f"\nKeys: {len(repo_dict)}")
#for key in sorted(repo_dict.keys()):
	#print(key)

print(f"\nSelected information about each repository:")
for repo_dict in repo_dicts:
	print(f"\nName: {repo_dict['name']}")
	print(f"Owner: {repo_dict['owner']['login']}")
	print(f"Stars: {repo_dict['stargazers_count']}")
	print(f"Repository: {repo_dict['html_url']}")
	print(f"Decription: {repo_dict['description']}")
