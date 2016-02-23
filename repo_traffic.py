#!/usr/bin/env python
# coding=utf-8

import sys
from requests import session
from bs4 import BeautifulSoup as bs
import json

headers = {
    'Origin': 'https://github.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Referer': 'https://github.com/',
    'Connection': 'keep-alive',
}



class RepoTraffic:
    def __init__(self, username, password):
        s = session()
        login_url = "https://github.com/login"
        session_url = "https://github.com/session"
        req = s.get(login_url).content 
        html_object = bs(req, "html.parser")
        token = html_object.find("input", {"name": "authenticity_token"}).attrs['value']
        com_val = html_object.find("input", {"name": "commit"}).attrs['value']  
        login_data = {'login': username,
                    'password': password,
                    'commit' : com_val,
                    'authenticity_token' : token}    
        login_req = s.post(session_url, data = login_data, headers=headers)
        self.s = s

    def parse_top_list(self, top_list_data):
        pass

    def get_data(self, repo_name):
        clone_data_url = "https://github.com/binhe22/pullword/graphs/clone-activity-data"
        traffic_data_url = "https://github.com/binhe22/pullword/graphs/clone-activity-data"
        top_list_url = "https://github.com/binhe22/pullword/graphs/traffic?partial=top_lists"

        top_list = self.s.get(top_list_url, headers=headers)
        headers["Referer"] = "https://github.com/binhe22/pullword/graphs/traffic"
        headers["Accept"] = "application/json"
        clone_data = self.s.get(clone_data_url, headers=headers)
        traffic_data = self.s.get(traffic_data_url, headers=headers)
        clone_data_json = json.loads(clone_data.content)
        traffic_data_json = json.loads(traffic_data.content)


        print traffic_data.content
        print top_list.content

        


if __name__ == "__main__":
    inputs = sys.argv    
    if len(inputs) != 4:
        print """
        args num is wrong, you can use by:
        ./repo_traffic.py username password repo_name
        for example:
        ./repo_traffic.py ***@gmail.com 12312312 repo_traffic
        """
    username = sys.argv[1]
    password = sys.argv[2]
    repo_name = sys.argv[3]
    repo_traffic = RepoTraffic(username, password)
    repo_traffic.get_data("pullword")