import whois  # i'm using this http://cryto.net/pythonwhois

f = open('domains.txt','r')
urls = f.readlines()
domains = []
for line in urls:
    domains.append(line)
f.close()


for dom in domains:
    details = whois.query(dom)
    print(details.__dict__)