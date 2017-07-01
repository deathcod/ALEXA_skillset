#!/usr/bin/env python
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

if 'LD_LIBRARY_PATH' not in os.environ:
    try:
        os.environ['LD_LIBRARY_PATH'] = CURRENT_DIR + '/../LIB'
        os.execv(sys.argv[0], sys.argv)
    except:
        raise Exception("Failed execv")
        sys.exit(1)

import requests
import json
from lxml import html
from datetime import datetime


# this fucntion scraps the ongoing and future coding competitons
def codeforces(DEPLOY=False):
    x = ""
    output = []

    if DEPLOY:
        x = requests.get("http://codeforces.com/api/contest.list?gym=false").text
    else:
        with open(CURRENT_DIR + '/testing_sites/input_codeforces.json', 'r') as f:
            x = f.read()
            pass
        pass

    j = json.loads(x)
    for i in j["result"]:
        if i["phase"] == "BEFORE" or i["phase"] == "CODING":
            temp = {}
            temp["competiton_name"] = i["name"]
            temp["site_name"] = "codeforces"
            temp["start_time"] = i["startTimeSeconds"]
            temp["end_time"] = i["startTimeSeconds"] + i["durationSeconds"]
            temp["classification"] = "cp"
            temp["URL"] = " "
            output.append(temp)
            del temp
    del x, j
    return (output)
    pass


def codechef(DEPLOY=False):
    # TODO there is also UPCOMING Contest so do scrap it too.
    x = ""
    output = []
    if DEPLOY:
        x = requests.get("https://www.codechef.com/contests").text
    # open( CURRENT_DIR +'/testing_sites/input_codechef.html','w').write(x)
    else:
        with open(CURRENT_DIR + '/testing_sites/input_codechef.html', 'r') as f:
            x = f.read()
            pass
        pass

    tree = html.fromstring(x)

    competiton_name_list = tree.xpath(
        '//*[@id="primary-content"]/div/div[position()=3 or position()=4]/table/tbody/tr/td[2]/a')
    start_time_list = tree.xpath(
        '//*[@id="primary-content"]/div/div[position()=3 or position()=4]/table/tbody/tr/td[3]')
    end_time_list = tree.xpath('//*[@id="primary-content"]/div/div[position()=3 or position()=4]/table/tbody/tr/td[4]')
    URL_list = tree.xpath(
        '//*[@id="primary-content"]/div/div[position()=3 or position()=4]/table/tbody/tr/td[2]/a/@href')
    length = len(competiton_name_list)

    for i in range(length):
        temp = {}

        start_time = start_time_list[i].text_content()
        epoch = datetime.utcfromtimestamp(0)
        start_time = datetime.strptime(start_time, "%d %b %Y  %H:%M:%S")
        start_time -= epoch
        start_time = int(start_time.total_seconds())

        end_time = end_time_list[i].text_content()
        epoch = datetime.utcfromtimestamp(0)
        end_time = datetime.strptime(end_time, "%d %b %Y  %H:%M:%S")
        end_time -= epoch
        end_time = int(end_time.total_seconds())

        temp["competiton_name"] = competiton_name_list[i].text_content()
        temp["site_name"] = "codechef"
        temp["start_time"] = start_time
        temp["end_time"] = end_time
        temp["classification"] = "cp"
        temp["URL"] = "https://www.codechef.com" + URL_list[i]
        output.append(temp)
        del temp

    del x, tree, competiton_name_list, start_time_list, end_time_list, URL_list, length
    return output


# TODO currently this section is not working will have to review later
def hackerrank(DEPLOY=False):
    x = ""
    output = []
    if DEPLOY:
        x = requests.get("https://www.hackerrank.com/contests").text
    else:
        with open(CURRENT_DIR + '/testing_sites/input_hackerrank.html', 'r') as f:
            x = f.read()
            pass
        pass

    tree = html.fromstring(x)

    competiton_name_list = tree.xpath(
        '//*[@id="content"]/div/div/div/div[3]/div/div/div[1]/div/div[1]/ul/li/div[1]/div[1]/span')
    datetime_list = tree.xpath(
        '//*[@id="content"]/div/div/div/div[3]/div/div/div[1]/div/div[1]/ul/li/div[1]/div[2]/span/span//*[contains(@class, "timeago")]')
    URL_list = tree.xpath('//*[@id="content"]/div/div/div/div[3]/div/div/div[1]/div/div[1]/ul/li/div[1]/div[3]/a')

    print(tree.xpath(
        '//*[@id="content"]/div/div/div/div[3]/div/div/div[1]/div/div[1]/ul/li[2]/div[1]/div[2]/span/span/text()'))

    length = len(competiton_name_list)
    for i in range(length):
        temp = {}
        temp["competiton_name"] = competiton_name_list[i].text_content()
        temp["site_name"] = "hackerrank"
        temp["datetime"] = datetime_list[i].text_content()
        epoch = datetime.utcfromtimestamp(0)
        # temp["datetime"] = datetime.strptime(temp["datetime"], "%d %b %Y  %H:%M:%S")
        # temp["datetime"] -= epoch
        # temp["datetime"] = int(temp["datetime"].total_seconds())
        temp["classification"] = "cp"
        # temp["URL"] = "https://www.hackerrank.com/" + URL_list[i]
        output.append(temp)
        print(temp)
        del temp

    del x, tree, competiton_name_list, datetime_list, URL_list, length
    pass


