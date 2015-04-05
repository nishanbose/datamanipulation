#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'nishan'

import re
import urlparse

# secondary function for validating lenth of query string
def checkcond(url):
        result = urlparse.urlparse(url)
        a = urlparse.parse_qs(result.query)
        for k, v in a.items():
            for i in v:
                if len(i) > 255:
                    return False

# primary function for reading the lines
def process_log_file(fileName):

    IN = open(fileName, 'rU')

    # initiating list for logs
    valid_logs = list()
    invalid_logs = list()

    # initiating list for domain storage
    high_level_domain = []

    for line in IN:
        # extracting status code
        status_url = re.search(r'(?:\"\s200\s)', line)

        # splitting the complete line
        split_line = re.search(r'([\s]+)', line)
        line = line.split(split_line.group(1))

        # extracting post url (GET or POST)
        post_url = line[5].strip().replace('"', '')

        # extracting full url
        main_url = line[6].strip()

        # Splitting Dates for correct format
        timestamp = line[3].strip()
        date_regex = re.search(r'[[0-9]{2}/[a-zA-Z]{3}/[0-9]{4}', timestamp)
        date_split = date_regex.group(0)
        date_split1 = re.search(r'([0-9]{2})/([a-zA-Z]{3})/([0-9]{4})', date_split)
        date_new = str(date_split1.group(3)) + '-' + str(date_split1.group(2)) + '-' + str(date_split1.group(1))

        # Regular Expression for Validating URLs
        tld = re.search(r'(^http[s]?)://([A-Za-z]+[^/:]+)\.([A-Za-z]+)[/:]?', main_url, re.IGNORECASE)

        # Checking if log is valid
        if (post_url == "GET" or post_url == "POST") and status_url and tld and checkcond(main_url) != False:
            # creating list for top-level-domains
            tld2 = tld.group(3).lower()
            high_level_domain.append(tld2)
            # storing values in a dictionary
            valid_logs.append({'date':date_new, 'top_level_domain':tld2})
        else:
            # storing values in a list
            invalid_logs.append(line)

    # reducing duplicates in valid domains list
    u_doms = set(high_level_domain)
    uniq_domains = sorted(u_doms)

    return (valid_logs, invalid_logs, uniq_domains)


# start execution
if __name__ == '__main__':

    # passing arguments to primary function
    (valid_logs, invalid_logs, uniq_domains) = process_log_file('access_log.txt')

    #writing out invalid_access_log
    OUT1 = open('invalid_access_log_nishan.txt', 'w')

    with OUT1 as f:
        f.writelines(' '.join(str(j) for j in i) for i in invalid_logs)
    OUT1.close()


    #Processing valid_access_log
    report=dict()

    for item in valid_logs:
        top_level_domain=item['top_level_domain']
        date=item['date']
        if report.get(date)==None:
            report[date]=dict()
            report[date][top_level_domain]=1
        else:
            if report[date].get(top_level_domain)==None:
                report[date][top_level_domain]=1
            else:
                report[date][top_level_domain]+=1

    output1 = list()

    for i in uniq_domains:
        for k, v in report.items():
            if i not in v.keys():
                report[k][i] = 0


    OUT2 = open(r'valid_log_summary_nishan.txt','w+')

    uniq_domains.insert(0, "date")

    OUT2.write('\t'.join(map(str, uniq_domains)))

    uniq_domains.pop(0)

    sortedKeys1=sorted(report.keys())
    for date in sortedKeys1:
        count=report[date]
        sortedKeys2=sorted(count.keys())
        output=date
        for top_level_domain in sortedKeys2:
            output=output+'\t'+str(count[top_level_domain])
        OUT2.write('\n'+output)
    OUT2.close()