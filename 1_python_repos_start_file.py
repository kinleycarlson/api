import requests
import json

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)      #making a request
print(f"Status code: {r.status_code}")
##formatted string literal
##variables go in curly brackets


outfile = open('output.json','w')

response_dict = r.json()
#print(response_dict)
    #json method translates it into a dictionary

json.dump(response_dict,outfile,indent = 4)

# number of respositorys
list_of_repos = response_dict["items"]
print(f"Number of repos: {len(list_of_repos)}")

#examine the repo
first_repo_dict = list_of_repos[0]

print(first_repo_dict)

#number of keys in each repo
print(f"Number of Keys: {len(first_repo_dict)}")

for key in first_repo_dict:
    print(key)

#check details for 1st repo
print("\nSelected information about first repository")

print(f"Name: {first_repo_dict['name']}")
print(f"Owner: {first_repo_dict['owner']['login']}")
print(f"Stars: {first_repo_dict['stargazers_count']}")
print(f"HTML Url: {first_repo_dict['html_url']}")
print(f"Created: {first_repo_dict['created_at']}")
print(f"Updated: {first_repo_dict['updated_at']}")
print(f"Description: {first_repo_dict['description']}")
print()
print()


print('first 10 repos')
#first 10 repos
for repo in list_of_repos[:10]:
    try:
        print(f"Name: {repo['name']}")
        print(f"Owner: {repo['owner']['login']}")
        print(f"Stars: {repo['stargazers_count']}")
        print(f"HTML Url: {repo['html_url']}")
        print(f"Created: {repo['created_at']}")
        print(f"Updated: {repo['updated_at']}")
        print(f"Description: {repo['description']}") 
        print()
        print()
    except:
        pass

from plotly.graph_objs import bar 
from plotly import offline

repo_names, stars = [], []

#top 10 repos

for repo in list_of_repos[:10]:
    repo_names.append(repo['name'])
    stars.append(repo['stargazers_count'])

data = [
    {
        "type": "bar",
        "x": repo_names,
        "y": stars,
        "marker":{
            "color": "rgb(60,100,150)",
            "line":{"width": 1.5, "color": "rgb(25,25,25)"},
        },
        "opacity": 0.6,
        }
]

my_layout = {
    "title": "Most Starred Python Projects on Github",
    "xaxis": {"title": "Repository"},
    "yaxis": {"title": "Stars"},
    }

fig  = {"data": data, "layout": my_layout}

offline.plot(fig, filename="python_repos.html")


