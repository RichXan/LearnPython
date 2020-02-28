from city_functions import get_city_country
import unittest
class CityTestCase(unittest.TestCase):
    '''测试city_funtions.py'''
    def test_city_country(self):
        '''能否正确处理城市国家'''
        message = get_city_country("shenzhen","china")
        self.assertEqual(message,"shenzhen,china")
unittest.main()