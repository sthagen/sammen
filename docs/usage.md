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
❯ python -m sammen test/fixtures/brazil/b,.md5 test/fixtures/tmp/a,.sha -d
2022-10-01T17:34:35.461245+00:00 INFO [SAMMEN]: Watching for orphaned secondaries of {'test/fixtures/brazil/b': ('test/fixtures/brazil/b.md5',), 'test/fixtures/tmp/a': ('test/fixtures/tmp/a.sha',)}
^C2022-10-01T17:34:36.697649+00:00 INFO [SAMMEN]: Orphanage watch complete after 1.236843 seconds
```

```console
❯ sammen test/fixtures/brazil/b,.md5 test/fixtures/tmp/a,.sha -d &
[1] 14738
❯ 2022-10-01T17:36:11.383665+00:00 INFO [SAMMEN]: Watching for orphaned secondaries of {'test/fixtures/brazil/b': ('test/fixtures/brazil/b.md5',), 'test/fixtures/tmp/a': ('test/fixtures/tmp/a.sha',)}
❯ touch test/fixtures/brazil/b test/fixtures/brazil/b.md5
2022-10-01T17:36:30.422671+00:00 INFO [watchfiles.main]: 2 changes detected
2022-10-01T17:36:30.422770+00:00 INFO [SAMMEN]: Affected secondary in /Users/ruth/d/gh/sha/src/sammen/test/fixtures/brazil/b.md5
2022-10-01T17:36:30.422799+00:00 INFO [SAMMEN]: Entry(/Users/ruth/d/gh/sha/src/sammen/test/fixtures/brazil/b.md5): ADD
❯ kill %1
[1]  + terminated  sammen test/fixtures/brazil/b,.md5 test/fixtures/tmp/a,.sha -d
```
