import unittest

class unittest_example(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("setUpClass method - runs before setup method of first test method")
        '''
        in setupClass as it runs only once per class first in order we can be have below tasks associated with it
        instantiating the driver, browser, any constant values (browser location)
        we can check if the browser/driver instance is not null. if null we will relaunch it         
        '''

    def setUp(self):
        print("setUp method - runs before every test method")
        '''
        we can setup prerequisite for unit test or scenario like:
        launch applicaiton page
        we can do login 
        '''

    def tearDown(self):
        print("tearDown method - runs after every test method")
        '''
        we can have below activities like:
        closing the window
        loging out
        check if logout is done correctly
        '''

    @classmethod
    def tearDownclass(self):
        print("setUpClass method - runs after tearDown method of last test method")
        '''
        since it is running in last posiiton we can add the cleanup activities here like:
        close browser
        close selenium sesison
        quit selenium
        '''

    def test_TC1(self):
        print("TC1 method - unit test method")

    def test_TC2(self):
        print("TC2 method - unit test method")

    def test_TC3(self):
        print("TC2 method - unit test method")

if __name__ == '__main__':
    unittest.main()

