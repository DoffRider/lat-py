import xml.etree.ElementTree as ET
data = '''<person>
    <name>Palui</name>
    <phone type="intl">
        +6283183198
        </phone>
        <email hide="yes"/>
    </person>'''

tree = ET.fromstring(data)
print('Nama : ',tree.find('name').text)
print('Attr : ',tree.find('email').get('hide'))