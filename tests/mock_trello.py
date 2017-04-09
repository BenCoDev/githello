# std
from mock import Mock

mock_boards = [
	{
		u'id': u'58aabccb312e1c62277e84c5',
		u'datePluginDisable': None,
		u'subscribed': False,
		u'idTags': [],
		u'pinned': None,
		u'shortUrl': u'https://trello.com/b/asdf1',
		u'closed': False,
		u'prefs': {
			u'permissionLevel': u'org',
			u'cardCovers': True,
			u'backgroundColor': u'#4BBF6B',
			u'selfJoin': True,
			u'backgroundBrightness': u'dark',
			u'comments': u'members',
			u'invitations': u'members',
			u'canBePrivate': True,
			u'canInvite': True,
			u'backgroundImage': None,
			u'backgroundTile': False,
			u'background': u'lime',
			u'canBeOrg': True,
			u'cardAging': u'regular',
			u'backgroundImageScaled': None,
			u'calendarFeedEnabled': False,
			u'voting': u'disabled',
			u'canBePublic': True
		},
		u'dateLastActivity': u'2017-02-27T11:52:55.705Z',
		u'invitations': None,
		u'dateLastView': u'2017-03-24T14:35:28.755Z',
		u'powerUps': [],
		u'desc': u'',
		u'descData': None,
		u'labelNames': {
			u'blue': u'',
			u'pink': u'',
			u'purple': u'',
			u'sky': u'',
			u'yellow': u'ISSUES',
			u'green': u'MILESTONES',
			u'orange': u'',
			u'black': u'',
			u'red': u'',
			u'lime': u''
		},
		u'name': u'TECH - Milestones',
		u'shortLink': u'asdf1',
		u'idOrganization': u'54ec93cca4c1d554799bcc43',
		u'invited': False,
		u'memberships': [{
			u'deactivatedAtEnterprise': False,
			u'deactivated': False,
			u'memberType': u'admin',
			u'idMember': u'52e96e11f0d5b54d5fd4d4bb',
			u'_id': u'58aabccb312e1c62277e84c6',
			u'unconfirmed': False
		},
			{
				u'deactivatedAtEnterprise': False,
				u'deactivated': False,
				u'memberType': u'normal',
				u'idMemberAdder': u'52e96e11f0d5b54d5fd4d4bb',
				u'idMember': u'58b3e16e384a672e674ee484',
				u'_id': u'58b5775800cc7f6d927f3d69',
				u'unconfirmed': False
			}],
		u'url': u'https://trello.com/b/5fFaq41u/tech-milestones',
		u'starred': False
	},
	{
		u'id': u'58ac046faad15d151e3b3623',
		u'datePluginDisable': None,
		u'subscribed': False,
		u'idTags': [],
		u'pinned': None,
		u'shortUrl': u'https://trello.com/b/asdf2',
		u'closed': False,
		u'prefs': {
			u'permissionLevel': u'org',
			u'cardCovers': True,
			u'backgroundColor': u'#CD5A91',
			u'selfJoin': True,
			u'backgroundBrightness': u'dark',
			u'comments': u'members',
			u'invitations': u'members',
			u'canBePrivate': True,
			u'canInvite': True,
			u'backgroundImage': None,
			u'backgroundTile': False,
			u'background': u'pink',
			u'canBeOrg': True,
			u'cardAging': u'regular',
			u'backgroundImageScaled': None,
			u'calendarFeedEnabled': False,
			u'voting': u'disabled',
			u'canBePublic': True
		},
		u'dateLastActivity': u'2017-03-24T17:52:03.739Z',
		u'invitations': None,
		u'dateLastView': u'2017-03-24T17:57:32.476Z',
		u'powerUps': [],
		u'desc': u'',
		u'descData': None,
		u'labelNames': {
			u'blue': u'',
			u'pink': u'',
			u'purple': u'',
			u'sky': u'',
			u'yellow': u'',
			u'green': u'',
			u'orange': u'',
			u'black': u'',
			u'red': u'Prioritary',
			u'lime': u''
		},
		u'name': u'TECH - Issues',
		u'shortLink': u'asdf2',
		u'idOrganization': u'54ec93cca4c1d554799bcc43',
		u'invited': False,
		u'memberships': [
			{
				u'deactivatedAtEnterprise': False,
				u'deactivated': False,
				u'memberType': u'admin',
				u'idMember': u'52e96e11f0d5b54d5fd4d4bb',
				u'_id': u'58ac046faad15d151e3b3624',
				u'unconfirmed': False
			},
			{
				u'deactivatedAtEnterprise': False,
				u'deactivated': False,
				u'memberType': u'normal',
				u'idMemberAdder': u'52e96e11f0d5b54d5fd4d4bb',
				u'idMember': u'58b3e16e384a672e674ee484',
				u'_id': u'58b5771e8a23bae326b43e3e',
				u'unconfirmed': False
			},
			{
				u'deactivatedAtEnterprise': False,
				u'deactivated': False,
				u'memberType': u'normal',
				u'idMemberAdder': u'58105a30f8a05bb56aaa3f42',
				u'idMember': u'58105a30f8a05bb56aaa3f42',
				u'_id': u'58d55abd3c0a7d1392e2c24d',
				u'unconfirmed': False
			}],
		u'url': u'https://trello.com/b/EZnarVuK/tech-issues',
		u'starred': False
	}
]

