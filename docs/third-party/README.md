# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/sammen/blob/default/sbom/cdx.json) with SHA256 checksum ([0ffb8da1 ...](https://git.sr.ht/~sthagen/sammen/blob/default/sbom/cdx.json.sha256 "sha256:0ffb8da1074179cbcd64b69e58b53ac8dd6938c060e585eabf3a6d2ddbfbb68e")).
<!--[[[end]]] (checksum: fde4ed748a3f824eb23b39f3723d1fc2)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                                | Version                                               | License     | Author                           | Description (from packaging data)                                            |
|:--------------------------------------------------------------------|:------------------------------------------------------|:------------|:---------------------------------|:-----------------------------------------------------------------------------|
| [watchfiles](https://github.com/samuelcolvin/watchfiles/watchfiles) | [0.20.0](https://pypi.org/project/watchfiles/0.20.0/) | MIT License | Samuel Colvin <s@muelcolvin.com> | Simple, modern and high performance file watching and code reload in python. |
<!--[[[end]]] (checksum: 620f5028a7eb3d3a31f3dc4ed191d1b2)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                                | Version                                          | License                              | Author                                   | Description (from packaging data)                                                   |
|:--------------------------------------------------------------------|:-------------------------------------------------|:-------------------------------------|:-----------------------------------------|:------------------------------------------------------------------------------------|
| [anyio](https://anyio.readthedocs.io/en/stable/versionhistory.html) | [3.7.1](https://pypi.org/project/anyio/3.7.1/)   | MIT License                          | Alex Grönholm <alex.gronholm@nextday.fi> | High level compatibility layer for multiple asynchronous event loop implementations |
| [idna](https://github.com/kjd/idna)                                 | [3.4](https://pypi.org/project/idna/3.4/)        | BSD License                          | Kim Davies <kim@cynosure.com.au>         | Internationalized Domain Names in Applications (IDNA)                               |
| [sniffio](https://github.com/python-trio/sniffio)                   | [1.3.0](https://pypi.org/project/sniffio/1.3.0/) | Apache Software License; MIT License | Nathaniel J. Smith                       | Sniff out which async library your code is running under                            |
<!--[[[end]]] (checksum: b45063d8e5ad789c7cb04c114cf26cd6)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
watchfiles==0.20.0
└── anyio [required: >=3.0.0, installed: 3.7.1]
    ├── exceptiongroup [required: Any, installed: 1.1.2]
    ├── idna [required: >=2.8, installed: 3.4]
    └── sniffio [required: >=1.1, installed: 1.3.0]
````
<!--[[[end]]] (checksum: 0c033e74befcb35ca9c11291a7c0d307)-->
