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
repo_traffic = RepoTraffic(username, password)
repo_traffic.cache_repo("pullword")
print repo_traffic.get_all_data()
```
