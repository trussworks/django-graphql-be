# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['test_all_incidents 1'] = {
    'data': {
        'allIncidents': [{
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
            'firstName':
            'Jason',
            'id':
            '1',
            'incidents': [{
                'colorCode': 'GRAY',
                'receivedAt': '2021-12-10T23:13:13+00:00',
                'status': 'PRE_INQUIRY',
                'summary': 'Arrested for misdemeanor'
            }],
            'incidentsAssigned': [],
            'lastName':
            'Ash'
        }, {
            'firstName':
            'Riley',
            'id':
            '2',
            'incidents': [{
                'colorCode': 'GRAY',
                'receivedAt': '2021-12-10T23:13:36+00:00',
                'status': 'PRE_INQUIRY',
                'summary': 'Suspicious behavior'
            }],
            'incidentsAssigned': [],
            'lastName':
            'Baker'
        }, {
            'firstName':
            'Jonathan',
            'id':
            '3',
            'incidents': [],
            'incidentsAssigned': [{
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
            'lastName':
            None
        }, {
            'firstName':
            'Skyler',
            'id':
            '4',
            'incidents': [{
                'colorCode': 'BLUE',
                'receivedAt': '2021-12-10T23:14:47+00:00',
                'status': 'PRE_INQUIRY',
                'summary': 'Suspicious behavior'
            }],
            'incidentsAssigned': [],
            'lastName':
            'Hunt'
        }, {
            'firstName':
            'Susan',
            'id':
            '5',
            'incidents': [{
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
            'incidentsAssigned': [{
                'colorCode': 'GRAY',
                'receivedAt': '2021-12-09T23:18:47+00:00',
                'status': 'ZERO_INACTIVE',
                'summary': 'Suspicious behavior'
            }],
            'lastName':
            'Lee'
        }, {
            'firstName':
            'Kerry',
            'id':
            '6',
            'incidents': [{
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
            'incidentsAssigned': [],
            'lastName':
            'Smith'
        }, {
            'firstName':
            'Jessica',
            'id':
            '7',
            'incidents': [{
                'colorCode': 'BLUE',
                'receivedAt': '2021-12-09T23:16:50+00:00',
                'status': 'ZERO_INACTIVE',
                'summary': 'Unclassified email'
            }],
            'incidentsAssigned': [],
            'lastName':
            'Smith'
        }, {
            'firstName':
            'Ted',
            'id':
            '8',
            'incidents': [{
                'colorCode': 'PURPLE',
                'receivedAt': '2021-12-09T23:17:46+00:00',
                'status': 'ZERO_INACTIVE',
                'summary': 'Wrote passwords on sticky note on desk'
            }],
            'incidentsAssigned': [],
            'lastName':
            'Smith'
        }, {
            'firstName':
            'Lisa',
            'id':
            '9',
            'incidents': [],
            'incidentsAssigned': [{
                'colorCode': 'PURPLE',
                'receivedAt': '2021-12-09T23:17:46+00:00',
                'status': 'ZERO_INACTIVE',
                'summary': 'Wrote passwords on sticky note on desk'
            }],
            'lastName':
            None
        }, {
            'firstName':
            'christopher',
            'id':
            '10',
            'incidents': [{
                'colorCode': 'GRAY',
                'receivedAt': '2021-12-09T23:18:47+00:00',
                'status': 'ZERO_INACTIVE',
                'summary': 'Suspicious behavior'
            }],
            'incidentsAssigned': [],
            'lastName':
            'swinglhurse-walters'
        }, {
            'firstName':
            'Quinn',
            'id':
            '12',
            'incidents': [],
            'incidentsAssigned': [{
                'colorCode': 'BROWN',
                'receivedAt': '2021-12-08T23:19:36+00:00',
                'status': 'ZERO_INACTIVE',
                'summary': 'Mental health concern'
            }],
            'lastName':
            None
        }, {
            'firstName':
            'Jo',
            'id':
            '13',
            'incidents': [],
            'incidentsAssigned': [{
                'colorCode': 'BROWN',
                'receivedAt': '2021-12-08T23:20:11+00:00',
                'status': 'ZERO_INACTIVE',
                'summary': None
            }],
            'lastName':
            None
        }]
    }
}
