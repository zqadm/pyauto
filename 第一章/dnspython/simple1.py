#!/usr/bin/env python
import dns.resolver
from past.builtins import raw_input

domain = raw_input('Please input an domain: ')

A = dns.resolver.query(domain, 'A')
for i in A.response.answer:
    for j in i.items:
        print(j.address)

