import requests

url = 'https://raw.githubusercontent.com/manujml/fcfm-datamining036-1954305/main/SISMOS_MEX_1975-2023.csv'
filename = 'SISMOS_MEX_1975-2023.csv'

response = requests.get(url)

if response.status_code == 200:
    with open(filename, 'wb') as local_file:
        local_file.write(response.content)
    print(f'Downloaded {filename}')
else:
    print('download error')