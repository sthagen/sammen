# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://github.com/sthagen/pilli/blob/default/sbom.json) with SHA256 checksum ([539a7e81 ...](https://raw.githubusercontent.com/sthagen/pilli/default/sbom.json.sha256 "sha256:539a7e816b9417c769e0d645a657ef7f140ffab86772a225f7be0e661b5a78a8")).
<!--[[[end]]] (checksum: ee8b5c7606d1df107f2171d5827f1562)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name       | Version                                               | License     | Author  | Description (from packaging data)                                            |
|:-----------|:------------------------------------------------------|:------------|:--------|:-----------------------------------------------------------------------------|
| watchfiles | [0.17.0](https://pypi.org/project/watchfiles/0.17.0/) | MIT License | UNKNOWN | Simple, modern and high performance file watching and code reload in python. |
<!--[[[end]]] (checksum: f995c59636a3df23e6c008c3bff857f7)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name | Version | License | Author | Description (from packaging data) |
|:-----|:--------|:--------|:-------|:----------------------------------|
<!--[[[end]]] (checksum: 8a87b89207db0be2864af66f9266660c)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
watchfiles==0.17.0
  - anyio [required: >=3.0.0,<4, installed: 3.6.1]
    - idna [required: >=2.8, installed: 3.4]
    - sniffio [required: >=1.1, installed: 1.3.0]
````
<!--[[[end]]] (checksum: daff0e1bba9cd14cdaf0a8cc9330e57d)-->
