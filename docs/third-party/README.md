# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://github.com/sthagen/pilli/blob/default/sbom.json) with SHA256 checksum ([089355df ...](https://raw.githubusercontent.com/sthagen/pilli/default/sbom.json.sha256 "sha256:089355dfc41c7b30ff4f1df8d4ab80cfe29e423481653508b6a98f41e677d16a")).
<!--[[[end]]] (checksum: 6bca1e164482ae526e9784fb8c608fe4)-->
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
| Name                                          | Version                                        | License     | Author         | Description (from packaging data)         |
|:----------------------------------------------|:-----------------------------------------------|:------------|:---------------|:------------------------------------------|
| [click](https://palletsprojects.com/p/click/) | [8.1.3](https://pypi.org/project/click/8.1.3/) | BSD License | Armin Ronacher | Composable command line interface toolkit |
<!--[[[end]]] (checksum: dc3a866a7aa3332404bde3da87727cb9)-->

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
