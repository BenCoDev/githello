# -*- coding: utf-8 -*-

# std
import copy
from datetime import datetime
import dateutil.parser

# 3p
from trello import TrelloApi
from github_integration import SingleIssue as GithubSingleIssue
from github_integration import AssociatedIssue as GithubAssociatedIssue
from github_integration import Milestone as GithubMilestone


class Trello(TrelloApi):
	APP_NAME = 'Partoo'
	TRELLO_MILESTONE_BOARD_NAME = "TECH - Milestones"
	# TRELLO_MILESTONE_BOARD_NAME = "TEST_MILESTONES"

	TRELLO_SINGLE_ISSUE_BOARD_NAME = "TECH - Issues"
	# TRELLO_SINGLE_ISSUE_BOARD_NAME = "TEST_ISSUES"

	def __init__(self, app_key, token, username=None, user=None):
		super(Trello, self).__init__(app_key, token)
		self.username = username
		self.user = user

	@property
	def milestone_board(self):
		boards = [board for board in self.members.get_board(self.username)
		          if board['name'] == self.TRELLO_MILESTONE_BOARD_NAME]
		return MilestoneBoard(self, **boards[0])

	@property
	def single_issue_board(self):
		boards = [board for board in self.members.get_board(self.username)
		          if board['name'] == self.TRELLO_SINGLE_ISSUE_BOARD_NAME]
		return SingleIssueBoard(self, **boards[0])

	def update(self, issue):
		"""
		Update
		:param issue:
		:return:
		"""
		if isinstance(issue, GithubSingleIssue):
			card = Card.from_github(self, issue)
			existing_card = self.single_issue_board.get_card(card.name)
			if existing_card:
				self.single_issue_board.update_card(existing_card, card.to_json_dict())
			else:
				self.single_issue_board.add_card(card)

		elif isinstance(issue, GithubAssociatedIssue):
			checklist_item = CheckListItem.from_github(self, issue)

			existing_checklist = self.milestone_board.get_checklist(issue.milestone.title)

			if existing_checklist:
				# existing_checklist_item = self.milestone_board.get_checklist_item(checklist_item.name, existing_checklist)
				# if existing_checklist_item:
				# 	pass  # TODO: should update
				# else:
				# 	self.milestone_board.add_checklist_item(checklist_item.to_json_dict(), existing_checklist)
				pass
			else:
				# Should create card ?
				card = self.milestone_board.add_card(Card.from_github(self, issue.milestone))
				checklist = self.milestone_board.add_checklist(CheckList.from_github(self, issue.milestone), card)
				# self.milestone_board.add_checklist_item(checklist_item.to_json_dict(), checklist)

		else: raise Exception

	def refresh_token(self):
		return self.get_token_url(self.APP_NAME, expires='never', write_access=True)


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
		self.cards = [Card(**card) for card in trello_api.boards.get_card_filter("open", kwargs.get("id"))]  # init cards from Trello
		self.lists = [List(**list) for list in trello_api.boards.get_list(kwargs.get("id"))]  # init lists from Trello
		self.checklists = [CheckList(**checklist) for checklist in trello_api.boards.get_checklist(kwargs.get("id"))]  # init checklists from Trello

	def get_card(self, card_name):
		for card in self.cards:
			if card_name == card.name: return card
		return None

	def add_card(self, card):
		resp = self.trello_api.cards.new(
			card.name,
			card.idList,
			desc=card.desc
		)
		added_card = Card(**resp)
		self.cards.append(added_card)
		return added_card

	def update_card(self, card, json_dict):
		"""
		Update card in Trello with data from a json_dict
		:param card: 
		:param json_dict:
		:return:
		"""
		self.trello_api.cards.update(
			card.id,
			**json_dict
		)
		# TODO: implement reload

	def get_checklist(self, checklist_name):
		for checklist in self.checklists:
			if checklist_name == checklist.name: return checklist
		return None

	def add_checklist(self, checklist, card):
		resp = self.trello_api.checklists.new(
			checklist.name,
			card.id
		)
		return CheckList(**resp)

	def get_checklist_item(self, checklist_item_name, checklist):
		checklist_item = self.trello_api.checklists.get_checkItem(
			checklist.id,
			name=checklist_item_name
		)
		if checklist_item:
			return CheckListItem(**checklist_item)
		return None

	def add_checklist_item(self, checklist_item, checklist):
		# TODO implement
		return checklist_item

	def update_checklist_item(self, checklist_item, json_dict):
		pass

	def get_list(self, element):
		return self.lists[self.get_list_index(element)]

	@staticmethod
	def get_list_index(element):
		# Implemented by child
		pass


