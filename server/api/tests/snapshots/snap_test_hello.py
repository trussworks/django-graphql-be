# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['HelloTestCase::test_hello 1'] = GenericRepr('<HttpResponse status_code=200, "application/json">')

snapshots['HelloTestCase::test_hello 2'] = {
    'data': {
        'hello': 'Hello World!'
    }
}
