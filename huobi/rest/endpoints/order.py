"""
class of Huobi restful api client, order related endpoints
"""
import datetime
from huobi.rest.endpoints import HuobiRestClientBase
from huobi.rest.endpoint import Endpoint


def date_formatter(d):
    if isinstance(d, datetime.datetime):
        return d.date().isoformat()
    if isinstance(d, datetime.date):
        return d.isoformat()
    if isinstance(d, str):
        return d


class HuobiRestClientOrder(HuobiRestClientBase):

    place = Endpoint(
        method='POST',
        path='/v1/order/orders/place',
        auth_required=True,
        params={
            'account_id': {
                'required': True,
                'name': 'account-id'
            },
            'amount': {
                'required': True,
            },
            'price': {
                'required': False,
            },
            'source': {
                'required': False,
            },
            'symbol': {
                'required': True
            },
            'type': {
                'required': True,
                'choices': [
                    'buy-market',
                    'sell-market',
                    'buy-limit',
                    'sell-limit',
                ]
            },
        }
    )

    submit_cancel = Endpoint(
        method='POST',
        path='/v1/order/orders/{order-id}/submitcancel',
        auth_required=True,
        params={
            'order_id': {
                'required': True,
                'url': 'order-id'
            }
        }
    )

    batch_cancel = Endpoint(
        method='POST',
        path='/v1/order/orders/batchcancel',
        auth_required=True,
        params={
            'order_ids': {
                'required': True,
                'name': 'order-ids',
                'type': list
            }
        }
    )

    order_detail = Endpoint(
        method='GET',
        path='/v1/order/orders/{order-id}',
        auth_required=True,
        params={
            'order_id': {
                'required': True,
                'url': 'order-id'
            }
        }
    )

    order_id = Endpoint(
        method='GET',
        path='/v1/order/orders/{order-id}/matchresults',
        auth_required=True,
        params={
            'order_id': {
                'required': True,
                'url': 'order-id'
            }
        }
    )

    client_order = Endpoint(
        method='GET',
        path='/v1/order/orders/getClientOrder',
        auth_required=True,
        params={
            'clientOrderId': {
                'required': True,
            }
        }
    )

    order_state = Endpoint(
        method='GET',
        path='/v1/order/orders',
        auth_required=True,
        params={
            'symbol': {
                'required': True,
            },
            'types': {
                'required': False,
                'multiple': True,
                'choices': [
                    'buy-market',
                    'sell-market',
                    'buy-limit',
                    'sell-limit',
                    'buy-ioc', 
                    'sell-ioc', 
                    'buy-stop-limit', 
                    'sell-stop-limit', 
                    'buy-limit-fok', 
                    'sell-limit-fok', 
                    'buy-stop-limit-fok', 
                    'sell-stop-limit-fok',
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
            'states': {
                'required': True,
                'choices': [
                    'filled', 
                    'partial-canceled', 
                    'canceled',
                    'filled,partial-canceled,canceled',
                    'filled,canceled',
                    'partial-canceled,canceled',
                    'filled,partial-canceled',
                ]
            },
            'from': {
                'required': False,
            },
            'direct': {
                'required': False,
                'choices': [
                    'prev',
                    'next'
                ]
            },
            'size': {
                'required': False,
            }
        }
    )

    open_order = Endpoint(
        method='GET',
        path='/v1/order/openOrders',
        auth_required=True,
        params={
            'account_id': {
                'required': False,
                'name': 'account-id',
            },
            'symbol': {
                'required': False,
            },
            'side': {
                'required': False,
                'choices': [
                    'buy', 'sell'
                ]
            },
            'from': {
                'required': False,
            },
            'direct': {
                'required': False,
                'choices': [
                    'prev',
                    'next'
                ]
            },
            'size': {
                'required': False,
            }
        }
    )
    order_symbol = Endpoint(
        method='GET',
        path='/v1/order/matchresults',
        auth_required=True,
        params={
            'symbol': {
                'required': True,
            },
            'types': {
                'required': False,
                'multiple': True,
                'choices': [
                    'buy-market',
                    'sell-market',
                    'buy-limit',
                    'sell-limit',
                    'buy-ioc',
                    'sell-ioc',
                    'buy-limit-maker', 
                    'sell-limit-maker', 
                    'buy-stop-limit', 
                    'sell-stop-limit',
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
            'from': {
                'required': False,
            },
            'direct': {
                'required': False,
                'choices': [
                    'prev',
                    'next'
                ]
            },
            'size': {
                'required': False,
            }
        }
    )
