from enum import Enum

class PaymentMethodType(str, Enum):
    PIX = 'PIX'
    BANK_SLIP = 'BANK_SLIP'
    CARD = 'CARD'