import unittest
import HtmlTestRunner

from commonUtils.comUtils import commonUtilities
from commonUtils.Constants import Constants

from Selenium_code.TC01_AddLocation import TC01_AddLocation
from Selenium_code.TC02_DeleteLocation import TC02_DeleteLocation
from Selenium_code.TC03_HandleAlerts import TC03_HandleAlerts
from Selenium_code.TC04_DownloadUploadCases import TC04_DownloadUploadCases

tc1 = unittest.TestLoader().loadTestsFromModule(TC01_AddLocation)
tc2 = unittest.TestLoader().loadTestsFromModule(TC02_DeleteLocation)
tc3 = unittest.TestLoader().loadTestsFromModule(TC03_HandleAlerts)
tc4 = unittest.TestLoader().loadTestsFromModule(TC04_DownloadUploadCases)

smokeTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])
regressionTestSuite = unittest.TestSuite([tc3])
functionalTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])
integrationTestSuite = unittest.TestSuite([tc1, tc2, tc4])

cu = commonUtilities()
const = Constants()
properties = cu.readPropertyFile(const.propFilePath)
suiteName = properties['testSuite']
print("Suite Name:", suiteName)

if suiteName.lower() == "integration":
    unittest.TextTestRunner().run(integrationTestSuite)
elif suiteName.lower() == "smoke":
    unittest.TextTestRunner().run(smokeTestSuite)
elif suiteName.lower() == "functional":
    unittest.TextTestRunner().run(functionalTestSuite)
elif suiteName.lower() == "regression":
    unittest.TextTestRunner().run(regressionTestSuite)


# if suiteName.lower() == "smoke":
#     print("running smoke suite")
#     unittest.TextTestRunner().run(smokeTestSuite)
#     # test_runner.run(smokeTestSuite)

unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Reports/HTMLReports", verbosity=3, combine_reports=True))


