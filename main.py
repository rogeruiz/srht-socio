from textwrap import wrap
from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image


def word_wrap(image, ctx, text, roi_width, roi_height):
    """Break long text to multiple lines, and reduce point size
    until all text fits within a bounding box."""
    mutable_message = text
    iteration_attempts = 100

    def eval_metrics(txt):
        """Quick helper function to calculate width/height of text."""
        metrics = ctx.get_font_metrics(image, txt, True)
        return (metrics.text_width, metrics.text_height)

    while ctx.font_size > 0 and iteration_attempts:
        iteration_attempts -= 1
        width, height = eval_metrics(mutable_message)
        if height > roi_height:
            ctx.font_size -= 0.75  # Reduce pointsize
            mutable_message = text  # Restore original text
        elif width > roi_width:
            columns = len(mutable_message)
            while columns > 0:
                columns -= 1
                mutable_message = "\n".join(wrap(mutable_message, columns))
                wrapped_width, _ = eval_metrics(mutable_message)
                if wrapped_width <= roi_width:
                    break
            if columns < 1:
                ctx.font_size -= 0.75  # Reduce pointsize
                mutable_message = text  # Restore original text
        else:
            break
    if iteration_attempts < 1:
        raise RuntimeError("Unable to calculate word_wrap for " + text)
    return mutable_message


# TODO: Bring in these variables as `--flags` from the command line. These will
# be `--msg`, `--time`, `--author`, `--date`, and `--url`. This means that I
# will need some string templates for things like the `byline` variable.
message = """Using Nix with Exercism"""
byline = """Reading time: 9 minutes
By: Roger Steve Ruiz"""
dateLine = "01 Feb 2023"
urlLine = "https://write.rog.gr/writing/using-nix-with-exercism"

# TODO: Set x, y and px, py as an object to make it easier to understand and
# get rid of magic numbers

xTitle = 850  # 80
yTitle = 300  # 200

xInfo = 700  # 80
yInfo = 80  # 400

xDate = 300  # 80
yDate = 50  # 560

xUrl = 1120  # 80
yUrl = 50  # 80

# TODO: Support using `latte` or `mocha` as the input image.
with Image(filename="social-media-template-latte.png") as img:
    with Drawing() as ctx:
        ctx.fill_color = Color("#1e66f5")
        ctx.font_family = "FantasqueSansM Nerd Font"
        ctx.text_interline_spacing = 0
        ctx.font_size = 26
        mutable_byline = word_wrap(img, ctx, urlLine, xUrl, yUrl)
        ctx.text(80, 110, mutable_byline)
        ctx.draw(img)
    with Drawing() as ctx:
        ctx.fill_color = Color("#8839ef")
        ctx.font_family = "Playfair Display"
        ctx.font_style = "normal"
        ctx.font_weight = 700
        ctx.text_interline_spacing = -25
        ctx.font_size = 80
        mutable_message = word_wrap(img, ctx, message, xTitle, yTitle)
        ctx.text(80, 250, mutable_message)
        ctx.draw(img)
    with Drawing() as ctx:
        ctx.fill_color = Color("#8c8fa1")
        ctx.font_family = "Quattrocento"
        ctx.text_interline_spacing = 0
        ctx.font_size = 30
        mutable_byline = word_wrap(img, ctx, byline, xInfo, yInfo)
        ctx.text(80, 400, mutable_byline)
        ctx.draw(img)
    with Drawing() as ctx:
        ctx.fill_color = Color("#dc8a78")
        ctx.font_family = "Quattrocento"
        ctx.font_weight = 700
        ctx.font_size = 30
        mutable_byline = word_wrap(img, ctx, dateLine, xDate, yDate)
        ctx.text(80, 540, mutable_byline)
        ctx.draw(img)

    img.save(filename="social-media-template-latte-done.png")
