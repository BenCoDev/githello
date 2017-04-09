# std
import unittest

# project
from mock_trello import *


class TrelloUnitTest(unittest.TestCase):
	pass


class BoardUnitTest(unittest.TestCase):
	def setUp(self):
		from trello_integration import Board
		self.board = Board(mock_trello_api, **{
			"id": u"58ac046faad15d151e3b3623",  # Single Issues Board
			"name": u"Test name"
		})

	def test_get_card(self):
		"""
		Expect proper card to be returned
		:return:
		"""
		from trello_integration import Card
		from github_integration import SingleIssue
		card = Card.from_github(mock_trello_api, SingleIssue(**{
			"id": u"test_id",
			"title": u'Issue Super Name 3',
			"description": u"Lorem Ipsum",
			"state": u"open"
		}))
		self.assertEquals(self.board.get_card(card.name).name, card.name)
		self.assertEquals(self.board.get_card("Card does not exist"), None)

	def test_add_card(self):
		"""
		Expect card to be added to the board
		:return:
		"""
		from trello_integration import Card
		from github_integration import SingleIssue
		card = Card.from_github(mock_trello_api, SingleIssue(**{
			"id": u"test_id",
			"title": u'Issue Super Name 3',
			"description": u"Lorem Ipsum",
			"state": u"open"
		}))
		self.assertEquals(type(self.board.add_card(card)), Card)

	def test_update_card(self):
		"""
		Expect proper card to be added
		:return:
		"""
		card = self.board.get_card(u'Issue Super Name 3')

		self.assertEquals(self.board.update_card(card, {
			"desc": "New description"
		}), None)

	def test_get_checklist_item(self):
		from trello_integration import CheckListItem
		from github_integration import AssociatedIssue
		checklist_item = CheckListItem.from_github(mock_trello_api, AssociatedIssue(**{
			"id": u"test_id",
			"title": u'Issue Super Name 3',
			"description": u"Lorem Ipsum",
			"state": u"open"
		}))
		# self.assertEquals(self.board.get_card(card.name).name, card.name)
		# self.assertEquals(self.board.get_card("Card does not exist"), None)

	def test_add_checklist_item(self):
		pass


class MilestoneBoardUnitTest(unittest.TestCase):
	pass


class SingleIssueBoardUnitTest(unittest.TestCase):
	pass


class ListUnitTest(unittest.TestCase):
	pass


class CardUnitTest(unittest.TestCase):
	pass

class CheckListUnitTest(unittest.TestCase):
	pass


class CheckListItemUnitTest(unittest.TestCase):
	pass
