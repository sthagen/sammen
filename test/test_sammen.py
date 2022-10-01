import sammen.sammen as api


def test_paths_to_watch():
    assert api.paths_to_watch({'a': ('b', 'c')}) == ('.',)


def test_paths_exist():
    assert api.paths_exist(('this-should-not-exist',)) == (False, 'this-should-not-exist is no directory')
