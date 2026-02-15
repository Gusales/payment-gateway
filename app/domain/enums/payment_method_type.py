from enum import Enum

class PaymentMethodType(str, Enum):
    PIX = 'pix'
    BANK_SLIP = 'bank slip'
    CARD = 'card'