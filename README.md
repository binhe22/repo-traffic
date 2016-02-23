# repo-traffic
Crawl the github repo traffic data.

## Usage:
### Command
```./repo_traffic.py username password repo_name```

###Use in code
```
from repo_traffic import RepoTraffic
username = ""#email
password = ""
repo_name = ""
repo_traffic = RepoTraffic(username, password)
repo_traffic.cache_repo(repo_name)
print repo_traffic.get_all_data()
print repo_traffic.get_visit_data()
print repo_traffic.get_clone_data()
print repo_traffic.get_reffer_sites()
print repo_traffic.get_popular_content()
```
