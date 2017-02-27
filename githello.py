# -*- coding: utf-8 -*-

# std
import logging.config

# 3p

# project
from user import User


logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('githello')


def run(board_type="milestone_board"):
	"""
	Run
	:param board_type:
	:return:
	"""
	user = User()
	if board_type == "milestone_board":
		[getattr(user.trello, board_type).update(milestone) for milestone in user.github.milestones]
	else:
		[getattr(user.trello, board_type).update(issue) for issue in user.github.single_issues]


run(board_type="single_issue_board")
# Define objective
# Define use cases
# Place on heroku with cron
# Implement cache to tests
# Priority to Github

# A new github milestone has been created
# A trello card has been modified
# An existing github milestone has been updated
# An issue has been added to a milestone on Github

# Attributes sync
# Github milestone ==> Trello card with label Milestone
# Github milestone issue ==> Trello check list of the Milestone
# Github milestone issue state ==> Trello check list of the Milestone with the check attribute
# Github milestone assignee ==> Trello card member
# Github milestone deadline ==> Trello card deadline
# Github milestone name ==> Trello card name

