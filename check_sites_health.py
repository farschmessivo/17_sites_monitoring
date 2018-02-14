import whois
import sys
import requests
from datetime import datetime


def load_urls_list(path):
    with open(path, 'r') as file_with_urls:
        return file_with_urls.read().splitlines()


def is_server_respond_ok(domain):
    try:
        response = requests.get(domain)
        return response.ok
    except requests.exceptions.RequestException:
        return False


def is_expiry_date_close(date_time, number_of_days_in_month):
    if isinstance(date_time, list):
        time_left = min(date_time) - datetime.now()
    else:
        time_left = date_time - datetime.now()
    return time_left.days < number_of_days_in_month


def get_domain_expiration_date(url):
    domain_info = whois.whois(url)
    return domain_info.expiration_date


if __name__ == '__main__':
    days_in_calendar_month = 31
    if len(sys.argv) == 1:
        sys.exit('Usage: python3 check_sites_health.py <path_to_txt>')
    filepath = sys.argv[1]
    urls = load_urls_list(filepath)
    for url in urls:
        print('Checking {}'.format(url))
        print('\tServer respond with 200: {}'.format(
            is_server_respond_ok(url)
        ))
        expiration_date = get_domain_expiration_date(url)
        if expiration_date is None:
            print('No expiry date for {}'.format(url))
        else:
            print('\tExpiring in month: {}\n'.format(
                is_expiry_date_close(expiration_date, days_in_calendar_month)
            ))
