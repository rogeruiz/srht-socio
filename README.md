# Generating Social Media Open Graph Images

This project exists to generate social media images for open graph images using
custom text, custom font, and a template image. The first iteration is a simple
Bash script that leverages ImageMagick. Eventually, the idea here is to have a
Python CLI tool which can automatically determine the height and width for a
given space in the provided image template and automatically resize the text
passed in. **Watch this space for more exciting things to come**.

This project depends on ImageMagick to load up a template and takes two strings
of text to place that text with a particular font and color all submitted on the
command-line.

The initial work for this was inspired with a simple shell script which takes
two strings with hard-coded colors, placement, and font attributes using the
`convert` CLI tool from ImageMagick. The goal of this work is to create an
automated system for displaying social media open graph images for Hugo posts
using the title and the author's name so that all posts have a custom text area
to help with interactions on social media posts. The names of the output images
will be the slug that Hugo uses. Because of the dependence on Hugo posts
specifically, there will need to be some documentation around how to configure
Hugo in order to leverage this tool in a CI/CD pipeline for Hugo sites so when
things get shared on social media the `og:image` is relevant to the page that's
being shared. This can be leverage for more than social media posts with a
custom Hugo template or partial which builds out the necessary structure to pass
into this tool.

This tool is will need to have some basic knowledge of how Hugo sites are
created in order to update the paths for the build step in the Hugo SSG process.
