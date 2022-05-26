"""
class of Huobi restful api client, account related endpoints
"""
from huobi.rest.endpoints import HuobiRestClientBase
from huobi.rest.endpoint import Endpoint


class HuobiRestClientAccounts(HuobiRestClientBase):
    """
    Huobi restful api client
    """

    accounts = Endpoint(
        method='GET',
        path='/v1/account/accounts',
        auth_required=True,
    )

    balance = Endpoint(
        method='GET',
        path='/v1/account/accounts/{account-id}/balance',
        auth_required=True,
        params={
            'account_id': {
                'required': True,
                'url': 'account-id'
            }
        }
    )

    valuation = Endpoint(
        method='GET',
        path='/v2/account/valuation',
        auth_required=True,
        params={
            'accountType': {
                'required': False,
            },
            'valuationCurrency': {
                'required': False,
                'choices': [
                    'BTC',
                ]
            },
        }
    )
    
    asset_valuation = Endpoint(
        method='GET',
        path='/v2/account/asset-valuation',
        auth_required=True,
        params={
            'accountType': {
                'required': True,
                'choices': [
       	            'spot', 
                    'margin', 
                    'otc', 
                    'super-margin',
                ]
            },
            'valuationCurrency': {
                'required': False,
                'choices': [
                    'BTC', 
                    'CNY', 
                    'USD', 
                    'JPY', 
                    'KRW', 
                    'GBP', 
                    'TRY', 
                    'EUR', 
                    'RUB', 
                    'VND', 
                    'HKD', 
                    'TWD', 
                    'MYR', 
                    'SGD', 
                    'AED', 
                    'SAR',
                ]
            },
            'subUid': {
                'required': False,
            },
        }
    )
    
    transfer = Endpoint(
        method='POST',
        path='/v1/account/transfer',
        auth_required=True,
        params={
            'from_user': {
                'required': True,
                'name': 'from-user',
            },
            'from_account_type': {
                'required': False,
                'name': 'from-account-type',
                'choices': [
                    'spot', 
                    'margin',
                ]
            },
            'from_account': {
                'required': True,
                'name': 'from-account',
            },
            'to_user': {
                'required': True,
                'name': 'to-user',
            },
            'to_account_type': {
                'required': False,
                'name': 'to-account-type',
                'choices': [
                    'spot', 
                    'margin',
                ]
            },
            'to_account': {
                'required': True,
                'name': 'to-account',
            },
            'currency': {
                'required': True,
            },
            'amount': {
                'required': True,
            },
        }
    )

    account_history = Endpoint(
        method='GET',
        path='/v1/account/history',
        auth_required=True,
        params={
            'account_id': {
                'required': True,
                'name': 'account-id',
            },
            'currency': {
                'required': False,
            },
            'transact_types': {
                'required': False,
                'name': 'transact-types',
                'multiple': True,
                'choices': [
                    'trade',
                    'etf', 
                    'transact-fee', 
                    'fee-deduction', 
                    'transfer', 
                    'credit', 
                    'liquidation', 
                    'interest', 
                    'deposit', 
                    'withdraw', 
                    'withdraw-fee', 
                    'exchange', 
                    'other-types', 
                    'rebate',
                ]
            },
            'start_time': {
                'required': False,
                'name': 'start-time',
            },
            'end_time': {
                'required': False,
                'name': 'end-time',
            },
            'sort': {
                'required': False,
                'choices': [
                    'asc', 
                    'desc', 
                ]
            },
            'from_id': {
                'required': False,
                'name': 'from-id',
            },
        }
    )
    
    account_ledger = Endpoint(
        method='GET',
        path='/v2/account/ledger',
        auth_required=True,
        params={
            'account_id': {
                'required': True,
                'name': 'account-id',
            },
            'currency': {
                'required': False,
            },
            'start_time': {
                'required': False,
                'name': 'startTime',
            },
            'end_time': {
                'required': False,
                'name': 'endTime',
            },
            'sort': {
                'required': False,
                'choices': [
                    'asc', 
                    'desc', 
                ]
            },
            'limit': {
                'required': False,
                'default': 100,
            },
            'from_id': {
                'required': False,
                'name': 'from-id',
            },
        }
    )
