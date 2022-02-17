'''
Temporary File with currency info, meant to provide functionality before databases are implemented.
Eventually this information will be retrieved through the API and stored in the database.
'''

currencies = {
    'btc': {
        'id':'bitcoin',
        'symbol':'btc',
        'name':'Bitcoin',
    },
    'eth':{
        'id':'ethereum',
        'symbol':'eth',
        'name':'Ethereum'
    },
    'lrc':{
        'id':'loopring',
        'symbol':'lrc',
        'name':'Loopring'
    },
    'cro':{
        'id':'crypto-com-chain',
        'symbol':'cro',
        'name':'Crypto.com Coin'
    },
    'sol':{
        'id':'solana',
        'symbol':'sol',
        'name':'Solana'
    }
}