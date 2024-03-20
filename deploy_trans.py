# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:25:36 2024

@author: aritr
"""

input_text = "This is a sample text to translate."

import requests

#url = "http://127.0.0.1:8000/translation"
url = "https://mbart-translator-f86b423c2fc6.herokuapp.com/translation"

data = {"lang": input_text}

response = requests.post(url, json=data)


if response.status_code == 200:
    result = response.json()
    print("Hindi:", result["Hindi"])
    print("Bangla:", result["Bangla"])
else:
    print("Error:", response.status_code)
    print("Detail:", response.text)