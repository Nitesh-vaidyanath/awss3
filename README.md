# awss3
AWS S3 storage analysis tool Beta version.

## Tool Output

Tool gives below information of a s3 bucket
1. Bucket name
2. Creation date of the bucket
3. Number of files
4. Total size of files
5. Last modified date (most recent file of a bucket)
6. Cost anayalsis (Only storage)
7. Region 

### Prerequisites

awscli 

### Installing

Clone repository:

git clone https://github.com/Nitesh-vaidyanath/awss3.git

Before running script please run "aws configure" 

OSX user can "source virtenv/bin/activate" and Linux user can use "source virtenv-linux/bin/activate" to activate virtual environment or use absoulte path of python while exectuing.  All the required modules have been installed in virtual environment.
  - awscli
  
Run:
  From the repository folder run "virtenv-linux/bin/python  awss3info.py"
```
  (virtenv-linux) ubuntu@ip-172-31-42-233:~/awss3/aws-s3$ virtenv-linux/bin/python  awss3info.py
{
    "<Name of the S3 bucket>": {
        "EstimatedPrice": 0.012221185223199427,
        "lastModifiedTimeStamp": "2017-07-27 22:57:16",
        "createdDate": "2017-07-25 20:20:26",
        "region": "us-west-2",
        "fileCount": "2577",
        "size": "570539031"
    }
}
```

## Running the tests
  
Unit Test Case:
```
  (virtenv-linux) ubuntu@ip-172-31-42-233:~/awss3/aws-s3$ python unittestcase.py
.{'test': {'EstimatedPrice': 8652.799999999977, 'lastModifiedTimeStamp': '2018-04-17 21:58:18', 'createdDate': '2018-04-17 21:57:27', 'region': 'ap-south-1', 'fileCount': '1', 'size': '384829069721599'}}
.{'test': {'EstimatedPrice': 14694.399999999958, 'lastModifiedTimeStamp': '2018-04-17 21:58:18', 'createdDate': '2018-04-17 21:57:27', 'region': 'ap-south-1', 'fileCount': '1', 'size': '659706976665598'}}
.{'test': {'EstimatedPrice': 1254.399999999977, 'lastModifiedTimeStamp': '2018-04-17 21:58:18', 'createdDate': '2018-04-17 21:57:27', 'region': 'ap-south-1', 'fileCount': '1', 'size': '53876069761023'}}
.
----------------------------------------------------------------------
Ran 4 tests in 0.002s

OK
```
 
