import requests
from requests.auth import HTTPBasicAuth

# Your KORONA.cloud account ID
korona_account_id = "dd0b749a-56f5-4185-a782-590230a8530f"

# API endpoint for adding products
url = f"https://167.koronacloud.com/web/api/v3/accounts/{korona_account_id}/products"

# Your credentials for Basic Authentication
username = "support"
password = "support"

# The new product to add
product = [
    ##product number/assortment
  {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "number": "00000001",
    "assortment": {
      "name": "General Assortment",
    },
    ##UPC
    "codes": [
      {
        "productCode": "SP0015184",
        "containerSize": 1,
        "description": "SmartphoneModelX"
      }
    ],
    ## commodityGroup
    "commodityGroup": {
      "name": "Ticketing",
    },
    "conversion": False,
    "costs": 250,
    "deactivated": False,
    "deposit": False,
    "discountable": True,
    ##LAST PP
    "lastPurchasePrice": 200,
    "listed": True,
    "listedSince": "2023-01-01T09:40:21+01:00",
    #MAX & MIN PRICE
    "maxPrice": 9999,
    "minPrice": -9999,
    #PRODUCT NAME
    "name": "Hot New Product",
    "packagingQuantity": 1,
    "packagingRequired": False,
    "packagingUnit": "CUBIC_INCH",
    "personalizationRequired": False,
    "priceChangable": False,
    ##prodcut prices
   # "prices": [
 # {
   # "value": 1000,
 #   "organizationalUnit": {
  #    "name": "Default",
  #    "number": "1"
  #  }
 # },
 # {
  #  "value": 1000,
  #  "productCode": "1245788745",
   # "priceGroup": {
   #   "number": "1"
   # },
 # }
#],
    "printTicketsSeparately": False,
    #"recommendedRetailPrice": 275,
    "sector": {
      "name": "General",
      "number": "1"
    },
    "serialNumberRequired": False,
    "trackInventory": True,
    #"containerCapacity": 1,
    #"independentSubarticleDiscounts": False,
    #"stockReturnUnsellable": False
  }
]

# Send a POST request to the API endpoint
response = requests.post(url, json=product, auth=HTTPBasicAuth(username, password))

# Check the response
if response.status_code == 200:
    print("Product added successfully", response.text)
else:
    print("Failed to add product. Status code:", response.status_code)
    print("Response:", response.text)
