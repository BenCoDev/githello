# -*- coding: utf-8 -*-

# std
import logging.config

# 3p
from github import Github as GithubApi
from unidecode import unidecode

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)


class Github(GithubApi):

	def __init__(self, username, pwd, repo_name=None, user=None):
		logging.info("Github - Init")

		super(Github, self).__init__(username, pwd)

		self.repo_name = repo_name
		self.user = user

	def load(self):
		"""
		Iterate over Github issues
		
		yield Github issue

		:return:
		"""
		issues = self.get_repo(self.repo_name).get_issues(state="all")

		total_count = issues.totalCount

		for index, issue in enumerate(issues):
			logging.info("Github - Loading issue {} / {} ".format(index + 1, total_count))

			# If Github issue has milestones, create/update milestone
			github_issue = Issue(**issue.raw_data)

			if github_issue.milestone_id: github_issue = AssociatedIssue(**issue.raw_data)
			else: github_issue = SingleIssue(**issue.raw_data)

			yield github_issue


class Element(object):

	def __init__(self, **kwargs):
		self.id = kwargs.get("id")
		self.title = kwargs.get("title")
		self.description = kwargs.get("description")
		self.state = kwargs.get("state")

	def to_json_dict(self):
		return self.__dict__

	def __repr__(self):
		return u"{} <{} {}>".format(self.__class__.__name__, self.id, unidecode(self.title))


class Milestone(Element):

	def __init__(self, **kwargs):
		super(Milestone, self).__init__(**kwargs)
		self.deadline = kwargs.get("deadline")
		self.issues = set()

	def has_closed_issues(self):
		return len([issue for issue in list(self.issues) if issue.state == "closed"]) >= 1

	def has_open_issues(self):
		return len([issue for issue in list(self.issues) if issue.state == "open"]) >= 1


class Issue(Element):
	def __init__(self, **kwargs):
		super(Issue, self).__init__(**kwargs)
		self.milestone_id = kwargs.get("milestone", {}).get("id", None) if kwargs.get("milestone") else None
		self.assignees = [assignee["login"] for assignee in kwargs.get("assignees", [])]
		self.closed_at = kwargs.get("closed_at")


class SingleIssue(Issue):
	def __init__(self, **kwargs):
		super(SingleIssue, self).__init__(**kwargs)


class AssociatedIssue(Issue):
	def __init__(self, **kwargs):
		super(AssociatedIssue, self).__init__(**kwargs)
		self.milestone = Milestone(**kwargs.get("milestone", {}))
