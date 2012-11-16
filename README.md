# Markdown to Bulletin Board Code

A custom renderer for Misaka that allows you to convert from Markdown to BBCode.

## Requirements

* Misaka.

## Usage

    from <this-file> import BBCodeRenderer
    from misaka import Markdown

    renderer = BBCodeRenderer()
    markdown = Markdown(renderer)

    print markdown.render('This is *just* an **example**.')
