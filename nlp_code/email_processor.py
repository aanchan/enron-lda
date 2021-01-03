import email
import re


def write_processed_email(file_name,email_str):
    """
    Function that takes in a file name and an email
    string and writes the email string to the file.
    Args:
        file_name: File name
        email_str: Email string

    Returns:

    """
    f = open(file_name, 'w')
    f.write(email_str)
    f.close()


def read_email_file(data_path):
    """
    Function to read a raw email file
    Args:
        data_path:

    Returns:
        A string containing the email contents
    """
    f = open(data_path, 'r')
    msg_string=f.read()
    f.close()
    return msg_string



def if_skip_line(inp_str):
    """
    This function consumes a single line of an
    email as a string and goes through a series
    of regular expressions and marks if this
    line should be skipped or not.
    Args:
        inp_str:

    Returns:
        A boolean value skip_line which is set to :
        False - if the line is not be skipped and
        True - if the line is to be skipped
    """
    skip_line = False

    if inp_str:
        r_date = re.compile("Date:")
        r_to = re.compile("[Tt]o:")
        #lines containing ----Forwarded message
        dashes_dates=re.compile('-{4,}')
        r_underscore = re.compile('_{4,}')
        #email regex from emailregex.com
        email_regex = re.compile("(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"
                                 "\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")"
                                 "@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)"
                                 "+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)"
                                 "{3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:"
                                 "(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])")
        #lines containing date-sender-to-from
        r_from = re.compile("From:")
        r_am_pm = re.compile('[AP]M')
        r_subject = re.compile("Subject:")
        r_enron = re.compile("@ENRON")
        r_sp_enron = re.compile("@ ENRON")
        r_sent_by = re.compile("Sent by:")
        r_sent = re.compile("Sent:")
        r_content = re.compile("Content-Type:")
        r_mime = re.compile("MIME-Version:")
        r_x_mailer = re.compile("X-Mailer:")
        r_mozilla = re.compile("X-Mozilla")
        r_fw =re.compile("[Ff][Ww]")

        r_enron_x_gate = re.compile("@enronXgate")
        r_enron_sm = re.compile("@Enron")
        r_mail_to = re.compile("mailto:")
        r_simple_email = re.compile('\S*@\S*\s?')
        patt_list = [dashes_dates, email_regex, r_subject, r_date, r_from,
                     r_am_pm, r_enron, r_sp_enron, r_mail_to, r_sent, r_sent_by, r_enron_x_gate, r_enron_sm,
                     r_simple_email, r_content, r_mime, r_x_mailer, r_mozilla, r_fw, r_to, r_underscore]

        for patt in patt_list:
            if re.findall(patt, inp_str):
                skip_line = True
                break
    else:
        skip_line=True

    return skip_line

def remove_email_headers(inp_str):
    """
    A function that operates on an input string
    to remove email headers. Regular expressions
    in this function use lookahead to deal with
    multiple emails addresses and replaces them
    with an empty string
    Args:
        inp_str:

    Returns:
        An email string without email headers
    """
    r_marker = re.compile('>', re.MULTILINE)
    r_received = re.compile("Received:\ (.|\n)+?Subject:", re.MULTILINE)
    r_to = re.compile("To:\ (.|\n)+?(?=cc:)", re.MULTILINE)
    r_cc = re.compile('cc:\ (.|\n)+?(?=Subject:)', re.MULTILINE)
    r_sent_by = re.compile('Sent by:\ (.|\n)+?(?=Subject:)', re.MULTILINE)
    inp_str = re.sub(r_marker, '', inp_str)
    inp_str = re.sub(r_received, '', inp_str)
    inp_str_no_to = re.sub(r_to, '', inp_str)
    inp_str_no_cc = re.sub(r_cc, '', inp_str_no_to)
    inp_str_no_sent_by = re.sub(r_sent_by, '', inp_str_no_cc)
    return inp_str_no_sent_by


def process_email(email_string):
    """
    A function that takes a raw email message
    and calls the appropriate methods to
    clean up the email contents and make the
    resulting text string suitable for further
    processing.
    Args:
        email_string:

    Returns:
        A cleaned up string containing perhaps multiple
        email bodies together.
    """
    b = email.message_from_string(email_string)
    payload = b.get_payload()
    payload_no_headers = remove_email_headers(payload)
    lines_of_interest = []
    for line in payload_no_headers.splitlines():  # keepends=True
        if not if_skip_line(line):
            lines_of_interest.append(line)

    joined_document = " ".join(lines_of_interest)
    return joined_document