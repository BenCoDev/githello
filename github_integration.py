# -*- coding: utf-8 -*-

# std
import logging.config

# 3p
from github import Github as GithubApi

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)


ITEM_LIST_MATCHING = {
	"issue": "issues",
	"milestone": "milestones"
}


class Github(GithubApi):

	def __init__(self, username, pwd, repo_name=None, user=None):
		logging.info("Github - Init")

		super(Github, self).__init__(username, pwd)

		self.repo_name = repo_name
		self.milestones = set()
		self.issues = set()
		self.user = user

	def load(self):
		"""
		Iterate over Github issues

		Append data in self.milestones if is a issue has a milestone
		Append data in self.issues

		FIXME: Limit: using list to store the issues, should use generator and fetch one by one and process one by one
		:return:
		"""
		logging.info("Github - Loading milestones")

		issues = self.get_repo(self.repo_name).get_issues(state="all")

		total_count = len(list(issues)) or issues.totalCount

		for index, issue in enumerate(issues):
			logging.info("Github - Loading issue {} / {} ".format(index + 1, total_count))

			# If Github issue has milestones, create/update milestone
			github_issue = Issue(**issue.raw_data)

			if github_issue.milestone_id:
				github_issue = AssociatedIssue(**issue.raw_data)
				milestone = Milestone(**issue.raw_data["milestone"])
				self.add(milestone, "milestone")
			else:
				github_issue = SingleIssue(**issue.raw_data)

			self.add(github_issue, "issue")

	def add(self, new_item, item_label):
		"""
		Add an item to a list
		:param new_item: {object} - can be an Issue or a Milestone instance
		 :param item_label: {str} - "milestone" | "issue"
		:return: 
		"""
		if new_item.id not in [item.id for item in getattr(self, ITEM_LIST_MATCHING[item_label])]:
			logging.info("Adding {} to {}".format(new_item, self))
			getattr(self, ITEM_LIST_MATCHING[item_label]).add(new_item)
		return new_item


class Element(object):

	def __init__(self, **kwargs):
		self.id = kwargs.get("id")
		self.title = kwargs.get("title")
		self.description = kwargs.get("description")
		self.state = kwargs.get("state")

	def to_json_dict(self):
		return self.__dict__

	def __repr__(self):
		return "{} <{} {}>".format(self.__class__.__name__, self.id, self.title)


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


class SingleIssue(Issue):
	def __init__(self, **kwargs):
		super(SingleIssue, self).__init__(**kwargs)


class AssociatedIssue(Issue):
	def __init__(self, **kwargs):
		super(AssociatedIssue, self).__init__(**kwargs)
