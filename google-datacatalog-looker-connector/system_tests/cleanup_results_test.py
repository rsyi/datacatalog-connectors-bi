#!/usr/bin/python
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import unittest

from google.cloud import datacatalog
from google.cloud.datacatalog import types

datacatalog = datacatalog.DataCatalogClient()


class CleanupResultsTest(unittest.TestCase):

    def test_looker_entries_should_not_exist_after_cleanup(self):
        query = 'system=looker'

        scope = types.SearchCatalogRequest.Scope()
        scope.include_project_ids.append(
            os.environ['LOOKER2DC_DATACATALOG_PROJECT_ID'])

        search_results = [
            result for result in datacatalog.search_catalog(
                scope=scope, query=query, order_by='relevance', page_size=1000)
        ]
        self.assertEqual(len(search_results), 0)
