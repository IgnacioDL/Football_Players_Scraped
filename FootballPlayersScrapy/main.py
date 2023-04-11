# This file calls the spider and saves the players data in a json file.
# Teams from transfermarkt.es have to be added to the team_list variable.

import subprocess

# Chilean first division 2023
team_list = [
        'https://www.transfermarkt.es/csd-colo-colo/startseite/verein/2433',
        'https://www.transfermarkt.es/club-universidad-de-chile/startseite/verein/1037/'
        'https://www.transfermarkt.es/cd-universidad-catolica/startseite/verein/3277/',
        'https://www.transfermarkt.es/union-espanola/startseite/verein/4321/',
        'https://www.transfermarkt.es/huachipato-fc/startseite/verein/6368/',
        'https://www.transfermarkt.es/cdp-curico-unido/startseite/verein/19027/',
        'https://www.transfermarkt.es/union-la-calera/startseite/verein/20514/',
        'https://www.transfermarkt.es/cd-ohiggins/startseite/verein/11470/',
        'https://www.transfermarkt.es/cd-nublense/startseite/verein/14723/',
        'https://www.transfermarkt.es/audax-italiano/startseite/verein/6363/',
        'https://www.transfermarkt.es/cd-everton/startseite/verein/7020/',
        'https://www.transfermarkt.es/cd-cobresal/startseite/verein/17482/',
        'https://www.transfermarkt.es/cd-palestino/startseite/verein/6536/',
        'https://www.transfermarkt.es/coquimbo-unido/startseite/verein/11004/',
        'https://www.transfermarkt.es/magallanes-cf/startseite/verein/13394/',
        'https://www.transfermarkt.es/deportes-copiapo/startseite/verein/20694/'
]

def main():
    rewrite = '-O'
    output_filename = 'chilean_football_players'
    spider = 'football_players'

    subprocess.run(['scrapy', 'crawl', spider, rewrite, f'{output_filename}.json'])


if __name__ == '__main__':
    main()
