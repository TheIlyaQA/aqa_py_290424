import unittest
import os
from db_module import create_database, create_table, insert_record, select_all_records, delete_record


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db_name = 'test.db'
        create_database(self.db_name)
        self.table_name = 'test_table'
        self.columns = {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT'}
        create_table(self.db_name, self.table_name, self.columns)

    def tearDown(self):
        if os.path.exists(self.db_name):
            os.remove(self.db_name)

    def test_insert_and_select(self):
        insert_record(self.db_name, self.table_name, (1, 'John'))
        records = select_all_records(self.db_name, self.table_name)
        self.assertEqual(records, [(1, 'John')])

    def test_delete(self):
        insert_record(self.db_name, self.table_name, (1, 'John'))
        delete_record(self.db_name, self.table_name, 'id=1')
        records = select_all_records(self.db_name, self.table_name)
        self.assertEqual(records, [])


if __name__ == '__main__':
    unittest.main()
