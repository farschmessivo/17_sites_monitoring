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


def is_expiry_date_close(
        date_time,
        number_of_days_in_month
    ):
    time_left = date_time - datetime.now()
    return time_left.days < number_of_days_in_month


def get_domain_expiration_date(url):
    domain_info = whois.whois(url)
    expiry_date_time = domain_info.expiration_date
    if expiry_date_time is None:
        return None
    elif isinstance(expiry_date_time, list):
        return min(expiry_date_time)
    else:
        return expiry_date_time


def print_domain_health(
        url,
        server_response,
        expiration_date
    ):
    print('\tChecking {}:'.format(url))
    print('\tServer respond with 200: {}'.format(
        server_response
    ))
    if expiration_date is None:
        print('\tNo expiry date for {}'.format(url))
    else:
        print('\tExpiring in a month: {}\n'.format(
            is_expiry_date_close(
                expiration_date,
                days_in_calendar_month
            )
        ))


if __name__ == '__main__':
    days_in_calendar_month = 31
    if len(sys.argv) == 1:
        sys.exit('Usage: python3 check_sites_health.py <path_to_txt>')
    filepath = sys.argv[1]
    urls = load_urls_list(filepath)
    for url in urls:
        server_response = is_server_respond_ok(url)
        expiration_date = get_domain_expiration_date(url)
        print_domain_health(
            url,
            server_response,
            expiration_date
        )

