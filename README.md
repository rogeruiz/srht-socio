# Socio

Socio is a Python CLI tool that can be used to generate social media images for
use in the Open Graph Protocol. It uses TOML configuration files to pass
parameters to ImageMagick to overlay text onto a provided image template. It is
configured to output to a single directory which contains the new images.

This CLI tool is most useful for generating multiple unique Open Graph images
that can be used for each unique post on a blog or specific pages of a website.

The TOML configuration has the following schema to set various style attributes
to best customize the layout and typography for a given input string.

```toml
x_position = 0
y_position = 0
max_width = 0
max_height = 0
color = ""

[font]
family = ""
style = ""
size = 0
leading = 0
weight = 0
```

## Installation

This project uses *Nix* and `direnv` for setting up the development environment
using `.venv`. This may change in the future. Currently the project needs to be
constructed from source. The provided `shell.nix` can leverage `direnv` to
create an environment to build the project locally and install it as a Python
module on your system.

## Contributing

Contributions are welcome. Please reach out to me via email if you have any
questions.

## Simple usage

```sh
gesock \
  --title 'Title you want to use' tmp/configs/title.toml \
  --url 'https://example.com/url-you-want/to-have/on-top/' tmp/configs/url.toml \
  --author 'by Author Name' tmp/configs/author.toml \
  --reading_time 'reading time: 9 minutes' tmp/configs/reading_time.toml \
  --date '01 Jan 2006' tmp/configs/date.toml \
  tmp/template.png tmp/
```

The `--title` flag above is also used to create the end filename for the output
image. The extension of the template is used to create the extension on the
created files as well. Currently there is no flag to set a filename for the
new file.

## Integration in CI

**Coming Soon**: This section will discuss how to use this tool when using a
static-site generator to build out these images dynamically after the site has
been built.
