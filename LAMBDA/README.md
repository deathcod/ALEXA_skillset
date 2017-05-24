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