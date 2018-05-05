# awss3
AWS S3 storage analysis tool Beta version.

Tool gives below information of a bucket
1. Bucket name
2. Creation date of the bucket
3. Number of files
4. Total size of files
5. Last modified date (most recent file of a bucket)
6. Cost anayalsis (Only storage)
7. Region 


Clone repository:

git clone https://github.com/Nitesh-vaidyanath/awss3.git

Before running script please run "aws configure" 

Linux and OSX user can "source awss3/bin/activate" to activate virtual environment or use absoulte path of python while exectuing.  All the required modules have been installed in virtual environment.
  - awscli
  
Run:
  From the repository folder run "awss3/bin/python  awss3info.py"
  


 