# MILESTONES BOARDS LIST
mock_milestones_lists = [{
	u'idBoard': u'58aabccb312e1c62277e84c5',
	u'subscribed': False,
	u'pos': 65535,
	u'closed': False,
	u'id': u'58aabce1f1fb7c88113ac5ec',
	u'name': u'Product Backlog'
}, {
	u'idBoard': u'58aabccb312e1c62277e84c5',
	u'subscribed': False,
	u'pos': 131071,
	u'closed': False,
	u'id': u'58aabce8b29848508bba7d12',
	u'name': u'Sprint Backlog'
}, {
	u'idBoard': u'58aabccb312e1c62277e84c5',
	u'subscribed': False,
	u'pos': 196607,
	u'closed': False,
	u'id': u'58aabcf0c0b8effa11a3919f',
	u'name': u'Staging'
}, {
	u'idBoard': u'58aabccb312e1c62277e84c5',
	u'subscribed': False,
	u'pos': 262143,
	u'closed': False,
	u'id': u'58aabcf193ef66eb551c3039',
	u'name': u'Prod'
}]

# MILESTONES BOARDS CARDS
mock_milestones_cards = [
	{
		u'labels': [],
		u'pos': 8192,
		u'manualCoverAttachment': False,
		u'id': u'58aabd2091dfdc112e51948a',
		u'badges': {
			u'votes': 0,
			u'attachments': 0,
			u'subscribed': False,
			u'due': u'2017-01-02T08:00:00.000Z',
			u'comments': 0,
			u'dueComplete': False,
			u'checkItemsChecked': 0,
			u'fogbugz': u'',
			u'viewingMemberVoted': False,
			u'checkItems': 0,
			u'description': True
		},
		u'idBoard': u'58aabccb312e1c62277e84c5',
		u'idShort': 1,
		u'due': u'2017-01-02T08:00:00.000Z',
		u'dueComplete': False,
		u'shortUrl': u'https://trello.com/c/asdf3',
		u'closed': False,
		u'subscribed': False,
		u'dateLastActivity': u'2017-02-27T11:52:43.246Z',
		u'idList': u'58aabce8b29848508bba7d12',
		u'idMembersVoted': [],
		u'idLabels': [],
		u'idMembers': [],
		u'checkItemStates': None,
		u'desc': u'Lorem Ipsum Description of Miletone',
		u'descData': {
			u'emoji': {}
		},
		u'name': u'Milestone SuperName 1',
		u'shortLink': u'asdf3',
		u'idAttachmentCover': None,
		u'url': u'https://trello.com/c/9bv5i6C8/milestone_supername',
		u'idChecklists': []
	},
	{
		u'labels': [],
		u'pos': 16384,
		u'manualCoverAttachment': False,
		u'id': u'58aaf0e7ef466eef16168993',
		u'badges': {
			u'votes': 0,
			u'attachments': 0,
			u'subscribed': False,
			u'due': None,
			u'comments': 0,
			u'dueComplete': False,
			u'checkItemsChecked': 0,
			u'fogbugz': u'',
			u'viewingMemberVoted': False,
			u'checkItems': 0,
			u'description': False
		},
		u'idBoard': u'58aabccb312e1c62277e84c5',
		u'idShort': 6,
		u'due': None,
		u'dueComplete': False,
		u'shortUrl': u'https://trello.com/c/asdf4',
		u'closed': False,
		u'subscribed': False,
		u'dateLastActivity': u'2017-02-27T11:52:44.169Z',
		u'idList': u'58aabce8b29848508bba7d12',
		u'idMembersVoted': [],
		u'idLabels': [],
		u'idMembers': [],
		u'checkItemStates': None,
		u'desc': u'',
		u'descData': {
			u'emoji': {}
		},
		u'name': u'Milestone SuperName 2',
		u'shortLink': u'asdf4',
		u'idAttachmentCover': None,
		u'url': u'https://trello.com/c/7ejf7BGu/milestone_supername_2',
		u'idChecklists': []
	},
	{
		u'labels': [],
		u'pos': 32768,
		u'manualCoverAttachment': False,
		u'id': u'58aaf1fc5120f5c165383024',
		u'badges': {
			u'votes': 0,
			u'attachments': 0,
			u'subscribed': False,
			u'due': None,
			u'comments': 0,
			u'dueComplete': False,
			u'checkItemsChecked': 0,
			u'fogbugz': u'',
			u'viewingMemberVoted': False,
			u'checkItems': 0,
			u'description': False
		},
		u'idBoard': u'58aabccb312e1c62277e84c5',
		u'idShort': 7,
		u'due': None,
		u'dueComplete': False,
		u'shortUrl': u'https://trello.com/c/asdf5',
		u'closed': False,
		u'subscribed': False,
		u'dateLastActivity': u'2017-02-27T11:52:45.173Z',
		u'idList': u'58aabce8b29848508bba7d12',
		u'idMembersVoted': [],
		u'idLabels': [],
		u'idMembers': [],
		u'checkItemStates': None,
		u'desc': u'',
		u'descData': {
			u'emoji': {}
		},
		u'name': u'Internationalisation / Translation',
		u'shortLink': u'asdf5',
		u'idAttachmentCover': None,
		u'url': u'https://trello.com/c/BDUpARGQ/7-internationalisation-translation',
		u'idChecklists': []
	},
	{
		u'labels': [],
		u'pos': 49152,
		u'manualCoverAttachment': False,
		u'id': u'58aaf1fed62e1f08170d0f38',
		u'badges': {
			u'votes': 0,
			u'attachments': 0,
			u'subscribed': False,
			u'due': None,
			u'comments': 0,
			u'dueComplete': False,
			u'checkItemsChecked': 0,
			u'fogbugz': u'',
			u'viewingMemberVoted': False,
			u'checkItems': 0,
			u'description': True
		},
		u'idBoard': u'58aabccb312e1c62277e84c5',
		u'idShort': 8,
		u'due': None,
		u'dueComplete': False,
		u'shortUrl': u'https://trello.com/c/asdf6',
		u'closed': False,
		u'subscribed': False,
		u'dateLastActivity': u'2017-02-27T11:52:46.258Z',
		u'idList': u'58aabce8b29848508bba7d12',
		u'idMembersVoted': [],
		u'idLabels': [],
		u'idMembers': [],
		u'checkItemStates': None,
		u'desc': u'Milestone Description',
		u'descData': {
			u'emoji': {}
		},
		u'name': u'Milestone other super name',
		u'shortLink': u'asdf6',
		u'idAttachmentCover': None,
		u'url': u'https://trello.com/c/ZI7GobVm/milestone-other',
		u'idChecklists': []
	},
]
mock_milestones_checklists = []

