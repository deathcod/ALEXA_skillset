## Testing  
  
Fixtures are set of objects that are the base line for testing.  
  
## Problems faced  
  
1) When I was trying to import files from other directories the import was not working than after searching I got to understand the concept of sys path. below is the code which is simple and serves the purpose.  
  
```python3  
import os, sys  
  
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))  
sys.path.append(os.path.dirname(CURRENT_DIR))  
```  
  
2) I am very new to software testing so it is very difficult to get to know how to test the database.  
  
3) I faced error that said it cannnot find module etree of lxml. On search on stackoverflow I came to the conclusion that to run lxml I had to download some dependencies, but the problem is in the local system it is managable but how to manage in the aws lambda that was difficult.   
  
So to rectify I included LD_LIBRARY_PATH and set the path of the the library with lib file required by lxml.  But still it was showing errors of permisision denied so I used chmod 755 to give excutable access to the files and now it was working fine. But there was still a problem though everything was working fine in the local system it was not executing the in the lambda funciton as to do so the virtual environment was needed to be activated, but the problem how to do that and thus it was difficult to proceed ahead,  
  
So then I realised that the problem is the setup. So I am building a serverless model when it should not be like instead it should be a complete server model so now I have shifted my project to EC2 and triggering the dynamodb and set the cron job for automation. And create the serverless model for the lambda function ALEXA is calling.  
  
4) was facing problem to create xpaths when we require to select two div positions, came to realise it can be done by div[position=3 or position=4]  
  
  
  
## Why to use shebang #!/usr/bin/env python  
  
See this is different, env is to point to a virtual environment.   
A reason not to use /usr/bin/env is that then the name of the process is not the name of the script. Having the script name as the process name is helpful in looking at process listings and when it is behaving badly and you need to kill it.  
  
  
## use of requirements.txt  
  
To build the requirements.txt you have use the following commmand. ``` pip freeze > requirements.txt``` This helps to keep in track of all the packages installed.  
  
## installation  
  
### Below is the guidelines to setup IAM user   
http://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html   
https://www.youtube.com/watch?v=Z4U5ymvEvKc   
  
  
(This procedure is to make a role for EC2)  
Now create new role  
roles --> Create new role --> Amazon EC2 -->select  
Attack policy --> AmazonEC2FullAccess, AmazonDynamoDBFullAccess  
select role name and save  
  
  
(This procedure is to make a role for Lambda)  
roles --> Create new role --> Amazon Lambda -->select  
Attack policy --> AmazonLambdaFullAccess  
select role name and save  
  
  
(This procedure is to make a role for DynamoDB)  
roles --> Create new role --> Amazon Config -->select  
Attack policy --> AWSLambdaDynamoDBExecutionRole  
select role name and save  
  
  
### Below is the guidelines about how to setup the EC2.  
setup EC2 instance  
https://www.youtube.com/watch?v=M2Wc8JIS-p8  
  
for the role use the role we created at the time of building IAM user  
  
IAM commandLine  
http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html  
http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html  
  
to download java  
http://stackoverflow.com/questions/14788345/how-to-install-jdk-on-ubuntu-linux  
  
get the dynamodb file for your local drive for local testing  
To start dynamodb use : java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar   
  
set up virtual environment : virtualenv --python=/usr/bin/python3 myenv  
upgrade pip : pip install --upgrade   
install all the requirements : pip install -r requirements.txt  
  
connect to EC2  
step 1)  
```aws ec2 get-console-output --instance-id instance_id```  
  
step 2)  
```chmod 400 <full path of the pem key>___.pem```  
  
step 3)  
```ssh -i <full path of the pem key>___.pem ec2-user@<aws ec2 instance public DNS>```  
  
  
To access your instance:  
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html  
  
  
Or else which I did, use Filezilla since it is a server model it can be worked with FTP client  
  
For downloading filezilla  
http://sourceforge.net/projects/filezilla/files/FileZilla_Client/3.25.2/FileZilla_3.25.2_x86_64-linux-gnu.tar.bz2/download  
  
To execute:  
  
extract --> bin/filezilla -->run  
  
If your filezilla is not executing.  
```  
sudo add-apt-repository ppa:ubuntu-toolchain-r/test   
sudo apt-get update  
sudo apt-get upgrade  
sudo apt-get dist-upgrade
```  
  
managing ec2 inside filezilla  
http://stackoverflow.com/questions/16744863/connect-to-amazon-ec2-file-directory-using-filezilla-and-sftp  
  
Having setup your filezilla upload all the files inside EC2  
1)making a directory under ec2-user in ec2 instance and upload the EC2 folder  
2)upload the requirements.txt inside this folder in ec2  
  
now come back to command line:(I hope aws cli is configured, credentials are set, ec2 is running in command line as well in filezilla)   
```  
cd EC2  
which python  							#returns the current version of the python  
sudo yum install python34 				#install python3.4 inside ec2  
virtualenv -p python3.4 myenv			#make a virtual environment  
source myenv/bin/activated				#activate the virtual environment  
pip install upgrade pip  
pip install -r requirement.txt 			#install the requirements  
pwd										#to get the path of the current working directory  
```  
  
having done all the requirement installed now lets set the cron job  
  
```  
crontab -l 								#to check if any cronjob is set or not  
nano task.cron 							# this step is optional if you see the path is different then set the path accordingly and update the task.cron  
crontab task.cron 						#add task to cron  
crontab -l 								#you can see the task is added to cron  
```  
  
At last set whenever ec2 loads the virtual environment also loads  
```  
echo "source /home/ec2-user/EC2/myenv/bin/activate" >> /home/ec2-user/.bashrc  
```