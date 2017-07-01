#!/usr/bin/env python
from __future__ import print_function

import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from process_query import Fetch
import json
from datetime import datetime
import time
import re


# --------------- Helpers that build all of the responses ----------------------

# this function filters the text and makes it acceptable by the SSML.
def SSML_filter(text):
    # replace the key in the text with the value
    replacement = {"&": "and", "\n": "", "[ ]+": " "}

    for key, value in replacement.items():
        text = re.sub(key, value, text)

    return text


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def help_response():
    session_attributes = {}
    card_title = "Help"
    speech_output = '''
                    Hi, I am CodeGeek. I will be assisting you to know the latest 
                    online competitions such as, hackathons or coding competitions going over 
                    different online platform.
                    You can ask me to get ongoing, upcoming competitions.
                    You can ask me the count of competitions like two upcoming or three upcoming.
                    You can also specify the type like hackathon or coding.
                    To start please say, "get two upcoming coding competitions".
                    '''
    reprompt_text = ""
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def invalid_response():
    session_attributes = {}
    card_title = "Invalid Response"
    speech_output = '''
                    Sorry but I didn't understand what you meant.
                    Please say "help" if you are facing problem.
                    '''

    reprompt_text = '''
                     Please tell me what information you want on coding competitions, like
                    "get recent competitions" or
                    "fetch two recent competitions" or
                    "retrieve future hackathon competitions" or
                    "fetch onging coding contest"
                    '''
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = '''
                    Welcome to the CodeGeek. Please say, "get two upcoming coding competitions",
                    to know the latest upcoming coding contests. Else, for more information please say "help"
                    '''

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = '''
                    Please tell me what information you want on coding competitions, like
                    "get recent competitions" or
                    "fetch two recent competitions" or
                    "retrieve future hackathon competitions" or
                    "fetch onging coding contest"
                    '''
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the CodeGeek. " \
                    "Have a nice day!"

    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def get_competitions(intent, current_time):
    ''' Called when GetCompetition intent is called '''

    epoch = datetime.utcfromtimestamp(0)
    current_time = datetime.strptime(current_time, "%Y-%m-%dT%H:%M:%SZ")
    current_time -= epoch
    current_time = int(current_time.total_seconds())
    x = {'count': 1, 'status': 'recent', 'type': 'all', 'DEPLOY': True, 'now': current_time}

    if 'value' in intent['slots']['fetch']:
        if intent['slots']['fetch']['value'] not in ['load', 'get', 'fetch', 'retrieve']:
            return invalid_response()

    if 'value' in intent['slots']['count']:
        x['count'] = int(intent['slots']['count']['value'])
        if x['count'] not in [1, 2, 3]:
            return invalid_response()

    if 'value' in intent['slots']['type']:
        x['type'] = intent['slots']['type']['value']
        if x['type'] not in ['all', 'hackathon', 'coding', 'algorithmic', 'competitive programming']:
            return invalid_response()

    if 'value' in intent['slots']['status']:
        x['status'] = intent['slots']['status']['value']
        if x['status'] not in ['future', 'upcoming', 'ongoing', 'recent', 'latest']:
            return invalid_response()

    response = Fetch(**x)

    # reply structures
    # TODO add more structures in future.
    reply = ["%s will start at %s, in %s.com .", "%s has started since %s, and will end at %s, in %s.com ."]

    session_attributes = {}
    card_title = x['type'] + " contest"

    speech_output = ""
    if x['status'] == 'ongoing':
        for i in response:
            start_time = time.strftime('%d-%h ,%I:%M %p', time.gmtime(i["start_time"]))
            end_time = time.strftime('%d-%h ,%I:%M %p', time.gmtime(i["end_time"]))

            # reference process_query.json
            speech_output += SSML_filter(reply[1] % (i["competiton_name"]  # competiton_name
                                                     , start_time
                                                     , end_time
                                                     , i['site_name']  # site_name
                                                     ))

    else:
        for i in response:
            start_time = time.strftime('%d-%h ,%I:%M %p', time.gmtime(i["start_time"]))

            # reference process_query.json
            speech_output += SSML_filter(reply[0] % (i["competiton_name"]  # competiton_name
                                                     , start_time
                                                     , i['site_name']  # site_name
                                                     ))

    reprompt_text = "I know I speak too fast, but you can follow me if you lower down your query count."

    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

    pass


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "AMAZON.HelpIntent":
        return help_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    elif intent_name == "GetCompetitions":
        return get_competitions(intent, intent_request['timestamp'])
    else:
        return invalid_response()


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def testing_lambda():
    x = ""
    with open(CURRENT_DIR + '/testing/input1.json', 'r') as f:
        x = json.loads(f.read())
        pass
    print(lambda_handler(x, " "))
    pass

    # comment it out while transfering to the LAMBDA
    # testing_lambda()
