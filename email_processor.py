import email
import re


def if_skip_line(inp_str):
    skip_line = False
    if inp_str:
        #lines containing ----Forwarded message
        dashes_dates=re.compile('-{4, }(. *)(\d{2}:\d{2}:\d{2})\s * (PM | AM)')
        #email regex from emailregex.com
        email_regex = re.compile("(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"
                                 "\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")"
                                 "@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)"
                                 "+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)"
                                 "{3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:"
                                 "(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])")
        #lines containing date-sender-to-from
        r_date = re.compile("^Date:\ (?P<date>.+?$)")
        r_sender = re.compile("^From:\ (?P<sender>.+?$)")
        r_to = re.compile("^To:\ (?P<to>.+?$)")
        r_cc = re.compile("^cc:\ (?P<cc>.+?$)")
        r_subject = re.compile("^Subject:\ (?P<subject>.+?$)")
        patt_list = [dashes_dates, email_regex, r_date, r_sender, r_to,
                     r_cc, r_subject]

        for patt in patt_list:
            if re.findall(patt, inp_str):
                skip_line = True
                break
    else:
        skip_line=True

    return skip_line


def process_email(email_string):
    b = email.message_from_string(email_string)
    payload = b.get_payload()
    lines_of_interest = []

    for line in payload.splitlines():  # keepends=True
        if not if_skip_line(line):
            lines_of_interest.append(line)

    joined_document = " ".join(lines_of_interest)
    return joined_document