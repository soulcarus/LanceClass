from moveai.providers.lichess import LichessProvider
from moveai.provider import AbstractProvider

lichess = LichessProvider()
abstract_provider = AbstractProvider(lichess)
print(abstract_provider.connect())
print(abstract_provider.classify_game())
print(abstract_provider.classify_move())
