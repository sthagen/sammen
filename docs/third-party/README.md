# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/sammen/blob/default/sbom/cdx.json) with SHA256 checksum ([352b8de6 ...](https://git.sr.ht/~sthagen/sammen/blob/default/sbom/cdx.json.sha256 "sha256:352b8de6d01eda6ac9fd66b5ac17ca96b14dc4b925d595d6de065bb3b24de020")).
<!--[[[end]]] (checksum: 609f60431232be4ddefabd51eb693408)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                                | Version                                               | License     | Author                           | Description (from packaging data)                                            |
|:--------------------------------------------------------------------|:------------------------------------------------------|:------------|:---------------------------------|:-----------------------------------------------------------------------------|
| [watchfiles](https://github.com/samuelcolvin/watchfiles/watchfiles) | [0.19.0](https://pypi.org/project/watchfiles/0.19.0/) | MIT License | Samuel Colvin <s@muelcolvin.com> | Simple, modern and high performance file watching and code reload in python. |
<!--[[[end]]] (checksum: 033f2e9e2e846e0d984b2f1f5d8f7bab)-->

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
watchfiles==0.19.0
└── anyio [required: >=3.0.0, installed: 3.7.1]
    ├── exceptiongroup [required: Any, installed: 1.1.2]
    ├── idna [required: >=2.8, installed: 3.4]
    └── sniffio [required: >=1.1, installed: 1.3.0]
````
<!--[[[end]]] (checksum: c21dec1246d993f4ca124923db546bc5)-->
