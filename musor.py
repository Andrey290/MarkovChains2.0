import json
import sys

a = {'сt4рt': {
    'variants': ['современная'], 'современная': [1, 1.0]
},
    'современная': {
        'variants': ['война'], 'война': [1, 1.0]
    },
    'война': {
        'variants': ["3nD"],
        "3nD": [1, 1.0]
    }
}


with open('memory.json', 'w') as output_file:
    json.dump(a, output_file)
