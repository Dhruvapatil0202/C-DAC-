import requests

region = input("Enter the region: ").title()
currency_code = input("Enter the currency code: ").upper()

API_link = f"https://restcountries.com/v3.1/currency/{currency_code}"

response = requests.get(API_link)

response_json = response.json()

for country in response_json:
    print("\n")
    print(f"Name of country: {country.get('name').get('common')}")
    print(f"Name of capital: {country.get('capital')[0]}")
    print(f"Area of country: {country.get('area')}")
    print(f"Currency of country: {list(country.get('currencies').keys())[0]}")
    print(f"Region of country: {country.get('region')}")

    # print("\n")