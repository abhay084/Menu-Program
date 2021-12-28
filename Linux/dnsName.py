from nslookup import Nslookup

domain = "google.com"

dns_query = Nslookup(dns_servers=["1.1.1.1"])

ips_record = dns_query.dns_lookup(domain)

print(ips_record.response_full,ips_record.answer)

soa_record = dns_query.soa_lookup(domain)

print(soa_record.response_full,soa_record.answer)
