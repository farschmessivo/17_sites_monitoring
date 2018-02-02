import whois
import sys
from datetime import datetime
import requests


def load_urls_list(path):
    with open(path, 'r') as domains:
        return domains.read().splitlines()


def is_server_respond_ok(domain):
    response = requests.get(domain)
    return response.ok


def is_expiration_in_month(date_time, number_of_days_in_month):
    if isinstance(date_time, list):
        time_left = min(date_time) - datetime.now()
    else:
        time_left = date_time - datetime.now()
    return True if time_left.days < number_of_days_in_month else False


def get_domain_expiration_date(url):
    domain_info = whois.whois(url)
    return domain_info.expiration_date


if __name__ == '__main__':
    days_in_calendar_month = 31
    if len(sys.argv) == 1:
        sys.exit('Usage: python3 check_sites_health.py <path_to_txt>')
    filepath = sys.argv[1]
    websites = load_urls_list(filepath)
    for website in websites:
        print('Checking {}'.format(website))
        print('\tServer respond with 200: {}'.format(
            is_server_respond_ok(website)))
        expiration_date = get_domain_expiration_date(website)
        print('\tExpiring in month: {}\n'.format(
            is_expiration_in_month(expiration_date, days_in_calendar_month)))
