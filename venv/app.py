import requests
import json

API_KEY ='XCxSuYrc4AsqypAdYX'
resp = '{"error": 0, "draw": "2019-08-31", "results": "14,41,50,56,57,18,5"}'
# r = requests.get(f'https://www.magayo.com/api/results.php?api_key={API_KEY}&game=us_powerball')
req_obj = json.loads(resp)

user_num = input('Type 7 numbers \n')
# user_num_fill = (lambda x: x if len(x) >= 7 else [num if num for num in x else ''])(user_num.split(' '))
try:
    values = [int(num.replace(' ','')) for num in user_num.split(' ')]
    user_num_fill = values if len(values) >= 7 else [val if index != len(values) else '-0--' for index, val in enumerate(values)]

    print(user_num_fill)
    print(len(user_num_fill))
except ValueError:
    print('Invalid input type')

