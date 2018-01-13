import whois
from datetime import datetime, timedelta

f = open('domains.txt','r')
urls = f.readlines()
domains = []
for line in urls:
    domains.append(line)
f.close()

for dom in domains:
    time_now = datetime.now()
    details = whois.whois(dom)
    domain_expiration_date = details.expiration_date

    if domain_expiration_date - datetime.now() >= timedelta(days=31):
        print('ok')
    else:
        print('not ok')






# details = whois.whois('romangagarin.com')
# domain_expiration_date = details.expiration_date
# print(domain_expiration_date)
# time_now = datetime.now()
# print(time_now)
# if domain_expiration_date - datetime.now() >= timedelta(days=31):
#     print('ok')
# else:
#     print('not ok')