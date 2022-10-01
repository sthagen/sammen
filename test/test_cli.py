import pathlib

import pytest

import sammen.cli as cli

TEST_PREFIX = pathlib.Path('test', 'fixtures')
DEFAULT_DOCUMENTS_PATH = TEST_PREFIX
TEST_MAKE_MISSING = 'missing-this-file-for-'


def test_parse_request(capsys):
    options = cli.parse_request([])
    assert options == 0  # type: ignore
    out, err = capsys.readouterr()
    assert 'usage: sammen [-h] [--dry-run] [--quiet] [--verbose] families' in out
    assert not err


def test_parse_request_doc_root_option(capsys):
    options = cli.parse_request([f'{DEFAULT_DOCUMENTS_PATH}', '-q', '-d'])
    assert options.families == [str(DEFAULT_DOCUMENTS_PATH)]  # type: ignore
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_parse_request_pos(capsys):
    options = cli.parse_request([f'{DEFAULT_DOCUMENTS_PATH}', '--dry-run'])
    assert options.families == [f'{DEFAULT_DOCUMENTS_PATH}']  # type: ignore
    out, err = capsys.readouterr()
    assert not out
    assert not err


def test_parse_request_pos_doc_root_not_present(capsys):
    with pytest.raises(SystemExit) as err:
        cli.parse_request([f'{TEST_MAKE_MISSING}{DEFAULT_DOCUMENTS_PATH}', '-q', '-v'])
    assert err.value.code == 2
    out, err = capsys.readouterr()
    assert not out
    message_part = 'sammen: error: you cannot be quiet and verbose at the same time'
    assert message_part in err
