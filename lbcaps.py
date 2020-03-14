import requests
import json
from yattag import Doc, indent

url = "http://dwebsrv02.lbcapps.com/lbcpickuprequest/api/DirectInjection/InsertPickupRequest"

payload = """<PickupRequestEntity xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\">  
<AppKey>2b28bdaf34a34bc88cf0135fae6244c2</AppKey>
<ShipmentMode>1</ShipmentMode>
<Origin>MMB</Origin><Destination />
<TransactionDate>11/07/2019 11:28:47</TransactionDate>
<ODZ>false</ODZ>
<ShipperAccountNo>2019100826898887</ShipperAccountNo>
<Shipper>SHOPEE PHILIPPINES, INC</Shipper>
<ShipperStBldg>37/F Net Park Building, 5th Ave., Bonifacio Global City, Taguig, PH 1634</ShipperStBldg>
<ShipperBrgy>ANYWHERE</ShipperBrgy>
<ShipperCityMuncipality>TAGUIG CITY</ShipperCityMuncipality>
<ShipperProvince>METRO MANILA</ShipperProvince>  
<ShipperContactNumber>0</ShipperContactNumber>
<ShipperSendSMS>0</ShipperSendSMS>
<ShipperMobileNumber>0</ShipperMobileNumber>
<ProductLine>2</ProductLine>
<ServiceMode>8</ServiceMode>
<CODAmount>5499</CODAmount>
<PreferredDate>11/25/2020 10:10:10</PreferredDate>
<Consignee>mark philip zurbito</Consignee>
<ConsigneeStBldg>Test Consignee Address</ConsigneeStBldg>
<ConsigneeBrgy>33446</ConsigneeBrgy>
<ConsigneeCityMuncipality>1129</ConsigneeCityMuncipality>
<ConsigneeProvince>42</ConsigneeProvince>
<ConsigneeContactNumber>524807617</ConsigneeContactNumber>
<ConsigneeSendSMS>1</ConsigneeSendSMS>
<ConsigneeMobileNumber>524807617</ConsigneeMobileNumber>
<Quantity>1</Quantity>
<PKG>16</PKG>
<ACTWTkgs>0</ACTWTkgs>
<LengthCM>0</LengthCM>
<WidthCM>0</WidthCM>
<HeightCM>0</HeightCM>
<VolWTcbm>0</VolWTcbm>
<CBM>0</CBM>
<ChargeableWT>0</ChargeableWT>
<DeclaredValue>2000</DeclaredValue>
<Description>Ace 32" Slim LED TV Black LED-808 DN4(qty-1)</Description>
<Commodity xsi:nil="true" />
<ForCrating xsi:nil=\"true\" />
<AttachmentNameOne>ORDERNO</AttachmentNameOne>
<ReferenceNoOne>SP123456792</ReferenceNoOne>
<AttachmentNameTwo>SHOPEEMODE</AttachmentNameTwo>
<ReferenceNoTwo>REGULAR</ReferenceNoTwo>
<AttachmentNameThree>SHOPEESLS</AttachmentNameThree>
<ReferenceNoThree>123456792</ReferenceNoThree>
<AttachmentNameFour>STATUS</AttachmentNameFour>
<ReferenceNoFour>0</ReferenceNoFour>
<DestinationCode>COP</DestinationCode>
<Client>SPE</Client>
</PickupRequestEntity>
"""

headers = {
    'Content-Type': 'application/xml'
}

doc, tag, text = Doc().tagtext()
# doc.asis('<?xml version="1.0" encoding="utf-8"?>')
with tag('AppKey'):
    text('2b28bdaf34a34bc88cf0135fae6244c2')
with tag('ShipmentMode'):
    text(1)  # default to 1
with tag('Origin'):
    text('MMB')  # origin where merchant is located-check with LBC
with tag('TransactionDate'):
    text('11/07/2019 11:28:47')  # Ordered Date - Format MM/DD/YYYY HH:MM:SS
