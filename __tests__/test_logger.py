import unittest
from py_sls_lambda_toolkit.logger import logger

class TestLogger(unittest.TestCase):

    def test_logger(self,):
        logger.info('test logger')
        logger.error('test logger')
        logger.debug('test logger')
        logger.warning('test logger')
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
