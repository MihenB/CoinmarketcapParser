headers = {
    'authority': 'api.coinmarketcap.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru,en;q=0.9',
    'cache-control': 'no-cache',
    'origin': 'https://coinmarketcap.com',
    'platform': 'web',
    'referer': 'https://coinmarketcap.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Yandex";v="22"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.5005.167 YaBrowser/22.7.5.1027 Yowser/2.5 Safari/537.36',
    'x-request-id': '7d160e841360481c8d98791b83e3bdb5',
}

params = {
    'start': '201',
    'limit': '100',
    'sortBy': 'market_cap',
    'sortType': 'desc',
    'convert': 'USD,BTC,ETH',
    'cryptoType': 'all',
    'tagType': 'all',
    'audited': 'false',
    'aux': 'ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,'
           'volume_7d,volume_30d,self_reported_circulating_supply,self_reported_market_cap',
}

url = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing'

token = '5456637413:AAF2rZuG9EmPhUYAeBJNtRDNr6ID0G8qtD8'
