# std
import unittest
import os

# 3p

# project
from mock_github import *


class GithubUnitTest(unittest.TestCase):

	def setUp(self):
		from github_integration import Github

		GITHUB_USER = os.environ["GITHUB_USER"]
		GITHUB_PWD = os.environ["GITHUB_PWD"]
		GITHUB_REPO_NAME = os.environ["GITHUB_REPO_NAME"]

		self.github = Github(GITHUB_USER, GITHUB_PWD, repo_name=GITHUB_REPO_NAME)

		self.github.get_repo = mock_get_repo

	def test_load(self):
		"""
		Expect len of generator to be 7
		:return: 
		"""
		from github_integration import AssociatedIssue
		issues = []

		for issue in self.github.load():
			issues.append(issue)

		self.assertEquals(len(issues), 7)
		self.assertEquals(isinstance(issues[6], AssociatedIssue), True)


class ElementUnitTest(unittest.TestCase):
	pass


class IssueUnitTest(unittest.TestCase):
	pass


class SingleIssueUnitTest(unittest.TestCase):
	pass


class AssociatedIssueUnitTest(unittest.TestCase):
	pass
