
from huobi.rest.endpoints import HuobiRestClientBase
from huobi.rest.endpoint import Endpoint


class HuobiRestClientQuery(HuobiRestClientBase): 
    deposit_address = Endpoint(
        method='GET',
        path='/v2/account/deposit/address',
        auth_required=True,
        params={
            'currency': {
                'required': True
            },
        },
    )
    
    withdraw_quota = Endpoint(
        method='GET',
        path='/v2/account/withdraw/quota',
        auth_required=True,        
        params={
            'currency': {
                'required': True
            },
        },
    )
    
    withdraw_address = Endpoint(
        method='GET',
        path='/v2/account/withdraw/address',
        auth_required=True,        
        params={
            'currency': {
                'required': True,
            },
        },
    )
    
    withdraw_request = Endpoint(
        method='POST',
        path='/v1/dw/withdraw/api/create',
        auth_required=True,
        params={
            'address': {
                'required': True,
            },
            'currency': {
                'required': True,
            },
            'amount': {
                'required': True,
            },
            'fee': {
                'required': True,
            },
            'chain': {
                'required': False,
            },
            'addr_tag': {
                'required': False,
                'name': 'addr-tag',
            },
            'client_order_id': {
                'required': False,
                'name': 'client-order-id',
            },
        },
    )
    
    withdraw_cancel = Endpoint(
        method='POST',
        path='/v1/dw/withdraw-virtual/{withdraw-id}/cancel',
        auth_required=True,
        params={
            'withdraw_id': {
                'required': True,
                'url': 'withdraw-id',
            },
        },
    )
    
    deposit_withdraw = Endpoint(
        method='GET',
        path='/v1/query/deposit-withdraw',
        auth_required=True,
        params={
            'currency': {
                'required': False,
            },
            'type': {
                'required': True,
                'choices': ['deposit', 'withdraw'],
            },
            'from': {
                'required': False,
                'default': 1,
            },
            'size': {
                'required': False,
                'default': 100,
            },
            'direct': {
                'required': False,
                'choices': ['prev', 'next'],
            },
        },
    )
