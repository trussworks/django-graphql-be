# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['test_all_cases 1'] = {
    'data': {
        'allCases': [{
            'analyst': None,
            'colorCode': 'GRAY',
            'id': '1',
            'receivedAt': '2021-12-10T23:13:13+00:00',
            'status': 'PRE_INQUIRY',
            'subject': {
                'firstName': 'Jason',
                'lastName': 'Ash'
            },
            'summary': 'Arrested for misdemeanor'
        }, {
            'analyst': {
                'firstName': 'Jonathan',
                'lastName': None
            },
            'colorCode': 'GRAY',
            'id': '2',
            'receivedAt': '2021-12-10T23:13:36+00:00',
            'status': 'PRE_INQUIRY',
            'subject': {
                'firstName': 'Riley',
                'lastName': 'Baker'
            },
            'summary': 'Suspicious behavior'
        }, {
            'analyst': None,
            'colorCode': 'BLUE',
            'id': '3',
            'receivedAt': '2021-12-10T23:14:47+00:00',
            'status': 'PRE_INQUIRY',
            'subject': {
                'firstName': 'Skyler',
                'lastName': 'Hunt'
            },
            'summary': 'Suspicious behavior'
        }, {
            'analyst': None,
            'colorCode': 'GRAY',
            'id': '4',
            'receivedAt': '2021-12-10T23:15:20+00:00',
            'status': 'IN_PROGRESS',
            'subject': {
                'firstName': 'Susan',
                'lastName': 'Lee'
            },
            'summary': None
        }, {
            'analyst': None,
            'colorCode': 'GRAY',
            'id': '5',
            'receivedAt': '2021-12-10T23:15:59+00:00',
            'status': 'IN_PROGRESS',
            'subject': {
                'firstName': 'Kerry',
                'lastName': 'Smith'
            },
            'summary': 'Harassment'
        }, {
            'analyst': {
                'firstName': 'Jonathan',
                'lastName': None
            },
            'colorCode': 'BLUE',
            'id': '6',
            'receivedAt': '2021-12-09T23:16:50+00:00',
            'status': 'ZERO_INACTIVE',
            'subject': {
                'firstName': 'Jessica',
                'lastName': 'Smith'
            },
            'summary': 'Unclassified email'
        }, {
            'analyst': {
                'firstName': 'Lisa',
                'lastName': None
            },
            'colorCode': 'PURPLE',
            'id': '7',
            'receivedAt': '2021-12-09T23:17:46+00:00',
            'status': 'ZERO_INACTIVE',
            'subject': {
                'firstName': 'Ted',
                'lastName': 'Smith'
            },
            'summary': 'Wrote passwords on sticky note on desk'
        }, {
            'analyst': {
                'firstName': 'Susan',
                'lastName': 'Lee'
            },
            'colorCode': 'GRAY',
            'id': '8',
            'receivedAt': '2021-12-09T23:18:47+00:00',
            'status': 'ZERO_INACTIVE',
            'subject': {
                'firstName': 'christopher',
                'lastName': 'swinglhurse-walters'
            },
            'summary': 'Suspicious behavior'
        }, {
            'analyst': {
                'firstName': 'Quinn',
                'lastName': None
            },
            'colorCode': 'BROWN',
            'id': '9',
            'receivedAt': '2021-12-08T23:19:36+00:00',
            'status': 'ZERO_INACTIVE',
            'subject': {
                'firstName': 'Susan',
                'lastName': 'Lee'
            },
            'summary': 'Mental health concern'
        }, {
            'analyst': {
                'firstName': 'Jo',
                'lastName': None
            },
            'colorCode': 'BROWN',
            'id': '10',
            'receivedAt': '2021-12-08T23:20:11+00:00',
            'status': 'ZERO_INACTIVE',
            'subject': {
                'firstName': 'Kerry',
                'lastName': 'Smith'
            },
            'summary': None
        }]
    }
}

