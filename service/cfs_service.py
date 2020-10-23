from flask import current_app
import random
import requests

class CFSService:

    def call(self)-> int:
        """calls CFS api"""
        response = requests.get(current_app.config['CFS_API_ENDPOINT'])
        return response.status_code

    @property
    def bv_category(self) -> str:
        """get"""
        buckets = ['A1', 'A2', 'A3', 'D1']
        return random.choice(buckets)   
    
    