"""Dansk for together - multiple watch to ensure special events come together or go away."""
import argparse
import datetime as dti
import logging
import pathlib

from watchfiles import Change, awatch

from sammen import log

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


async def process(options, families, changes) -> None:
    """Correlate and eventually act."""
    primary_present = {primary: pathlib.Path(primary).is_file() for primary in families}
    log.debug(primary_present)
    primary_abs_paths = {str(pathlib.Path(p).resolve()): p for p in primary_present}
    log.debug(primary_abs_paths)
    secondaries = set(secondary for secondaries in families.values() for secondary in secondaries)
    log.debug(secondaries)
    secondaries_abs_paths = {str(pathlib.Path(s).resolve()): s for s in secondaries}
    log.debug(secondaries_abs_paths)
    for file_change in changes:
        log.info(display_change(file_change))
        change, entry = file_change
        if entry in primary_abs_paths:
            if change == Change.deleted:
                for secondary in families[primary_abs_paths[entry]]:
                    if pathlib.Path(secondary).is_file():
                        if options.dry_run:
                            log.info(f'Would remove secondary {secondary} of gone primary {primary_abs_paths[entry]}')
            continue
        if entry in secondaries_abs_paths:
            for primary, secondaries in families.items():
                if any(entry.endswith(secondary) for secondary in secondaries):
                    log.info(f'Affected secondary of primary {primary} in {secondaries_abs_paths[entry]}')


async def main(options: argparse.Namespace) -> int:
    pos_args = options.families
    if options.quiet:
        logging.getLogger().setLevel(logging.ERROR)
    elif options.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    start_time = dti.datetime.now(tz=dti.timezone.utc)
    families = {}
    for csl in pos_args:
        if COMMA not in csl:
            continue
        p, s = csl.split(COMMA, 1)
        xs = set(x.strip() for x in s.strip().split(COMMA))
        families[p] = tuple(sorted(f'{p}{x}' if x.startswith(DOT) else x for x in xs))
    if not families:
        log.error('families should be given as comma separated paths')
        return 2

    log.info(f'Watching for orphaned secondaries of {families}')
    paths = paths_to_watch(families)
    log.debug(f'- set up watchers along the paths {paths}')
    ok, diagnostic = paths_exist(paths)
    if not ok:
        log.error(diagnostic)
        return 1

    try:
        async for changes in awatch(*paths):
            await process(options, families, changes)
    except RuntimeError:
        log.debug('Noisy request handling - preparing termination')
    except KeyboardInterrupt:
        log.debug('Received keyboard interrupt - preparing termination')

    end_time = dti.datetime.now(tz=dti.timezone.utc)
    log.info(f'Orphanage watch complete after {(end_time - start_time).total_seconds()} seconds')
    return 0
