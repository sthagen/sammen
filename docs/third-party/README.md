# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/sammen/blob/default/sbom.json) with SHA256 checksum ([d472012a ...](https://git.sr.ht/~sthagen/sammen/blob/default/sbom.json.sha256 "sha256:d472012add751684eb361237343b8c802f2f4c03ee209e60a20b1cebd4030bb7")).
<!--[[[end]]] (checksum: 17cea444bfdf3157897c42a8b8ca5269)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                                | Version                                               | License     | Author  | Description (from packaging data)                                            |
|:--------------------------------------------------------------------|:------------------------------------------------------|:------------|:--------|:-----------------------------------------------------------------------------|
| [watchfiles](https://github.com/samuelcolvin/watchfiles/watchfiles) | [0.18.1](https://pypi.org/project/watchfiles/0.18.1/) | MIT License | UNKNOWN | Simple, modern and high performance file watching and code reload in python. |
<!--[[[end]]] (checksum: 2970dbc7c43b89a7b0109c7f795e2758)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                              | Version                                          | License                              | Author             | Description (from packaging data)                                                   |
|:--------------------------------------------------|:-------------------------------------------------|:-------------------------------------|:-------------------|:------------------------------------------------------------------------------------|
| [sniffio](https://github.com/python-trio/sniffio) | [1.3.0](https://pypi.org/project/sniffio/1.3.0/) | Apache Software License; MIT License | Nathaniel J. Smith | Sniff out which async library your code is running under                            |
| anyio                                             | [3.6.2](https://pypi.org/project/anyio/3.6.2/)   | MIT License                          | Alex Grönholm      | High level compatibility layer for multiple asynchronous event loop implementations |
| idna                                              | [3.4](https://pypi.org/project/idna/3.4/)        | BSD License                          | UNKNOWN            | Internationalized Domain Names in Applications (IDNA)                               |
<!--[[[end]]] (checksum: 24c4d215b5dd3ae93918621a5909840e)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
watchfiles==0.18.1
  - anyio [required: >=3.0.0, installed: 3.6.2]
    - idna [required: >=2.8, installed: 3.4]
    - sniffio [required: >=1.1, installed: 1.3.0]
````
<!--[[[end]]] (checksum: f6d5438c75dac0921092408dedec3b8f)-->
