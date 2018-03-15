#!/usr/bin/env python2
# -*- coding:utf-8 -*-

"""
Convert https://github.com/caorong/gfwlist2pac to gfwlist forward-zone for unbound.
"""

from sys import argv
import re

script, gfwlist2pac, unbound_zone = argv

gfwlist_fp = open(gfwlist2pac)
unbound_zone_fp = open(unbound_zone, 'w')

for line in gfwlist_fp:
    if re.match(r"  \".*\": \d,", line) != None:
        domain_valid = line.split('"')[1]
        zone_line1 = "forward-zone:\n"
        zone_line2 = '        name: \"' + domain_valid + '\"\n'
        zone_line3 = "        forward-addr: 127.0.0.1@60053\n"
        unbound_zone_fp.writelines(zone_line1 + zone_line2 + zone_line3)

gfwlist_fp.close()
unbound_zone_fp.close()