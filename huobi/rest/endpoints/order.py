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
                'name': 'account-id',
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
                    'buy-ioc',
                    'sell-ioc',
                    'buy-limit-maker',
                    'sell-limit-maker',
                    'buy-stop-limit',
                    'sell-stop-limit',
                    'buy-limit-fok',
                    'sell-limit-fok',
                    'buy-stop-limit-fok',
                    'sell-stop-limit-fok',
                ],
            },
            'amount': {
                'required': True,
            },
            'price': {
                'required': False,
            },
            'source': {
                'required': False,
                 'choices': [
                    'spot-api',
                    'margin-api',
                    'super-margin-api',
                    'c2c-margin-api',
                 ],
            },
            'client_order_id': {
                'required': False,
                'name': 'client-order-id',
            },
            'self_match_prevent': {
                'required': False,
                'name': 'self-match-prevent',
            },
            'operator': {
                'required': False,
                 'choices': [
                    'gte',
                    'lte',
                 ],
            },
        }
    )


    order_cancel = Endpoint(
        method='POST',
        path='/v1/order/orders/{order-id}/submitcancel',
        auth_required=True,
        params={
            'order_id': {
                'required': True,
                'url': 'order-id',
            },
            'symbol': {
                'required': False,
            },
        },
    )

    cancel_all_after = Endpoint(
        method='POST',
        path='/v2/algo-orders/cancel-all-after',
        auth_required=True,
        params={
            'timeout': {
                'required': True,
            },
        },
    )

    order_detail = Endpoint(
        method='GET',
        path='/v1/order/orders/{order-id}',
        auth_required=True,
        params={
            'order_id': {
                'required': True,
                'url': 'order-id',
            },
        },
    )

    order_id = Endpoint(
        method='GET',
        path='/v1/order/orders/{order-id}/matchresults',
        auth_required=True,
        params={
            'order_id': {
                'required': True,
                'url': 'order-id',
            },
        },
    )

    order_client = Endpoint(
        method='GET',
        path='/v1/order/orders/getClientOrder',
        auth_required=True,
        params={
            'clientOrderId': {
                'required': True,
            },
        },
    )

    order_history = Endpoint(
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
                ],
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
                'multiple': True,
                'choices': [
                    'filled',
                    'partial-canceled',
                    'canceled',
                ],
            },
            'from': {
                'required': False,
            },
            'direct': {
                'required': False,
                'choices': [
                    'prev',
                    'next'
                ],
            },
            'size': {
                'required': False,
            },
        },
    )

    order_open = Endpoint(
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
                ],
            },
            'from': {
                'required': False,
            },
            'direct': {
                'required': False,
                'choices': ['prev','next']
            },
            'size': {
                'required': False,
            },
        },
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
                ],
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
                    'next',
                ],
            },
            'size': {
                'required': False,
            },
        }
    )