# SINGLE ISSUES BOARD LISTS
mock_single_issues_lists = [{
	u'idBoard': u'58ac046faad15d151e3b3623',
	u'subscribed': False,
	u'pos': 65535,
	u'closed': False,
	u'id': u'58ac04781e639a7d23efd0c1',
	u'name': u'TODO'
}, {
	u'idBoard': u'58ac046faad15d151e3b3623',
	u'subscribed': False,
	u'pos': 131071,
	u'closed': False,
	u'id': u'58ac047b0d0f9408271189e0',
	u'name': u'DOING'
}, {
	u'idBoard': u'58ac046faad15d151e3b3623',
	u'subscribed': False,
	u'pos': 196607,
	u'closed': False,
	u'id': u'58ac047c1e1339a310d5db36',
	u'name': u'DONE'
}]
# SINGLE ISSUES BOARD CARDS
mock_single_issues_cards = [{
	u'labels': [{
		u'color': u'red',
		u'uses': 1,
		u'id': u'58d55aceced82109ffe3b9f4',
		u'idBoard': u'58ac046faad15d151e3b3623',
		u'name': u'Prioritary'
	}],
	u'pos': 16384,
	u'manualCoverAttachment': False,
	u'id': u'58b41ef642bf7e0e10695b17',
	u'badges': {
		u'votes': 0,
		u'attachments': 0,
		u'subscribed': False,
		u'due': None,
		u'comments': 0,
		u'dueComplete': False,
		u'checkItemsChecked': 0,
		u'fogbugz': u'',
		u'viewingMemberVoted': False,
		u'checkItems': 0,
		u'description': False
	},
	u'idBoard': u'58ac046faad15d151e3b3623',
	u'idShort': 1,
	u'due': None,
	u'dueComplete': False,
	u'shortUrl': u'https://trello.com/c/asdf7',
	u'closed': False,
	u'subscribed': False,
	u'dateLastActivity': u'2017-03-24T17:43:46.530Z',
	u'idList': u'58ac04781e639a7d23efd0c1',
	u'idMembersVoted': [],
	u'idLabels': [u'58d55aceced82109ffe3b9f4'],
	u'idMembers': [],
	u'checkItemStates': None,
	u'desc': u'',
	u'descData': None,
	u'name': u'Issue Super Name 1',
	u'shortLink': u'asdf7',
	u'idAttachmentCover': None,
	u'url': u'https://trello.com/c/5ifyPIwe/issue-super-name-1',
	u'idChecklists': []
}, {
	u'labels': [],
	u'pos': 32768,
	u'manualCoverAttachment': False,
	u'id': u'58b41f83c9d333427bc6ca9a',
	u'badges': {
		u'votes': 0,
		u'attachments': 0,
		u'subscribed': False,
		u'due': None,
		u'comments': 0,
		u'dueComplete': False,
		u'checkItemsChecked': 0,
		u'fogbugz': u'',
		u'viewingMemberVoted': False,
		u'checkItems': 0,
		u'description': False
	},
	u'idBoard': u'58ac046faad15d151e3b3623',
	u'idShort': 2,
	u'due': None,
	u'dueComplete': False,
	u'shortUrl': u'https://trello.com/c/asdf8',
	u'closed': False,
	u'subscribed': False,
	u'dateLastActivity': u'2017-02-27T12:45:55.047Z',
	u'idList': u'58ac04781e639a7d23efd0c1',
	u'idMembersVoted': [],
	u'idLabels': [],
	u'idMembers': [],
	u'checkItemStates': None,
	u'desc': u'',
	u'descData': None,
	u'name': u'Issue Super Name 2',
	u'shortLink': u'asdf8',
	u'idAttachmentCover': None,
	u'url': u'https://trello.com/c/MUNI0jrQ/issue-super-name-2',
	u'idChecklists': []
}, {
	u'labels': [],
	u'pos': 49152,
	u'manualCoverAttachment': False,
	u'id': u'58b41f85c746f4526610eba5',
	u'badges': {
		u'votes': 0,
		u'attachments': 0,
		u'subscribed': False,
		u'due': None,
		u'comments': 0,
		u'dueComplete': False,
		u'checkItemsChecked': 0,
		u'fogbugz': u'',
		u'viewingMemberVoted': False,
		u'checkItems': 0,
		u'description': False
	},
	u'idBoard': u'58ac046faad15d151e3b3623',
	u'idShort': 3,
	u'due': None,
	u'dueComplete': False,
	u'shortUrl': u'https://trello.com/c/asdf9',
	u'closed': False,
	u'subscribed': False,
	u'dateLastActivity': u'2017-02-27T12:45:57.432Z',
	u'idList': u'58ac04781e639a7d23efd0c1',
	u'idMembersVoted': [],
	u'idLabels': [],
	u'idMembers': [],
	u'checkItemStates': None,
	u'desc': u'',
	u'descData': None,
	u'name': u'Issue Super Name 3',
	u'shortLink': u'asdf9',
	u'idAttachmentCover': None,
	u'url': u'https://trello.com/c/NH4j6yC3/issue-super-name-3',
	u'idChecklists': []
}, {
	u'labels': [],
	u'pos': 65536,
	u'manualCoverAttachment': False,
	u'id': u'58b41f8a1434c7c8262303d5',
	u'badges': {
		u'votes': 0,
		u'attachments': 0,
		u'subscribed': False,
		u'due': None,
		u'comments': 0,
		u'dueComplete': False,
		u'checkItemsChecked': 0,
		u'fogbugz': u'',
		u'viewingMemberVoted': False,
		u'checkItems': 0,
		u'description': False
	},
	u'idBoard': u'58ac046faad15d151e3b3623',
	u'idShort': 6,
	u'due': None,
	u'dueComplete': False,
	u'shortUrl': u'https://trello.com/c/asdf10',
	u'closed': False,
	u'subscribed': False,
	u'dateLastActivity': u'2017-02-27T12:46:02.987Z',
	u'idList': u'58ac04781e639a7d23efd0c1',
	u'idMembersVoted': [],
	u'idLabels': [],
	u'idMembers': [],
	u'checkItemStates': None,
	u'desc': u'',
	u'descData': None,
	u'name': u'Issue Super Name 4',
	u'shortLink': u'asdf10',
	u'idAttachmentCover': None,
	u'url': u'https://trello.com/c/oi1FALNJ/issue-super-name-4',
	u'idChecklists': []
}, {
	u'labels': [],
	u'pos': 81920,
	u'manualCoverAttachment': False,
	u'id': u'58b41f8c6337c0691690815d',
	u'badges': {
		u'votes': 0,
		u'attachments': 0,
		u'subscribed': False,
		u'due': None,
		u'comments': 0,
		u'dueComplete': False,
		u'checkItemsChecked': 0,
		u'fogbugz': u'',
		u'viewingMemberVoted': False,
		u'checkItems': 0,
		u'description': False
	},
	u'idBoard': u'58ac046faad15d151e3b3623',
	u'idShort': 7,
	u'due': None,
	u'dueComplete': False,
	u'shortUrl': u'https://trello.com/c/asdf11',
	u'closed': False,
	u'subscribed': False,
	u'dateLastActivity': u'2017-02-27T12:46:04.777Z',
	u'idList': u'58ac04781e639a7d23efd0c1',
	u'idMembersVoted': [],
	u'idLabels': [],
	u'idMembers': [],
	u'checkItemStates': None,
	u'desc': u'',
	u'descData': None,
	u'name': u'Issue SuperName 5',
	u'shortLink': u'asdf11',
	u'idAttachmentCover': None,
	u'url': u'https://trello.com/c/G897RgYI/issue-super-name-5',
	u'idChecklists': []
}, {
	u'labels': [],
	u'pos': 98304,
	u'manualCoverAttachment': False,
	u'id': u'58b41f8f59282e5301f9bddd',
	u'badges': {
		u'votes': 0,
		u'attachments': 0,
		u'subscribed': False,
		u'due': None,
		u'comments': 0,
		u'dueComplete': False,
		u'checkItemsChecked': 0,
		u'fogbugz': u'',
		u'viewingMemberVoted': False,
		u'checkItems': 0,
		u'description': False
	},
	u'idBoard': u'58ac046faad15d151e3b3623',
	u'idShort': 9,
	u'due': None,
	u'dueComplete': False,
	u'shortUrl': u'https://trello.com/c/asdf12',
	u'closed': False,
	u'subscribed': False,
	u'dateLastActivity': u'2017-02-27T12:46:07.335Z',
	u'idList': u'58ac04781e639a7d23efd0c1',
	u'idMembersVoted': [],
	u'idLabels': [],
	u'idMembers': [],
	u'checkItemStates': None,
	u'desc': u'',
	u'descData': None,
	u'name': u'Issue SuperName 6',
	u'shortLink': u'asdf12',
	u'idAttachmentCover': None,
	u'url': u'https://trello.com/c/sp4uWmNY/issue-super-name-6',
	u'idChecklists': []
}
]
# SINGLE ISSUES BOARD CHECKLISTS
mock_single_issues_checklists = []


def get_mock_list(id):
	if id == u'58ac046faad15d151e3b3623':
		return mock_single_issues_lists
	elif id == u'58aabccb312e1c62277e84c5':
		return mock_milestones_lists


def get_mock_checklist(id):
	if id == u'58ac046faad15d151e3b3623':
		return mock_single_issues_checklists
	elif id == u'58aabccb312e1c62277e84c5':
		return mock_milestones_checklists


def get_mock_cards(filter, id):
	if id == u'58ac046faad15d151e3b3623':
		return mock_single_issues_cards
	elif id == u'58aabccb312e1c62277e84c5':
		return mock_milestones_cards


mock_trello_api = Mock(
	members=Mock(
		get_board=Mock(return_value=mock_boards)
	),
	boards=Mock(
		get_list=get_mock_list,
		get_card_filter=get_mock_cards,
		get_checklist=get_mock_checklist,
	),
	cards=Mock(
		new=Mock(return_value=mock_milestones_cards[0])
	)
)
