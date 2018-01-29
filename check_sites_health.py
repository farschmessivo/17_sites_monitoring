import whois
import sys
from datetime import datetime, timedelta
import requests

month = 31


def load_urls4check(path):
    domains = []
    with open(path, 'r') as file:
        for line in file:
            domains.append(line.rstrip())
    return domains


def is_server_respond_with_200(domain):
    response = requests.get(domain)
    return response.ok


def is_expiration_in_month(date_time):
    if isinstance(date_time, list):
        time_left = min(date_time) - datetime.now()
    else:
        time_left = date_time - datetime.now()
    return True if time_left.days < month else False


def get_domain_expiration_date(url):
    domain_expiration_date = whois.whois(url)
    if isinstance(domain_expiration_date, list):
        domain_expiration_date = domain_expiration_date[0]
    return domain_expiration_date.expiration_date


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit('Usage: python3 check_sites_health.py <path_to_txt>')
    filepath = sys.argv[1]
    websites = load_urls4check(filepath)
    for website in websites:
        print('Checking {}'.format(website))
        print('\tServer respond with 200: {}'.format(
            is_server_respond_with_200(website)))
        expiration_date = get_domain_expiration_date(website)
        print('\tExpiring in month: {}\n'.format(
            is_expiration_in_month(expiration_date)))