with tag('ODZ'):
    text('false')  # default to false
with tag('ShipperAccountNo'):
    text(2019100826898887)  # Merchants account no-check with LBC
with tag('Shipper'):
    text('Merchant seller company name')  # Merchant seller company name-check with LBC
with tag('ShipperStBldg'):
    text("37/F Net Park Building, 5th Ave., Bonifacio Global City, Taguig, PH 1634")
with tag('ShipperBrgy'):
    text("ANYWHERE")
with tag('ShipperCityMuncipality'):
    text("TAGUIG CITY")
with tag('ShipperProvince'):
    text("METRO MANIL")
with tag('ShipperContactNumber'):
    text(0)
with tag('ShipperSendSMS'):
    text(0)  # default to 0
with tag('ShipperMobileNumber'):
    text(0)  # 0 if not applicable
with tag('ProductLine'):
    text(2)  # only use 2 (Cargo)
with tag('ServiceMode'):
    text(8)  # default to 8 - door to door
# if not order.cod_amt_to_collect:
#     cod_amt_to_collect = '0.00'
# else:
#     cod_amt_to_collect = '{0:.2f}'.format(order.cod_amt_to_collect)
with tag('CODAmount'):
    text(5499)
with tag('PreferredDate'):
    text("11/25/2020 10:10:10")  # confirm date & time - Format MM/DD/YYYY HH:MM:SS-check
with tag('Consignee'):
    text("mark philip zurbito")
with tag('ConsigneeStBldg'):
    text("Test Consignee Address")
with tag('ConsigneeBrgy'):
    text("33446")
with tag('ConsigneeCityMuncipality'):
    text(1129)
with tag('ConsigneeProvince'):
    text(42)
with tag('ConsigneeContactNumber'):
    text('524807617')
with tag('ConsigneeSendSMS'):
    text(1)  # optional
with tag('ConsigneeMobileNumber'):
    text("524807617")
with tag('Quantity'):
    text(1)  # to check
with tag('PKG'):
    text(16)  # default to 16
with tag('ACTWTkgs '):
    text('{0:.2f}'.format(0))
with tag('LengthCM'):
    text(0)
with tag('WidthCM'):
    text(0)
with tag('HeightCM'):
    text(0)
with tag('VolWTcbm'):
    text(0)  # volumetric weight-check with LBC - LXWXH/3500 in kg
with tag('CBM'):
    text(0)  # default to 0 (sea cargo)
with tag('ChargeableWT'):
    text(0)  # default to 0
with tag('DeclaredValue'):  # package value - kerryhk
    text(2000)  # Package value to check
with tag('Description'):
    text('items description')  # check example from ams

with tag('AttachmentNameOne'):  # check with LBC
    text('ORDERNO')  # Merchant Order Number
with tag('ReferenceNoOne'):  # check with LBC
    text('SP123456792')

with tag('AttachmentNameTwo'):
    text('MERCHANTS MODE')  # check with LBC
with tag('ReferenceNoTwo'):
    text('REGULAR')

with tag('AttachmentNameThree'):
    text('SHOPEESLS')  # Merchant SLS tracking number - check with LBC
with tag('ReferenceNoThree'):
    text('123456789')

with tag('AttachmentNameFour'):
    text('STATUS')  # check with LBC
with tag('ReferenceNoFour'):
    text('0')

with tag('DestinationCode'):  # Use elastic search - map given values
    text('COP')

with tag('Client'):
    text('SPE')  # Merchants code check with LBC

message = indent(doc.getvalue(), indentation=' ' * 4, newline='\r\n')
xml_payload = """<PickupRequestEntity xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\">
{}
<Commodity xsi:nil="true" />
<ForCrating xsi:nil="true" />
</PickupRequestEntity>""".format(message)
print('REQUEST', xml_payload)

response = requests.request("POST", url, headers=headers, data=xml_payload)

json_resp = json.loads(response.text)
print(json_resp)
