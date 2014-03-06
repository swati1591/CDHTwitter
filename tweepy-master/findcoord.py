import sys
import urllib
from xml.dom import minidom

googleGeocodeUrl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

def geocode(address):
    parms = {
        'output': 'csv',
        'address': address,
	'sensor':'false'}

    url = googleGeocodeUrl + urllib.urlencode(parms)
    #print url
    resp = urllib.urlopen(url)
    xmlresp=minidom.parse(resp)
    #print xmlresp.toxml()
    latitude=0
    longitude=0
    for element in xmlresp.getElementsByTagName('status'):
        status= element.firstChild.nodeValue
    for element in xmlresp.getElementsByTagName('lat'):
        latitude= element.firstChild.nodeValue
    for element in xmlresp.getElementsByTagName('lng'):
        longitude= element.firstChild.nodeValue
    #if float(longitude)<float(-70) and float(latitude)<float(42):
    #     print "In range"
    #     status='OK'
    if float(latitude)<float(42) and float(latitude)>float(25) and float(longitude)<float(-70) and float(longitude)>float(-179):
        status='OK'
    else:
        status='NO'
    return status
    #if(status!='OK'):
    #    latitude=0
    #    longitude=0
    #print latitude
    #print longitude
    #return latitude, longitude

def main():
    if 1 < len(sys.argv):
        address = sys.argv[1]
    else:
        address = '1600 Amphitheatre Parkway, Mountain View, CA 94043, USA'
    print address	
    coordinates = geocode(address)
    print coordinates

if __name__ ==  '__main__':
    main()
