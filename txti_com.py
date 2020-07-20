import requests
import random
import string

possible_chars = string.ascii_letters + string.digits + '-'

def post(**kwargs):
    requests.post('http://txti.es', kwargs)
