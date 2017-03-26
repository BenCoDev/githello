# std
import unittest
import os
from mock import patch

# project
from mock_github import *


class GithubUnitTest(unittest.TestCase):

	def setUp(self):
		from github_integration import Github
		GITHUB_USER = os.environ["GITHUB_USER"]
		GITHUB_PWD = os.environ["GITHUB_PWD"]
		GITHUB_REPO_NAME = os.environ["GITHUB_REPO_NAME"]
		self.github = Github(GITHUB_USER, GITHUB_PWD, repo_name=GITHUB_REPO_NAME)

	def test_load(self):
		from github_integration import Milestone
		with patch.object(self.github, "get_repo", return_value=mock_repo):
			self.github.load()
			self.assertEquals(len(self.github.issues), 7)
			self.assertEquals(isinstance(self.github.issues[6].milestone, Milestone), True)


class ElementUnitTest(unittest.TestCase):
	pass


class IssueUnitTest(unittest.TestCase):
	pass


class SingleIssueUnitTest(unittest.TestCase):
	pass


class AssociatedIssueUnitTest(unittest.TestCase):
	pass
