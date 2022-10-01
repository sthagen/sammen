import asyncio
import pathlib
import sys
from typing import Union

from watchfiles import Change, awatch

COMMA = ','
DOT = '.'


def paths_to_watch(families: dict[str, tuple[str, ...]]) -> tuple[str, ...]:
    """Extract the minimal spanning paths to watch."""
    path_set = set()
    for primary, secondaries in families.items():
        path_set.add(str(pathlib.Path(primary).parent))
        for secondary in secondaries:
            path_set.add(str(pathlib.Path(secondary).parent))

    paths: set[str] = set()
    for path in sorted(path_set):
        if not paths or path not in paths and str(pathlib.Path(path).parent) not in paths:
            paths.add(path)

    return tuple(sorted(paths))


def paths_exist(paths: tuple[str, ...]) -> tuple[bool, str]:
    """First error or all good."""
    for path in paths:
        folder = pathlib.Path(path)
        if not folder.is_dir():
            return False, f'{folder} is no directory'
    return True, ''


def display_change(file_change: tuple[Change, str]) -> str:
    """Temporary debugging dryness helper."""
    change, entry = file_change
    disp = 'ADD' if change == Change.added else ('MOD' if change == Change.modified else 'DEL')
    return f'Entry({entry}): {disp}'


async def main(argv: Union[list[str], None] = None) -> int:
    if argv is None:
        argv = sys.argv[1:]
    if not argv:
        print('usage: trial.py csnames', file=sys.stderr)
        return 2
    print(argv)
    families = {}
    for csl in argv:
        if COMMA not in csl:
            continue
        p, s = csl.split(COMMA, 1)
        xs = set(x.strip() for x in s.strip().split(COMMA))
        families[p] = tuple(sorted(f'{p}{x}' if x.startswith(DOT) else x for x in xs))
    if not families:
        print('usage: trial.py groups-of-comma-separated-names', file=sys.stderr)
        return 2

    print(f'Watching for orphaned secondaries in {families}')
    paths = paths_to_watch(families)
    print(f'Along the paths {paths}')
    ok, diagnostic = paths_exist(paths)
    if not ok:
        print(diagnostic, file=sys.stderr)
        return 1

    async for changes in awatch(*paths):
        print('# --- triggered ---')
        for file_change in changes:
            change, entry = file_change
            if any(entry.endswith(f) for fs in families.values() for f in fs):
                print(f'Affected secondary in {entry}')
            print(display_change(file_change))

    return 0


asyncio.run(main(argv=sys.argv[1:]))
