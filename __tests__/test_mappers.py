import unittest
from py_sls_lambda_toolkit.mappers import mapper


class TestMappers(unittest.TestCase):

    def test_mapper(self):
        data = {
            'name': 'John',
            'age': 30,
            'city': 'New York'
        }
        fields = ['age', 'city']
        expected = {'name': 'John'}
        result = mapper(data, fields)
        self.assertEqual(expected, result)

    def test_mapper_with_list(self):
        data = [
            {
                'name': 'John',
                'age': 30,
                'city': 'New York'
            },
            {
                'name': 'Jane',
                'age': 25,
                'city': 'Boston'
            }
        ]
        fields = ['age', 'city']
        expected = [
            {
                'name': 'John'
            },
            {
                'name': 'Jane'
            }
        ]
        result = mapper(data, fields)
        self.assertEqual(expected, result)

    def test_mapper_with_invalid_data(self):
        data = 'John'
        fields = ['age', 'city']
        with self.assertRaises(TypeError):
            mapper(data, fields)


if __name__ == '__main__':
    unittest.main()