def venturesity(DEPLOY=False):
    x = ""
    output = []
    if DEPLOY:
        x = requests.get("http://www.venturesity.com/challenge/").text
    else:
        with open(CURRENT_DIR + '/testing_sites/input_venturesity.html', 'r') as f:
            x = f.read()
            pass
        pass

    tree = html.fromstring(x)
    contest_name_list = tree.xpath('/html/body/section[2]/div/div[2]/div/div/div/div/div[1]/a/@title')  # contest name
    URL_list = tree.xpath('/html/body/section[2]/div/div[2]/div/div/div/div/div[1]/a/@href')  # href list
    register_list = tree.xpath('/html/body/section[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/a')  # register list

    length = len(contest_name_list)

    for i in range(length):
        if register_list[i].text_content() != "Closed":
            temp = {}
            url = "http://www.venturesity.com"
            temp_x = ""
            if DEPLOY:
                temp_x = requests.get(url + URL_list[i]).text
            # open(CURRENT_DIR +'/testing_sites/venturesity_subsites' + URL_list[i]+".html",'w').write(temp_x.encode('utf-8','ignore'))
            else:
                with open(CURRENT_DIR + '/testing_sites/venturesity_subsites' + URL_list[i] + ".html", 'r') as f:
                    temp_x = f.read()
                    pass
                pass

            temp_tree = html.fromstring(temp_x)
            start_time = temp_tree.xpath('/html/body/section[1]/div[1]/div/div/div/div/div[1]/span')[0].text_content()
            end_time = temp_tree.xpath('/html/body/section[1]/div[1]/div/div/div/div/div[2]/span')[0].text_content()
            start_time = start_time.strip()
            end_time = end_time.strip()

            epoch = datetime.utcfromtimestamp(0)
            start_time = datetime.strptime(start_time, "%d %b %Y - %H:%M %p")
            start_time -= epoch
            start_time = int(start_time.total_seconds())
            temp["start_time"] = start_time

            epoch = datetime.utcfromtimestamp(0)
            end_time = datetime.strptime(end_time, "%d %b %Y - %H:%M %p")
            end_time -= epoch
            end_time = int(end_time.total_seconds())
            temp["end_time"] = end_time

            temp["competiton_name"] = contest_name_list[i]
            temp["site_name"] = "Venturesity"
            temp["classification"] = "h"
            temp["URL"] = url + URL_list[i]
            output.append(temp)
            del temp, temp_tree, start_time, end_time, epoch, url, temp_x

    del tree, contest_name_list, URL_list, register_list, length
    return output
    pass


def analyticsvidhya(DEPLOY=False):
    x = ""
    output = []
    if DEPLOY:
        x = requests.get("https://datahack.analyticsvidhya.com/contest/all/").text
    else:
        with open(CURRENT_DIR + '/testing_sites/input_analyticsvidhya.html', 'r') as f:
            x = f.read()
            pass
        pass

    tree = html.fromstring(x)
    contest_name_list = tree.xpath('/html/body/div/div/div/div[2]/ul/li/a/div[2]/h4/text()')  # contest name
    contest_url_list = tree.xpath('/html/body/div/div/div/div[2]/ul/li/a/@href')
    contest_time_list = tree.xpath('/html/body/div/div/div/div[2]/ul/li/a/div[2]/p/text()[1]')

    length = len(contest_name_list)

    for i in range(length):
        start_time, end_time = contest_time_list[i].split(' to ')

        temp = {}

        epoch = datetime.utcfromtimestamp(0)
        start_time = datetime.strptime(start_time, "%d-%m-%Y")
        start_time -= epoch
        start_time = int(start_time.total_seconds())
        temp["start_time"] = start_time

        epoch = datetime.utcfromtimestamp(0)
        end_time = datetime.strptime(end_time, "%d-%m-%Y")
        end_time -= epoch
        end_time = int(end_time.total_seconds())
        temp["end_time"] = end_time

        url = 'https://datahack.analyticsvidhya.com'

        temp["competiton_name"] = contest_name_list[i]
        temp["site_name"] = "Analytics Vidhya"
        temp["classification"] = "h"
        temp["URL"] = url + contest_url_list[i]
        output.append(temp)

        del temp, start_time, end_time, epoch, url

        pass
    del tree, contest_url_list, contest_name_list, contest_time_list, x
    return output
    pass


