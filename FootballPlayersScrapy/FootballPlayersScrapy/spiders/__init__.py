# Spider to scrap football players from transfermarkt.es
# Extract players data from teams urls

import scrapy
from datetime import datetime
from main import team_list


class FootballPlayersSpider(scrapy.Spider):
    name = "football_players"
    start_urls = team_list

    def parse(self, response):

        now = datetime.now()
        team = response.css('body div main header div h1::text').get()
        base_url = 'https://www.transfermarkt.es'
        for player in response.css('tr.odd') + response.css('tr.even'):
            
            yield {
                'team' : team[2:].strip(),
                'player_name' : player.css('td.posrela table.inline-table tr td.hauptlink div span.hide-for-small a::text').get(),
                'profile_link' : base_url + player.css('td.posrela table.inline-table tr td.hauptlink div span.hide-for-small a::attr(href)').get(),
                'mini_profile_picture': player.css('td.posrela table.inline-table tr td a img::attr(data-src)').get(),
                'position' : player.css('td.posrela table.inline-table tr td::text').get(),
                'number' : player.css('td.zentriert div.tm-shirt-number::text').get(),
                'birthday' : player.css('td.zentriert::text').get().split(' ')[0],
                'age' : player.css('td.zentriert::text').get().split(' ')[1][1:3],
                'nacionality' : player.css('td.zentriert img.flaggenrahmen::attr(title)').getall(),
                'market_value' : player.css('td.rechts.hauptlink a::text').get(),
                'previous_market_value' : player.css('td.rechts.hauptlink span::attr(title)').get().split(':')[1][1:],
                'market_value_detail_link' : base_url + player.css('td.rechts.hauptlink a::attr(href)').get(),
                'transfer_info' : player.css('td.posrela span.wechsel-kader-wappen a::attr(title)').get(),
                'team_captain' : player.css('td table tr td.hauptlink span.kapitaenicon-table::attr(title)').get(),
                'injury' : player.css('td table tr td.hauptlink span.verletzt-table::attr(title)').get(),
                'scraped_at' : now
            }