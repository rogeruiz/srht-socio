#!/bin/bash

###
# This is a quick sketch of what I'm trying to do here. There's nothing
# validating anything so you will need ImageMagick installed along with an
# input image named `social-media-template-blank.jpg`. The variables are also
# all hard-coded and can't be modified from outside. So if you want to change
# the name of the image you can also tweak it from the variables too.
###

input_image='social-media-template-blank.jpg'
output_image="social-${3}"
position_x='+110'
position_y_heading='+164'
position_y_subject='+212'
font_family='Merriweather-Regular'
font_size_heading='28'
font_size_subject='44'

#   -fill '#4c4f69' Dark gray color (1st line, heading)
#   -fill '#8839ef' Bold purple color (2nd line, subject)

# set -o noglob
# IFS=$'\n' txt_display=($1)
# set +o noglob

###
# In the first pass on the image, we'll create the first line (heading). I'm
# doing this because the font size and fill will be different here compared to
# the second line (subject).
###
convert $input_image \
  -font "${font_family}" \
  -pointsize "${font_size_heading}" \
  -fill '#4c4f69' \
  -gravity 'northeast' \
  -annotate "${position_x}${position_y_heading}" "${1}" \
  "${output_image}.tmp.jpg"

convert "${output_image}.jpg" \
  -font "${font_family}" \
  -pointsize "${font_size_subject}" \
  -fill '#8839ef' \
  -gravity 'northeast' \
  -annotate "${position_x}${position_y_subject}" "${2}." \
  "${output_image}.jpg"

rm "${output_image}.tmp.jpg"
