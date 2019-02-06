# mkdocs-bootstrap-tables-plugin

This plugin adds a "markdown" template filter to mkdocs.

## Setup

Install the plugin using pip:

`pip install mkdocs-markdown-filter`

Activate the plugin in `mkdocs.yml`:
```yaml
plugins:
  - search
  - markdown-filter
```

> **Note:** If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set, but now you have to enable it explicitly.

More information about plugins in the [MkDocs documentation][mkdocs-plugins].

## Usage

Enabling this plugin will filter jinja template code through a markdown filter:

    {% set code_content %}
    ```php linenums="1"
    <?php
    foo = 1;
    bar = 3;
    if (foo == bar ) {
      // do something 
    }
    ?>
    ```
    {% endset %}
    {{ code_content|markdown }}

## See Also

More information about templates [here][mkdocs-template].

More information about blocks [here][mkdocs-block].

[mkdocs-plugins]: http://www.mkdocs.org/user-guide/plugins/
[mkdocs-template]: https://www.mkdocs.org/user-guide/custom-themes/#template-variables
[mkdocs-block]: https://www.mkdocs.org/user-guide/styling-your-docs/#overriding-template-blocks
