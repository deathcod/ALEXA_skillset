# INSTALLATION

### setup online

first setup the EC2(go through the EC2 README) and then follow up the lambda function.

Having completed the setting up the IAM user, and adding the role for lambda, lets move ahead.

* Go to the service--> lambda --> create a Lambda function
* Select runtime python 3.6
* Select the black blueprint -->next
* On the configure trigger click Alexa Skills Kit -->next
* type the name of the function (suppose demo_function)
* Change the runtime to python 3.6 if change accidently 
* Go to Lambda function handler and role:
	- Role: choose an existing role.
	- Existing role: Choose the role you set up in the IAM user.
	- Advanced : can change the time out to 3 sec.(Optional)
	- -->next --> Check --> Create Function

### setup offline

**setup git with storing the credentials**

```
$ git config credential.helper store
$ git push http://example.com/repo.git
Username: <type your username>
Password: <type your password>
```  
Change the origin master to the branch name if you are creating a new branch  


**for working offline.**

* a testing folder is kept where possible input jsons are stored. Do keep all the jsons there

* DEPLOY = False, by changing the DEPLOY keyword it is set up for the local machine, local database is used and also it prints all the json inserted or fetched from the database. It will show the work flow and all the data circulation.

* index.py
It has a testing_lambda() function this function is used to test the lambda handler with the input json from the testing folder.  

**seting up the publish.sh**  
now open publish.sh and change the function-name to demo_function also change the region of which you are using the service.

# PROBLEM FACED

**1) So this was the first problem I faced, what should be the code structure such that I can differentiate the code in the lambda from the query. such that all the query be in the database section. Basically maintaining the integrity of the space, and place the code that should be.**  

* I am thinking of JSON. Let me thinking of more clean solution if possible  
* After careful thinking and referencing from my previous work I conclude that I will write the query in the preocess query and forward it to the the database for running the the query. So I will write the filterexpresion in the process query itself.


**2) This was a new problem which helped to rectify my concept on how Dynamodb works. So earlier I was storing the partition key as the "competition_name" and the sort key as "start_time", and to retrieve the values from the table I was scanning the table over the start_date, BUT this didnt promise the data to be sorted. Now after careful reading through all the functionality of the scan and query I came to realise my setup was wrong, now I am making the partition key as "classification" and the sort key as "start_time" , this is more efficient for now, lets see if I have to change in future.**

**3) Error when passing the speech_output to ALEXA**

```Error: Unable to parse the provided SSML. The provided text is not valid SSML.```

So this was a basic error, and helped me to learn new stuff. So from this error I came to know about SSML(Speech Synthesis Markup Language).


___

## THINGS TO REMEMBER

ALEXA SSML DOC  
https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/speech-synthesis-markup-language-ssml-reference
