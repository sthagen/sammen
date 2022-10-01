# [[[fill git_describe()]]]
__version__ = '2022.9.25+parent.4d7d73be'
# [[[end]]] (checksum: 0fe1fb4dccaae23b681874e6f995ea65)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
__all__: list[str] = []
