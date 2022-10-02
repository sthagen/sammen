# Usage

## Help

```console
❯ sammen
usage: sammen [-h] [--dry-run] [--quiet] [--verbose] families [families ...]

Dansk for together - multiple watch to ensure special events come together or go away.

positional arguments:
  families       comma separated lists of families.

options:
  -h, --help     show this help message and exit
  --dry-run, -d  only log what would be done - no real actions (default: False)
  --quiet, -q    work as quiet as possible (default: False)
  --verbose, -v  work logging more information along the way (default: False)
```

## Examples

```console
❯ sammen -d test/fixtures/tmp/x,.sha256 test/fixtures/brazil/b,.md5,.gpg
2022-10-02T04:59:18.086407+00:00 INFO [SAMMEN]: Watching for orphaned secondaries of {'test/fixtures/tmp/x': ('test/fixtures/tmp/x.sha256',), 'test/fixtures/brazil/b': ('test/fixtures/brazil/b.gpg', 'test/fixtures/brazil/b.md5')} dry-run (no changes)
^C2022-10-02T04:59:19.318535+00:00 INFO [SAMMEN]: Orphanage watch complete after 1.232447 seconds
```

Background and dry-run mode:

```console
❯ sammen -d test/fixtures/tmp/x,.sha256 test/fixtures/brazil/b,.md5,.gpg &
[1] 12450
2022-10-02T04:59:45.076946+00:00 INFO [SAMMEN]: Watching for orphaned secondaries of {'test/fixtures/tmp/x': ('test/fixtures/tmp/x.sha256',), 'test/fixtures/brazil/b': ('test/fixtures/brazil/b.gpg', 'test/fixtures/brazil/b.md5')} dry-run (no changes)

❯ touch test/fixtures/brazil/b
2022-10-02T04:59:57.265855+00:00 INFO [watchfiles.main]: 1 change detected
2022-10-02T04:59:57.266150+00:00 INFO [SAMMEN]: Entry(/some/where/test/fixtures/brazil/b): ADD

❯ md5sum test/fixtures/brazil/b > test/fixtures/brazil/b.md5
2022-10-02T05:00:15.203083+00:00 INFO [watchfiles.main]: 1 change detected
2022-10-02T05:00:15.203321+00:00 INFO [SAMMEN]: Entry(/some/where/test/fixtures/brazil/b.md5): ADD

❯ echo "amended" >> test/fixtures/brazil/b
2022-10-02T05:00:36.340749+00:00 INFO [watchfiles.main]: 1 change detected
2022-10-02T05:00:36.340972+00:00 INFO [SAMMEN]: Entry(/some/where/test/fixtures/brazil/b): MOD

❯ md5sum test/fixtures/brazil/b > test/fixtures/brazil/b.md5
2022-10-02T05:00:41.812928+00:00 INFO [watchfiles.main]: 1 change detected
2022-10-02T05:00:41.813168+00:00 INFO [SAMMEN]: Entry(/some/where/test/fixtures/brazil/b.md5): ADD

❯ rm test/fixtures/brazil/b
2022-10-02T05:00:48.878645+00:00 INFO [watchfiles.main]: 1 change detected
2022-10-02T05:00:48.878875+00:00 INFO [SAMMEN]: Entry(/some/where/sammen/test/fixtures/brazil/b): DEL
2022-10-02T05:00:48.878911+00:00 INFO [SAMMEN]: Would remove secondary test/fixtures/brazil/b.gpg of gone primary test/fixtures/brazil/b
2022-10-02T05:00:48.878937+00:00 INFO [SAMMEN]: Would remove secondary test/fixtures/brazil/b.md5 of gone primary test/fixtures/brazil/b

❯ kill %1
[1]  + terminated  sammen -d test/fixtures/tmp/x,.sha256 ...
```

Background and default mode (deleting orphaned secondary files):

```console
❯ sammen test/fixtures/tmp/x,.sha256 test/fixtures/brazil/b,.md5,.gpg &
[1] 13246
2022-10-02T05:04:58.200583+00:00 INFO [SAMMEN]: Watching for orphaned secondaries of {'test/fixtures/tmp/x': ('test/fixtures/tmp/x.sha256',), 'test/fixtures/brazil/b': ('test/fixtures/brazil/b.gpg', 'test/fixtures/brazil/b.md5')}

❯ touch test/fixtures/brazil/b
2022-10-02T05:05:06.978603+00:00 INFO [watchfiles.main]: 1 change detected
2022-10-02T05:05:06.978941+00:00 INFO [SAMMEN]: Entry(/some/where/test/fixtures/brazil/b): ADD

❯ md5sum test/fixtures/brazil/b > test/fixtures/brazil/b.md5
2022-10-02T05:05:12.539863+00:00 INFO [watchfiles.main]: 1 change detected
2022-10-02T05:05:12.540124+00:00 INFO [SAMMEN]: Entry(/some/where/test/fixtures/brazil/b.md5): MOD

❯ echo "amended" >> test/fixtures/brazil/b
2022-10-02T05:05:18.070990+00:00 INFO [watchfiles.main]: 1 change detected
2022-10-02T05:05:18.071205+00:00 INFO [SAMMEN]: Entry(/some/where/test/fixtures/brazil/b): MOD

❯ md5sum test/fixtures/brazil/b > test/fixtures/brazil/b.md5
2022-10-02T05:05:23.953829+00:00 INFO [watchfiles.main]: 1 change detected
2022-10-02T05:05:23.954042+00:00 INFO [SAMMEN]: Entry(/some/where/test/fixtures/brazil/b.md5): MOD

❯ touch test/fixtures/brazil/b.gpg
2022-10-02T05:05:40.493237+00:00 INFO [watchfiles.main]: 1 change detected
2022-10-02T05:05:40.493457+00:00 INFO [SAMMEN]: Entry(/some/where/test/fixtures/brazil/b.gpg): MOD

❯ touch test/fixtures/brazil/b.keep
2022-10-02T05:05:51.365025+00:00 INFO [watchfiles.main]: 1 change detected
2022-10-02T05:05:51.365261+00:00 INFO [SAMMEN]: Entry(/some/where/test/fixtures/brazil/b.keep): ADD

❯ rm test/fixtures/brazil/b
2022-10-02T05:05:59.298175+00:00 INFO [watchfiles.main]: 1 change detected
2022-10-02T05:05:59.298394+00:00 INFO [SAMMEN]: Entry(/some/where/test/fixtures/brazil/b): DEL
2022-10-02T05:05:59.299086+00:00 INFO [SAMMEN]: Removed secondary test/fixtures/brazil/b.gpg of gone primary test/fixtures/brazil/b
2022-10-02T05:05:59.299601+00:00 INFO [SAMMEN]: Removed secondary test/fixtures/brazil/b.md5 of gone primary test/fixtures/brazil/b
2022-10-02T05:05:59.410061+00:00 INFO [watchfiles.main]: 2 changes detected
2022-10-02T05:05:59.410417+00:00 INFO [SAMMEN]: Entry(/some/where/test/fixtures/brazil/b.gpg): DEL
2022-10-02T05:05:59.410461+00:00 INFO [SAMMEN]: Entry(/some/where/test/fixtures/brazil/b.md5): DEL

❯ kill %1
[1]  + terminated sammen test/fixtures/tmp/x,.sha256 test/fixtures/brazil/b,.md5,.gpg
```
