#!/usr/bin/env python
# coding=utf-8

import xml.etree.ElementTree as ET

def xml_test():
    data = """
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>"""

    print data
    tree = ET.fromstring(data)
    print 'Name', tree.find('name').text
    print 'Attr', tree.find('email').get('hide')

xml_test()