class MilestoneBoard(Board):
	LIST_NAMES = [
		"Product Backlog",
		"Sprint Backlog",
		"Staging",
		"Prod",
	]

	@staticmethod
	def get_list_index(element):
		if element.state == "closed": return MilestoneBoard.LIST_NAMES.index("Prod")
		elif element.issues: return MilestoneBoard.LIST_NAMES.index("Sprint Backlog")
		elif element.deadline: return MilestoneBoard.LIST_NAMES.index("Sprint Backlog")
		return MilestoneBoard.LIST_NAMES.index("Product Backlog")


class SingleIssueBoard(Board):
	LIST_NAMES = [
		"TOUPGRADE",
		"TODO",
		"DOING",
		"DONE",
		"ARCHIVE"
	]

	@staticmethod
	def get_list_index(element):
		if element.state == "closed":
			if datetime.now().strftime("%W") == dateutil.parser.parse(element.closed_at).strftime("%W"):
				return SingleIssueBoard.LIST_NAMES.index("DONE")
			else:
				return SingleIssueBoard.LIST_NAMES.index("ARCHIVE")
		return SingleIssueBoard.LIST_NAMES.index("TODO")


class List(object):
	"""
	Load raw data from Trello
	"""

	def __init__(self, **kwargs):
		self.id = kwargs.get("id")
		self.name = kwargs.get("name")


class Card(object):
	"""
	Load raw data from json dict
	"""
	def __init__(self, **kwargs):
		self.id = kwargs.get("id")
		self.idList = kwargs.get("idList")
		self.name = kwargs.get("name")
		self.desc = kwargs.get("desc")
		self.labels = kwargs.get("labels", [])
		self.due = kwargs.get("due", None)
		self.closed = kwargs.get("closed", None)

	@classmethod
	def from_github(cls, trello_api, element):
		if isinstance(element, GithubMilestone):
			input_dict = {
				"id": element.id,
				"idList": trello_api.milestone_board.get_list(element).id,
				"name": element.title,
				"desc": element.description,
				"due": element.deadline,
				# "closed": element.state == "closed"
				"closed": False  # do not close them so far
			}
		elif isinstance(element, GithubSingleIssue):
			input_dict = {
				"id": element.id,
				"idList": trello_api.single_issue_board.get_list(element).id,
				"name": element.title,
				"desc": element.description,
				# "closed": element.state == "closed"
				"closed": False  # do not close them so far
			}

		return cls(**input_dict)

	def to_json_dict(self, action="update"):
		if action == "update":
			attrs = ["name", "desc", "closed", "idList", "due"]
			for attr in copy.deepcopy(self).__dict__:
				if attr not in attrs:
					delattr(self, attr)
				elif type(getattr(self, attr)) == bool:  # Convert bool to str
					setattr(self, attr, str(getattr(self, attr)).lower())
		return self.__dict__


class CheckList(object):
	def __init__(self, **kwargs):
		self.id = kwargs.get("id")
		self.name = kwargs.get("name")

	@classmethod
	def from_github(cls, trello_api, element):
		if isinstance(element, GithubMilestone):
			input_dict = {
				"id": element.id,
				# "idList": trello_api.single_issue_board.get_list(element).id,
				"name": element.title,
				# "desc": element.description,
				# "closed": element.state == "closed"
				# "closed": False  # do not close them so far
			}

		return cls(**input_dict)

	def to_json_dict(self, action="update"):
		return self.__dict__


class CheckListItem(object):
	def __init__(self, **kwargs):
		self.id = kwargs.get("id")
		self.name = kwargs.get("name")

	@classmethod
	def from_github(cls, trello_api, element):
		if isinstance(element, GithubAssociatedIssue):
			input_dict = {
				"id": element.id,
				# "idList": trello_api.single_issue_board.get_list(element).id,
				"name": element.title,
				# "desc": element.description,
				# "closed": element.state == "closed"
				# "closed": False  # do not close them so far
			}

		return cls(**input_dict)

	def to_json_dict(self, action="update"):
		return self.__dict__
#
#
# TRELLO_USER = os.environ["TRELLO_USER"]
# TRELLO_APP_KEY = os.environ["TRELLO_APP_KEY"]
# TRELLO_TOKEN = os.environ["TRELLO_TOKEN"]
# t = Trello(TRELLO_APP_KEY, TRELLO_TOKEN, username=TRELLO_USER)
#
# milestone = GithubMilestone(**{
#
# })
# t.update(GithubAssociatedIssue(**{
# 	"title": "HELLO",
# 	"state": "closed",
# 	"description": "OK GO",
# 	"closed_at": u'2017-01-26T11:53:05Z',
# 	"milestone": {"id": "fake_id", "title": "OK OK"}
# }))