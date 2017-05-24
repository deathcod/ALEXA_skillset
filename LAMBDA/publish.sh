#!/bin/sh


rm xyz.zip

#getting the files which are necessary
zip -r xyz.zip index.py process_query.py

#invoking aws lambda function 
aws lambda update-function-code --region us-east-1 --function-name get_coding --zip-file fileb://xyz.zip

#invoking git the credentials are already saved.
git add --all
git commit -m "new change"
git push origin master