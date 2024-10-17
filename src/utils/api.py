#
# https://github.com/mistralai/client-python
#

import os
from mistralai import Mistral

api_key = os.environ["MISTRAL_APIKEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

def ask(question):
    print('asking question..')