snapshots['test_all_people 1'] = {
    'data': {
        'allPeople': [{
            'cases': [{
                'colorCode': 'GRAY',
                'receivedAt': '2021-12-10T23:13:13+00:00',
                'status': 'PRE_INQUIRY',
                'summary': 'Arrested for misdemeanor'
            }],
            'casesAssigned': [],
            'firstName':
            'Jason',
            'id':
            '1',
            'lastName':
            'Ash'
        }, {
            'cases': [{
                'colorCode': 'GRAY',
                'receivedAt': '2021-12-10T23:13:36+00:00',
                'status': 'PRE_INQUIRY',
                'summary': 'Suspicious behavior'
            }],
            'casesAssigned': [],
            'firstName':
            'Riley',
            'id':
            '2',
            'lastName':
            'Baker'
        }, {
            'cases': [],
            'casesAssigned': [{
                'colorCode': 'GRAY',
                'receivedAt': '2021-12-10T23:13:36+00:00',
                'status': 'PRE_INQUIRY',
                'summary': 'Suspicious behavior'
            }, {
                'colorCode': 'BLUE',
                'receivedAt': '2021-12-09T23:16:50+00:00',
                'status': 'ZERO_INACTIVE',
                'summary': 'Unclassified email'
            }],
            'firstName':
            'Jonathan',
            'id':
            '3',
            'lastName':
            None
        }, {
            'cases': [{
                'colorCode': 'BLUE',
                'receivedAt': '2021-12-10T23:14:47+00:00',
                'status': 'PRE_INQUIRY',
                'summary': 'Suspicious behavior'
            }],
            'casesAssigned': [],
            'firstName':
            'Skyler',
            'id':
            '4',
            'lastName':
            'Hunt'
        }, {
            'cases': [{
                'colorCode': 'GRAY',
                'receivedAt': '2021-12-10T23:15:20+00:00',
                'status': 'IN_PROGRESS',
                'summary': None
            }, {
                'colorCode': 'BROWN',
                'receivedAt': '2021-12-08T23:19:36+00:00',
                'status': 'ZERO_INACTIVE',
                'summary': 'Mental health concern'
            }],
            'casesAssigned': [{
                'colorCode': 'GRAY',
                'receivedAt': '2021-12-09T23:18:47+00:00',
                'status': 'ZERO_INACTIVE',
                'summary': 'Suspicious behavior'
            }],
            'firstName':
            'Susan',
            'id':
            '5',
            'lastName':
            'Lee'
        }, {
            'cases': [{
                'colorCode': 'GRAY',
                'receivedAt': '2021-12-10T23:15:59+00:00',
                'status': 'IN_PROGRESS',
                'summary': 'Harassment'
            }, {
                'colorCode': 'BROWN',
                'receivedAt': '2021-12-08T23:20:11+00:00',
                'status': 'ZERO_INACTIVE',
                'summary': None
            }],
            'casesAssigned': [],
            'firstName':
            'Kerry',
            'id':
            '6',
            'lastName':
            'Smith'
        }, {
            'cases': [{
                'colorCode': 'BLUE',
                'receivedAt': '2021-12-09T23:16:50+00:00',
                'status': 'ZERO_INACTIVE',
                'summary': 'Unclassified email'
            }],
            'casesAssigned': [],
            'firstName':
            'Jessica',
            'id':
            '7',
            'lastName':
            'Smith'
        }, {
            'cases': [{
                'colorCode': 'PURPLE',
                'receivedAt': '2021-12-09T23:17:46+00:00',
                'status': 'ZERO_INACTIVE',
                'summary': 'Wrote passwords on sticky note on desk'
            }],
            'casesAssigned': [],
            'firstName':
            'Ted',
            'id':
            '8',
            'lastName':
            'Smith'
        }, {
            'cases': [],
            'casesAssigned': [{
                'colorCode': 'PURPLE',
                'receivedAt': '2021-12-09T23:17:46+00:00',
                'status': 'ZERO_INACTIVE',
                'summary': 'Wrote passwords on sticky note on desk'
            }],
            'firstName':
            'Lisa',
            'id':
            '9',
            'lastName':
            None
        }, {
            'cases': [{
                'colorCode': 'GRAY',
                'receivedAt': '2021-12-09T23:18:47+00:00',
                'status': 'ZERO_INACTIVE',
                'summary': 'Suspicious behavior'
            }],
            'casesAssigned': [],
            'firstName':
            'christopher',
            'id':
            '10',
            'lastName':
            'swinglhurse-walters'
        }, {
            'cases': [],
            'casesAssigned': [{
                'colorCode': 'BROWN',
                'receivedAt': '2021-12-08T23:19:36+00:00',
                'status': 'ZERO_INACTIVE',
                'summary': 'Mental health concern'
            }],
            'firstName':
            'Quinn',
            'id':
            '12',
            'lastName':
            None
        }, {
            'cases': [],
            'casesAssigned': [{
                'colorCode': 'BROWN',
                'receivedAt': '2021-12-08T23:20:11+00:00',
                'status': 'ZERO_INACTIVE',
                'summary': None
            }],
            'firstName':
            'Jo',
            'id':
            '13',
            'lastName':
            None
        }]
    }
}
