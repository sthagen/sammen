# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/sammen/blob/default/sbom/cdx.json) with SHA256 checksum ([4d3cf4b7 ...](https://git.sr.ht/~sthagen/sammen/blob/default/sbom/cdx.json.sha256 "sha256:4d3cf4b7b75555ddb311d73eaef4e675882ba6e0638b9587476c193c9fe8a279")).
<!--[[[end]]] (checksum: 539b452f7f59d9d43ede6fc321d3330d)-->
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
| Name                                                               | Version                                          | License                              | Author                           | Description (from packaging data)                                                   |
|:-------------------------------------------------------------------|:-------------------------------------------------|:-------------------------------------|:---------------------------------|:------------------------------------------------------------------------------------|
| [anyio](https://github.com/agronholm/anyio/blob/master/README.rst) | [3.6.2](https://pypi.org/project/anyio/3.6.2/)   | MIT License                          | Alex Grönholm                    | High level compatibility layer for multiple asynchronous event loop implementations |
| [idna](https://github.com/kjd/idna)                                | [3.4](https://pypi.org/project/idna/3.4/)        | BSD License                          | Kim Davies <kim@cynosure.com.au> | Internationalized Domain Names in Applications (IDNA)                               |
| [sniffio](https://github.com/python-trio/sniffio)                  | [1.3.0](https://pypi.org/project/sniffio/1.3.0/) | Apache Software License; MIT License | Nathaniel J. Smith               | Sniff out which async library your code is running under                            |
<!--[[[end]]] (checksum: 57a5f64e88d32333fd33e4b8104cae3c)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
watchfiles==0.19.0
└── anyio [required: >=3.0.0, installed: 3.6.2]
    ├── idna [required: >=2.8, installed: 3.4]
    └── sniffio [required: >=1.1, installed: 1.3.0]
````
<!--[[[end]]] (checksum: cc38bb4475567babab2ace802a66da0f)-->
