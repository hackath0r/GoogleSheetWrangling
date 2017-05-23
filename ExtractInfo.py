from __future__ import print_function
import httplib2
import os

from apiclient import discovery

API_KEY = 'AIzaSyAPGntsL0YhF5WT2OVqmw3U9YsVLB7quEc'

def main():
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                                'version=v4')
    service = discovery.build('sheets', 'v4', developerKey=API_KEY, discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1kw7CagEqxefbeyVfl5hDC0iR3zBoXmKEFERHiNATzZ0'

    rangeName = 'Class Data!A:F'
    result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    print(values)

if __name__ == '__main__':
        main()