def devpost(DEPLOY=False):
    x = ""
    output = []
    page_no = 1

    contest_name_list = []
    contest_url_list = []
    contest_time_list = []

    while (page_no > 0):

        if DEPLOY:
            x = requests.get(
                "https://devpost.com/hackathons?utf8=%E2%9C%93&search=&challenge_type=online&sort_by=Submission+Deadline&page=" + str(
                    page_no)).text

        else:
            with open(CURRENT_DIR + '/testing_sites/input_devpost.html', 'r') as f:
                x = f.read()

                # step to break the loop
                page_no = -1;
                pass
            pass

        tree = html.fromstring(x)
        local_contest_name_list = tree.xpath(
            '/html/body/section/div/div/div/div/div[1]/div/div/article/a/div[1]/section/div/h2/text()')  # contest name
        local_contest_url_list = tree.xpath(
            '/html/body/section/div/div/div/div/div[1]/div/div/article/a/@href')  # contest url
        local_contest_time_list = tree.xpath(
            '/html/body/section/div/div/div/div/div[1]/div/div/article/a/div[2]/section/div[2]/div/div[2]/time/@datetime')  # contest time

        if len(local_contest_name_list) == 0:
            page_no = -1
        else:
            contest_name_list += local_contest_name_list
            contest_url_list += local_contest_url_list
            contest_time_list += local_contest_time_list

        # incrementing the page number
        page_no += 1

        del local_contest_time_list, local_contest_name_list, local_contest_url_list
        pass

    length = len(contest_name_list)

    for i in range(length):
        temp = {}

        epoch = datetime.utcfromtimestamp(0)
        start_time = datetime.now()
        start_time -= epoch
        start_time = int(start_time.total_seconds() + i)
        temp["start_time"] = start_time

        epoch = datetime.utcfromtimestamp(0)
        # time = 2017-06-24T21:00:00-04:00
        end_time = datetime.strptime(contest_time_list[i][:contest_time_list[i].rfind('-')], "%Y-%m-%dT%H:%M:%S")
        end_time -= epoch
        end_time = int(end_time.total_seconds())
        temp["end_time"] = end_time

        temp["competiton_name"] = contest_name_list[i]
        temp["site_name"] = "Devpost"
        temp["classification"] = "h"
        temp["URL"] = contest_url_list[i]

        output.append(temp)

        del temp, start_time, end_time, epoch

        pass
    del tree, contest_url_list, contest_name_list, contest_time_list, x
    return output


def techgig(DEPLOY=False):
    x = ""
    output = []
    if DEPLOY:
        x = requests.get("https://www.techgig.com/challenge").text
    else:
        with open(CURRENT_DIR + '/testing_sites/input_techgig.html', 'r') as f:
            x = f.read()
            pass
        pass

    tree = html.fromstring(x)
    contest_name_list = tree.xpath(
        '/html/body/div[2]/div[9]/div/div/div[1]/div/div/div/div/span/a/div[2]/h5/text()')  # contest name
    contest_url_list = tree.xpath('/html/body/div[2]/div[9]/div/div/div[1]/div/div/div/div/span/a/@href')
    contest_time_list = tree.xpath(
        '/html/body/div[2]/div[9]/div/div/div[1]/div/div/div/div/span/a/div[2]/span[1]/text()')

    length = len(contest_name_list)

    for i in range(length):
        temp = {}

        start_time, end_time = contest_time_list[i].split('-')

        epoch = datetime.utcfromtimestamp(0)
        start_time = datetime.strptime(start_time.strip() + " " + str(datetime.now().year), "%d %b %Y")
        start_time -= epoch
        start_time = int(start_time.total_seconds())
        temp["start_time"] = start_time

        epoch = datetime.utcfromtimestamp(0)
        end_time = datetime.strptime(end_time.strip() + " " + str(datetime.now().year), "%d %b %Y")
        end_time -= epoch
        end_time = int(end_time.total_seconds())
        temp["end_time"] = end_time

        temp["competiton_name"] = contest_name_list[i]
        temp["site_name"] = "Techgig"
        temp["classification"] = "cp"
        temp["URL"] = contest_url_list[i]

        output.append(temp)
        del temp, start_time, end_time, epoch
        pass

    del tree, contest_url_list, contest_name_list, contest_time_list, x
    return output


    # print (venturesity(DEPLOY = True))
    # print (venturesity())

    # hackerrank()

    # print (codechef(DEPLOY = True))
    # print (codechef())

    # print (codeforces())

    # print (analyticsvidhya(DEPLOY = True))

    # print (devpost(DEPLOY = False))

    # print (techgig(DEPLOY = False))
