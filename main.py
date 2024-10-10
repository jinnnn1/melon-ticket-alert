import requests

def main() -> None:
    seats = get_seats_summary()
    messages = check_remaining_seats(seats['summary'])
    send_message(messages)

def get_seats_summary() -> None:
    url = "https://ticket.melon.com/tktapi/product/block/summary.json?v=1" 
   
    body = {
        'prodId': '210341',
        'pocCode': 'SC0002',
        'scheduleNo': '100002',
        'perfDate': '',
        'seatGradeNo': '11801',
        'corpCodeNo': ''
    }

    header = {
        'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'Content-Length': '76',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'PCID=17259579986695308673014; _fwb=163NfXqvyjlbAJJSJzhlwE0.1725957999027; PC_PCID=17259579986695308673014; TKT_POC_ID=WP15; NetFunnel_ID=WP15; cbo=0; MAC=48JoY4OXqOljUYd6m8njboP9yN7Mqdr6E2QeJ+UXkSRMKM70gEbdeivh0rJ2dlnulhABD21OoVUkV2Aa5TiOkQ==; MLCP=NTI5MzY5ODglM0IlMjNrYWthb180MjM1NDY1MTg2NTdlbjRjbHklM0IlM0IwJTNCZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKcGMzTWlPaUp0WlcxaVpYSXViV1ZzYjI0dVkyOXRJaXdpYzNWaUlqb2liV1ZzYjI0dGFuZDBJaXdpYVdGMElqb3hOekk0TlRJeE1qRTJMQ0p0WlcxaVpYSkxaWGtpT2lJMU1qa3pOams0T0NJc0ltRjFkRzlNYjJkcGJsbE9Jam9pVGlKOS5aYmpDYnpCUzB4U0d5OVpON1JyenVkMU83b0pabTFGbUd2VjAxeWQxa2dNJTNCJTNCMjAyNDEwMTAwOTQ2NTYlM0IlRUIlODQlQTQlRUMlOTglQTRzazl1eCUzQjElM0JpbnRoZXNreTEyJTQwbmF2ZXIuY29tJTNCMyUzQg==; MUS=-1927794900; keyCookie=52936988; store_melon_cupn_check=52936988; performance_layer_alert=%2C210341; JSESSIONID=2B61D0BB3F7E70DB043D77109CA5FCC4; wcs_bt=s_585b06516861:1728537677',
        'Host': 'ticket.melon.com',
        'Referer': 'https://ticket.melon.com/reservation/popup/stepBlock.htm',
        'User-Agent': 'X'
    }

    response = requests.post(url,headers=header,data=body)
    return response.json()

def check_remaining_seats(seats: list) -> list:
    result = []
    
    for seat in seats:
        if seat['realSeatCntlk'] > 0:
            result.append(generate_message(seat))

    return result

def send_message(messages: list) -> None:
    slack_webhook_url = ""
    for message in messages:
        response = requests.post(slack_webhook_url, json={'text' : message})
   
def generate_message(seat: dict) -> str: 
    return seat['seatGradeName'] + ", " + seat['floorNo'] + seat['floorName'] + " " + seat['areaNo'] + seat['areaName'] + "에 잔여좌석 " + str(seat['realSeatCntlk']) + "개 발생! "

main()
