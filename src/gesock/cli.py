import click
import tomllib

from wand.image import Image

from gesock import lib


@click.command()
@click.option(
    '--title',
    nargs=2,
    type=click.Tuple([str, click.File('rb')]),
    help="Set the Title along with TOML config file.",
)
@click.option(
    '--url',
    nargs=2,
    type=click.Tuple([str, click.File('rb')]),
    help="Set the Url with required TOML config file.",
)
@click.option(
    '--author',
    nargs=2,
    type=click.Tuple([str, click.File('rb')]),
    help="Set the Author with required TOML config file.",
)
@click.option(
    '--reading_time',
    nargs=2,
    type=click.Tuple([str, click.File('rb')]),
    help="Set the Reading Time with required TOML config file.",
)
@click.option(
    '--date',
    nargs=2,
    type=click.Tuple([str, click.File('rb')]),
    help="Set the Date with required TOML config file.",
)
@click.argument(
    "input_image",
)
@click.argument(
    "output_dir",
    type=click.Path(exists=True, dir_okay=True, file_okay=False),
)
def main(title, url, author, reading_time, date, input_image, output_dir):
    """Generate text on an image using Imagemagick from a template to a new
    image file. Pass in any of the options as a tuple of consistening of a
    message and a path to a TOML config file to style the message string.

    INPUT_IMAGE is a path to a readable image file.

    OUTPUT_DIR is a path to a writable directory where processed images will be
    saved.
    """

    slug = lib.generate_slug(title[0])

    with Image(filename=input_image) as img:
        lib.draw_on_image(img, title)
        lib.draw_on_image(img, url)
        lib.draw_on_image(img, author)
        lib.draw_on_image(img, reading_time)
        lib.draw_on_image(img, date)
        img.save(filename=f'{output_dir}/{slug}.png')
