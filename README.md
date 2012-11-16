# Markdown to Bulletin Board Code

A custom renderer for Misika that allows you to convert from Markdown to BBCode.

## Requirements

* Misika.

## Usage

    from <this-file> import BBCodeRenderer()
    from misika import Markdown

    renderer = BBCodeRenderer()
    markdown = Markdown(renderer)

    print markdown.render('This is *just* an **example**.')