from django.dispatch import Signal

object_veiwed_signal = Signal(providing_args=['instance', 'request'])