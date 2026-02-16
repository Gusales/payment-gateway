from enum import Enum

class AcceptProviderNames(str, Enum):
    STRIPE = 'STRIPE'
    ABACATE_PAY = 'ABACATE_PAY'
    PAYPAL = 'PAYPAL'
    MOCK = 'MOCK'