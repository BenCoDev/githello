# -*- coding: utf-8 -*-

# std
import os

# 3p

# project
from trello_integration import Trello
from github_integration import Github

GITHUB_USER = os.environ["GITHUB_USER"]
GITHUB_PWD = os.environ["GITHUB_PWD"]
GITHUB_REPO_NAME = os.environ["GITHUB_REPO_NAME"]
TRELLO_USER = os.environ["TRELLO_USER"]
TRELLO_APP_KEY = os.environ["TRELLO_APP_KEY"]
TRELLO_TOKEN = os.environ["TRELLO_TOKEN"]


class User(object):
	def __init__(self):
		self.github = Github(GITHUB_USER, GITHUB_PWD, repo_name=GITHUB_REPO_NAME, user=self)
		self.trello = Trello(TRELLO_APP_KEY, TRELLO_TOKEN, username=TRELLO_USER, user=self)
