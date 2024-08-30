import urllib.parse

secret_key = 'spaceships_and_rockets707'

mysql_username = 'imir'

# using to encode the password since the password has an '@' symbol in it
mysql_password = urllib.parse.quote_plus('Stephanie@77')

mysql_path = f'mysql://root:{mysql_password}@localhost/anime_data'