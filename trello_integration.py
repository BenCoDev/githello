# -*- coding: utf-8 -*-


# 3p
from trello import TrelloApi


class Trello(TrelloApi):
	TRELLO_MILESTONE_BOARD_NAME = "TECH - Milestones"
	TRELLO_SINGLE_ISSUE_BOARD_NAME = "TECH - Issues"

	def __init__(self, app_key, token, username=None, user=None):
		super(Trello, self).__init__(app_key, token)
		self.username = username
		self.user = user

	@property
	def milestone_board(self):
		boards = [board for board in self.members.get_board(self.username) if board['name'] == self.TRELLO_MILESTONE_BOARD_NAME]
		return Board(self, **boards[0])

	@property
	def single_issue_board(self):
		boards = [board for board in self.members.get_board(self.username) if board['name'] == self.TRELLO_SINGLE_ISSUE_BOARD_NAME]
		return Board(self, **boards[0])

	def refresh_token(self):
		return self.get_token_url('Partoo', expires='never', write_access=True)


class Board(object):
	"""
	Load raw data from Trello
	"""
	LIST_NAMES = [
		"TODO",
		"DOING",
		"DONE",
	]

	def __init__(self, trello_api, **kwargs):
		self.trello_api = trello_api
		self.id = kwargs.get("id")
		self.name = kwargs.get("name")
		self.cards = [Card(**card) for card in trello_api.boards.get_card_filter("open", kwargs.get("id"))]
		self.lists = [List(**list) for list in trello_api.boards.get_list(kwargs.get("id"))]

	def update(self, milestone_or_issue):
		# Is there already a card for this milestone ?
		existing_card = [card for card in self.cards if milestone_or_issue.title == card.name]

		if existing_card:
			existing_card = existing_card[0]
			self.trello_api.cards.update(existing_card.id, desc=milestone_or_issue.description)

		else:
			self.trello_api.cards.new(milestone_or_issue.title, self.lists[milestone_or_issue.get_list_index(self.LIST_NAMES)].id,
			                          desc=milestone_or_issue.description)


class Card(object):
	"""
		Load raw data from Trello
		"""

	def __init__(self, **kwargs):
		self.id = kwargs.get("id")
		self.name = kwargs.get("name")


class MilestoneBoard(Board):
	LIST_NAMES = [
		"Product Backlog",
		"Sprint Backlog",
		"Staging",
		"Prod",
	]

	def __init__(self, **kwargs):
		super(MilestoneBoard, self).__init__(**kwargs)


class SingleIssueBoard(Board):
	LIST_NAMES = [
		"TODO",
		"DOING",
		"DONE",
	]

	def __init__(self, **kwargs):
		super(SingleIssueBoard, self).__init__(**kwargs)


class List(object):
	"""
	Load raw data from Trello
	"""

	def __init__(self, **kwargs):
		self.id = kwargs.get("id")
		self.name = kwargs.get("name")


class CheckList(object):
	def __init__(self, **kwargs):
		self.id = kwargs.get("id")


class CheckListItem(object):
	def __init__(self, **kwargs):
		self.id = kwargs.get("id")
