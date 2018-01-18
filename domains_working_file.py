import whois
from datetime import datetime, timedelta
from tld import get_tld
import requests


def load_list_of_domains():
    f = open('domains.txt', 'r')
    urls = f.readlines()
    domains = []
    for line in urls:
        domains.append(line.strip())
    f.close()
    print(domains)
    return domains


def check_200(domains):
    for dom in domains:
        print(dom)
        r = requests.get(dom)
        print(r.status_code)
        print(check_if_expiration_date_is_ok(dom))


def check_if_expiration_date_is_ok(dom):
    details = whois.whois(dom)
    domain_expiration_date = details.expiration_date
    print(domain_expiration_date)
    time_now = datetime.now()
    print(time_now)
    if isinstance(domain_expiration_date, (list)):
        domain_expiration_date = domain_expiration_date[0]
    print(domain_expiration_date - datetime.now())
    if domain_expiration_date - datetime.now() >= timedelta(days=31):
        print('ok')
    else:
        print('not ok')


# # def check_if_expiration_date_is_ok(domains):
# #     for dom in domains:
# #         time_now = datetime.now()
# #         details = whois(dom)
# #         domain_expiration_date = details.expiration_date
# #         print(domain_expiration_date - time_now)
# #         print(domain_expiration_date)
# #         print(time_now)
# #         print(timedelta(days=31))
# #         if domain_expiration_date - time_now >= timedelta(days=31):
# #             print('ok')
# #         else:
# #             print('not ok')
#
if __name__ == '__main__':
    domains = load_list_of_domains()
    output = check_200(domains)
    ququshka = check_if_expiration_date_is_ok(domains)




# isinstance([], (list))




# details = whois.whois('github.com')
# domain_expiration_date = details.expiration_date
# print(domain_expiration_date)
# time_now = datetime.now()
# print(time_now)
# if isinstance(domain_expiration_date, (list)):
#     domain_expiration_date = domain_expiration_date[0]
# print(domain_expiration_date - datetime.now())
# if domain_expiration_date - datetime.now() >= timedelta(days=31):
#     print('ok')
# else:
#     print('not ok')