__author__ = 'nishan'

from yelpapi import YelpAPI

key = 'cdKLIdRVUr7vnYnsTWbiIA'
secret = 'gujwKmCVeIRDxB1QiWHCK4FPKiQ'
token = 'npddkfvdPPcQP9JtroXIeo6GaWqPIlWR'
token_secret = 'R9TFAp59AbjY8qtBVs0lwlwww3w'

yelp_api = YelpAPI(key, secret, token, token_secret)

search_results = yelp_api.search_query(limit=1, term='MOMOFUKU SSAM BAR', location='Manhattan')

print search_results