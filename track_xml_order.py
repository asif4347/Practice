from datetime import datetime

import requests
import xmltodict
import json
import pprint

url = "https://trackntrace.lbcapps.com/tntapi/"
tracking_no = '500000000921457'


def get_tracking_status_from_lbc():
    # TODO Uncomment the code for dynamic data
    # ext_order_info_queryset = order_models.ExternalOrderInfo.objects.filter(
    #     # order_id__in=order_queryset,
    #     partner_name='DTDC UK',
    #     order_id__created_on__gte=datetime.now(tz=timezone.utc) + timedelta(
    #         days=settings.DAYS_TO_FETCH_TRACKING_UPDATES)
    # ).exclude(
    #     order_id__tracker_status_code='SUCCESS'
    # ).select_related('order_id')
    # for ext_order_info in ext_order_info_queryset:          #TOdo for multiple data
    payload = """<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
    <LBCTrackAndTrace xmlns="http://tempuri.org/">
    <TrackingNo>{}</TrackingNo>
    </LBCTrackAndTrace>
    </soap:Body>
    </soap:Envelope>""".format(tracking_no)
    headers = {
        'Content-Type': 'text/xml'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    xml_resp = response.text.encode('utf8')
    dict_resp = xmltodict.parse(xml_resp)
    dict_data = dict_resp['soap:Envelope']['soap:Body']['LBCTrackAndTraceResponse']
    tracking = dict_data['LBCTrackAndTraceResult']['TrackingStatus']['TrackingDetails']['TrackingDetails']
    datetime_obj = datetime.strptime(tracking['TransactionDate'], '%b %d, %Y')
    print(datetime_obj)
    # tracker_tasks.update_tracker_for_partner.delay(.....)


if __name__ == '__main__':
    get_tracking_status_from_lbc()

# the response data will be like. so use it accordingly
"""
{
    "LBCTrackAndTraceResponse": {
        "@xmlns": "http://tempuri.org/",
        "LBCTrackAndTraceResult": {
            "TrackingStatus": {
                "StatusCode": "0001",
                "StatusMessage": "SUCCESS!",
                "TrackingDetails": {
                    "TrackingDetails": {
                        "ActualWt": null,
                        "BranchDestiId": "0",
                        "BranchDestination": null,
                        "Branch_Origin": "PHIL PREMIUM KLEEN CORP.",
                        "ConsigneeAddress": `ST. JUDE ST, LOT 13, PH1 SEC1 
                             BLK2 BELVEDERE TOWNE BRGY PARADAHAN UNO,   , TANZA , CAVITE , (LANDMARK NEAR 
                             AT 7/11 ARCO NG FIL-INVEST THEN GUARD HOUSE MAG ASK NA LANG), ANYWHERE, 
                             TANZA, CAVITE`,
                        "ConsigneeContact": "9167762485",
                        "ConsigneeName": "JANETTE ESLABON",
                        "Content": "GRF033050",
                        "ProdDescr": null,
                        "Product": "DOCUMENTS",
                        "ShipperAddress": `128B LOPE K. SANTOS STREET, PEDRO 
                            CRUZ, SAN JUAN CITY SAN JUAN CITY METRO MANILA`,
                        "ShipperContact": "875-7500,919-4866",
                        "ShipperName": "PHIL PREMIUM KLEEN",
                        "TNTStatus": "Delivered",
                        "TrackingNo": "500000000921457",
                        "TransactionDate": "Oct 31, 2019",
                        "VolWt": null,
                        "volDescr": null
                    }
                },
                "TrackingHistory": {
                    "TrackingHistory": [
                        {
                            "Branch": {
                                "BranchCode": "FNC01",
                                "BranchDescr": "FINANCE",
                                "BranchId": "4286"
                            },
                            "DateInserted": null,
                            "DatePosted": "04/11/2019",
                            "DatePostedTime": "12:00:00 AM",
                            "Remarks": null,
                            "StatusandLocation": `The amount has been 
                                 remitted to the specified bank account and will be credited within 3 banking 
                                 days.`,
                            "TrackingHistoryID": "61388946113"
                        },
                        {
                            "Branch": {
                                "BranchCode": "EXS01",
                                "BranchDescr": "SCS COURIER FACILITY -MANILA",
                                "BranchId": "1908"
                            },
                            "DateInserted": null,
                            "DatePosted": "10/31/2019",
                            "DatePostedTime": "08:32:22 PM",
                            "Remarks": "PHIL PREMIUM/MARVIC",
                            "StatusandLocation": "Arrived at  SCS COURIER FACILITY - MANILA.",
                            "TrackingHistoryID": "59012254680"
                        },
                        {
                            "Branch": {
                                "BranchCode": "CTEHA",
                                "BranchDescr": "CAVITE 3",
                                "BranchId": "4151"
                            },
                            "DateInserted": null,
                            "DatePosted": "11/01/2019",
                            "DatePostedTime": "01:41:15 AM",
                            "Remarks": "ROS 3 SCS PRODUCTS 11578991 ALLAN",
                            "StatusandLocation": "Forwarded to CAVITE 3.",
                            "TrackingHistoryID": "59033527333"
                        },
                        {
                            "Branch": {
                                "BranchCode": "CTEHA",
                                "BranchDescr": "CAVITE 3",
                                "BranchId": "4151"
                            },
                            "DateInserted": null,
                            "DatePosted": "11/01/2019",
                            "DatePostedTime": "05:51:00 AM",
                            "Remarks": null,
                            "StatusandLocation": "Arrived at  CAVITE 3.",
                            "TrackingHistoryID": "59043460605"
                        },
                        {
                            "Branch": {
                                "BranchCode": "CTEHA",
                                "BranchDescr": "CAVITE 3",
                                "BranchId": "4151"
                            },
                            "DateInserted": null,
                            "DatePosted": "11/01/2019",
                            "DatePostedTime": "07:43:44 AM",
                            "Remarks": "H",
                            "StatusandLocation": "Ready for delivery. Please expect delivery within the day.",
                            "TrackingHistoryID": "59055348929"
                        },
                        {
                            "Branch": {
                                "BranchCode": "CTEHA",
                                "BranchDescr": "CAVITE 3",
                                "BranchId": "4151"
                            },
                            "DateInserted": null,
                            "DatePosted": "11/01/2019",
                            "DatePostedTime": "01:43:00 PM",
                            "Remarks": "CLOSE",
                            "StatusandLocation": "We tried to deliver your shipment but house was closed and no one was there. LBC will deliver the next business day.",
                            "TrackingHistoryID": "59092528259"
                        },
                        {
                            "Branch": {
                                "BranchCode": "CTEHA",
                                "BranchDescr": "CAVITE 3",
                                "BranchId": "4151"
                            },
                            "DateInserted": null,
                            "DatePosted": "11/02/2019",
                            "DatePostedTime": "07:41:00 AM",
                            "Remarks": null,
                            "StatusandLocation": "Arrived at  CAVITE 3.",
                            "TrackingHistoryID": "59179670891"
                        },
                        {
                            "Branch": {
                                "BranchCode": "CTEHA",
                                "BranchDescr": "CAVITE 3",
                                "BranchId": "4151"
                            },
                            "DateInserted": null,
                            "DatePosted": "11/02/2019",
                            "DatePostedTime": "07:43:45 AM",
                            "Remarks": "H",
                            "StatusandLocation": "Ready for delivery. Please expect delivery within the day.",
                            "TrackingHistoryID": "59179350234"
                        },
                        {
                            "Branch": {
                                "BranchCode": "CTEHA",
                                "BranchDescr": "CAVITE 3",
                                "BranchId": "4151"
                            },
                            "DateInserted": null,
                            "DatePosted": "11/02/2019",
                            "DatePostedTime": "09:39:00 AM",
                            "Remarks": "(Branch Posting)",
                            "StatusandLocation": "Received by JANETTE ESLABON on 11/02/2019.",
                            "TrackingHistoryID": "59192360077"
                        },
                        {
                            "Branch": {
                                "BranchCode": "FNC01",
                                "BranchDescr": "FINANCE",
                                "BranchId": "4286"
                            },
                            "DateInserted": null,
                            "DatePosted": "11/04/2019",
                            "DatePostedTime": "12:00:00 AM",
                            "Remarks": "ACA-11042019-125355-017794971",
                            "StatusandLocation": "The amount has been remitted to the specified bank account and will be credited within 3 banking days.",
                            "TrackingHistoryID": "61307845702"
                        }
                    ]
                }
            }
        }
    }
}
"""
