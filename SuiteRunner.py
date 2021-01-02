import unittest
import HtmlTestRunner

from commonUtils.comUtils import commonUtilities

from Selenium_code.TC01_AddUser import TC01_AddUser
from Selenium_code.TC02_DeleteUser import TC02_DeleteUser
from Selenium_code.TC03_HandleAlerts import TC03_HandleAlerts
from Selenium_code.TC04_DownloadUploadCases import TC04_DownloadUploadCases

tc1 = unittest.TestLoader().loadTestsFromModule(TC01_AddUser)
tc2 = unittest.TestLoader().loadTestsFromModule(TC02_DeleteUser)
tc3 = unittest.TestLoader().loadTestsFromModule(TC03_HandleAlerts)
tc4 = unittest.TestLoader().loadTestsFromModule(TC04_DownloadUploadCases)

# Create test suites
smokeTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])
regressionTestSuite = unittest.TestSuite([tc1, tc4])
functionalTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])

cu = commonUtilities()
properties = cu.readPropertyFile("Selenium_code/config.properties")
suiteName = properties['testSuite']

# test_runner = HtmlTestRunner.HTMLTestRunner(output="Reports/HTMLReports", verbosity=2, report_name="SMOKE TEST REPORT", report_title=f"{suiteName} Test Report")

if suiteName.lower() == "smoke":
    print("running smoke suite")
    unittest.TextTestRunner().run(smokeTestSuite)
    # test_runner.run(smokeTestSuite)

unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Reports/HTMLReports", verbosity=3, combine_reports=True))


