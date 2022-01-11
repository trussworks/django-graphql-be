# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestGrapheneQueryMixinSQL.test_case_query_complex 1'] = '''SELECT "api_case"."id",
       "api_case"."subject_id",
       "api_case"."analyst_id",
       "api_case"."summary",
       "api_case"."color_code",
       "api_case"."status",
       "api_case"."received_at",
       "api_case"."created_at",
       "api_case"."updated_at",
       "api_person"."id",
       "api_person"."first_name",
       "api_person"."last_name",
       "api_person"."created_at",
       "api_person"."updated_at",
       T3."id",
       T3."first_name",
       T3."last_name",
       T3."created_at",
       T3."updated_at"
FROM "api_case"
INNER JOIN "api_person" ON ("api_case"."subject_id" = "api_person"."id")
LEFT OUTER JOIN "api_person" T3 ON ("api_case"."analyst_id" = T3."id")'''

snapshots['TestGrapheneQueryMixinSQL.test_case_query_simple 1'] = '''SELECT "api_case"."id",
       "api_case"."subject_id",
       "api_case"."analyst_id",
       "api_case"."summary",
       "api_case"."color_code",
       "api_case"."status",
       "api_case"."received_at",
       "api_case"."created_at",
       "api_case"."updated_at"
FROM "api_case"'''
