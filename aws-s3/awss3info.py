import awscommands
import json 
import argparse
import sys
import datetime
import os
import priceCalulator
#parser = argparse.ArgumentParser(description='aws configure')
#subparsers = parser.add_subparsers(help='Options')
#configure = subparsers.add_parser('configure', help='Get details')
#parser.set_defaults(func=awscommands.awsCommands("aws configure"))
#args = parser.parse_args()


class S3bucket(object):
      def getS3Bucket(self):
             bucket = awscommands.awsCommands("aws s3 ls")
             bucket = filter(None,bucket.split("\n"))
             return bucket
      def getFiles(self,bucketList):
             bucketDict = {}
             for i in bucketList:
                  bucketName = i.split()
                  try: 
                     lastModified = awscommands.awsCommands('aws s3 ls s3://{} --recursive  | sort | tail -n 1'.format(bucketName[-1]))
                     lastModified = lastModified.split()
                     lastModifiedTimeStamp = lastModified[0] + " " + lastModified[1]
                  except Exception as e:
                     print "No objects/files in bucket {}".format(bucketName[-1])
                     pass
                  location = awscommands.awsCommands('aws s3api get-bucket-location --bucket {} --output json'.format(bucketName[-1]))
                  region = json.loads(location)
                  try:
                        bucketInfo = awscommands.awsCommands('aws s3api list-objects --bucket {} --output json --query "[sum(Contents[].Size), length(Contents[])] "'.format(bucketName[-1]))
                        bucketInfo = bucketInfo.replace("]", '').replace("[",'').replace('\n', '').split(",")
                        bucketDict.update({ bucketName[-1] : { "createdDate": bucketName[0] + " " + bucketName[1] , "size" : bucketInfo[0].strip(), "fileCount" : bucketInfo[1].strip() , "lastModifiedTimeStamp" : lastModifiedTimeStamp, "region": region["LocationConstraint"] }})
                  except Exception as e:
                        print "No objects/files in bucket {}".format(bucketName[-1])
                        bucketDict.update({ bucketName[-1] : { "createdDate": bucketName[0] , "size" : 0 , "fileCount" : 0, "region": region["LocationConstraint"] }})
                        pass
             return bucketDict
      
if __name__ == "__main__":
     bucketObj = S3bucket()
     bucketList =  bucketObj.getS3Bucket()
     bucketInfo  = bucketObj.getFiles(bucketList)
     price = priceCalulator.priceEstimation(bucketInfo)
     print json.dumps(price, indent = 4)



