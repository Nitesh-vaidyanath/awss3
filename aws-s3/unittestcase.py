import unittest
import awss3info

class awsS3Test(unittest.TestCase):

      TestData49 = {
    "test": {
        "lastModifiedTimeStamp": "2018-04-17 21:58:18",
        "createdDate": "2018-04-17 21:57:27",
        "region": "ap-south-1",
        "fileCount": "1",
        "size": "53876069761023"
    }
   }

      TestData350 = {
    "test": {
        "lastModifiedTimeStamp": "2018-04-17 21:58:18",
        "createdDate": "2018-04-17 21:57:27",
        "region": "ap-south-1",
        "fileCount": "1",
        "size": "384829069721599"
    }
   }

      TestData600 = {
    "test": {
        "lastModifiedTimeStamp": "2018-04-17 21:58:18",
        "createdDate": "2018-04-17 21:57:27",
        "region": "ap-south-1",
        "fileCount": "1",
        "size": "659706976665598"
    }
   }


      def test_awscommands(self):
          mock  = awss3info.awscommands.awsCommands('echo "Hello World"')
          self.assertEquals(mock, b"Hello World\n")

      def test_pricecalculatori49(self):
          result = awss3info.priceCalulator.priceEstimation(self.TestData49)
          print result 
          self.assertAlmostEqual(result["test"]["EstimatedPrice"], 1254.40 )

      def test_pricecalculator350(self):
          result350 = awss3info.priceCalulator.priceEstimation(self.TestData350)
          print result350
          self.assertAlmostEqual(result350["test"]["EstimatedPrice"], 8652.80 )

      def test_pricecalculator600(self):
          result600 = awss3info.priceCalulator.priceEstimation(self.TestData600)
          print result600
          self.assertAlmostEqual(result600["test"]["EstimatedPrice"], 14694.40 )



if __name__ == "__main__":
    unittest.main()
          
 

       

