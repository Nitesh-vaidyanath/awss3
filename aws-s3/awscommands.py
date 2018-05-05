import awscli
import subprocess

def awsCommands(cmd):
     try:
       output =  subprocess.check_output(cmd,shell=True, stderr=subprocess.STDOUT)
     except subprocess.CalledProcessError as e:
       if e.returncode > 0:
        print e.output
        raise 
     else: 
       return output
