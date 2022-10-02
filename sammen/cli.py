"""CLI interface for overlap (Finnish: limitys) assesses sentences from constrained and overlapping vocabularies."""
import argparse
import asyncio
import sys
from typing import List, Union

import sammen.sammen as api
from sammen import APP_ALIAS, APP_NAME, log


def parse_request(argv: List[str]) -> Union[int, argparse.Namespace]:
    """DRY."""
    parser = argparse.ArgumentParser(
        prog=APP_ALIAS, description=APP_NAME, formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        'families',
        nargs='+',
        default='',
        help='comma separated lists of families.',
    )
    parser.add_argument(
        '--dry-run',
        '-d',
        dest='dry_run',
        default=False,
        action='store_true',
        help='only log what would be done - no real actions (default: False)',
    )
    parser.add_argument(
        '--quiet',
        '-q',
        dest='quiet',
        default=False,
        action='store_true',
        help='work as quiet as possible (default: False)',
    )
    parser.add_argument(
        '--verbose',
        '-v',
        dest='verbose',
        default=False,
        action='store_true',
        help='work logging more information along the way (default: False)',
    )
    if not argv:
        parser.print_help()
        return 0

    options = parser.parse_args(argv)

    if options.verbose and options.quiet:
        parser.error('you cannot be quiet and verbose at the same time')

    if not options.families:
        parser.error('we need families to watch')

    return options


def main(argv: Union[List[str], None] = None) -> int:
    """Delegate processing to functional module."""
    argv = sys.argv[1:] if argv is None else argv
    options = parse_request(argv)
    if isinstance(options, int):
        return 0
    try:
        asyncio.run(api.main(options))
    except RuntimeError:
        log.debug('Received run time error in CLI - terminating')
    except KeyboardInterrupt:
        log.debug('Received keyboard interrupt in CLI - terminating')
    except Exception as err:
        log.warning(f'Received {err} in CLI - terminating')
    return 0
