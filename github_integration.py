# -*- coding: utf-8 -*-

# std
import logging.config

# 3p
from github import Github as GithubApi

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)


class Github(GithubApi):
	def __init__(self, username, pwd, repo_name=None, user=None):
		logging.info("Github - Init")
		super(Github, self).__init__(username, pwd)
		self.repo_name = repo_name

		self.milestones = []
		self.single_issues = []
		self.load()

		self.user = user

	def load(self):
		logging.info("Github - Loading milestones")

		issues = self.get_repo(self.repo_name).get_issues(state="all")

		total_count = issues.totalCount or len(list(issues))

		for index, issue in enumerate(issues):
			logging.info("Github - Loading issue {} / {} ".format(index + 1, total_count))

			# If Github issue has milestones, create/update milestone
			github_issue = Issue(**issue.raw_data)

			if github_issue.milestone_id:

				github_issue = AssociatedIssue(**issue.raw_data)

				github_milestone = Milestone(**issue.raw_data["milestone"])

				if github_milestone.id in [milestone.id for milestone in self.milestones]:
					milestone = [milestone for milestone in self.milestones if milestone.id == github_milestone.id][0]
				else:
					milestone = github_milestone
					self.milestones.append(milestone)

				milestone.add_issue(github_issue)

			else:
				github_issue = SingleIssue(**issue.raw_data)
				if github_issue.id in [issue.id for issue in self.single_issues]:
					pass
				else:
					self.single_issues.append(github_issue)


class Milestone(object):

	def __init__(self, **kwargs):
		self.id = kwargs.get("id")
		self.title = kwargs.get("title")
		self.description = kwargs.get("description")
		self.state = kwargs.get("state")
		self.deadline = kwargs.get("deadline")
		self.issues = set()

	def get_list_index(self, lists=None):
		if not lists: lists = []

		if self.state == "closed": return len(lists) - 1
		else:
			if not self.issues: return 0
			elif not self.deadline: return 0
			else: return 1

	def add_issue(self, issue):
		self.issues.add(issue)

	def has_closed_issues(self):
		return len([issue for issue in list(self.issues) if issue.state == "closed"]) >= 1

	def has_open_issues(self):
		return len([issue for issue in list(self.issues) if issue.state == "open"]) >= 1

	def __repr__(self):
		return "{} {}".format(self.__class__, self.title)


class Issue(object):
	def __init__(self, **kwargs):
		self.id = kwargs.get("id")
		self.title = kwargs.get("title")
		self.description = kwargs.get("description")
		self.milestone_id = kwargs.get("milestone", {}).get("id", None) if kwargs.get("milestone") else None
		self.state = kwargs.get("state")
		self.assignees = [assignee["login"] for assignee in kwargs.get("assignees", [])]

	def __repr__(self):
		return "{} {}".format(self.__class__, self.title)


class SingleIssue(Issue):
	def __init__(self, **kwargs):
		super(SingleIssue, self).__init__(**kwargs)

	def get_list_index(self, lists=None):
		if not lists: lists = []

		if self.state == "closed":
			return len(lists) - 1
		else:
			return 0


class AssociatedIssue(Issue):
	def __init__(self, **kwargs):
		super(AssociatedIssue, self).__init__(**kwargs)
