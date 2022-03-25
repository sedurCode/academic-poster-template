# A template for (more) accessible posters, using HTML+CSS

Modern HTML+CSS is more than enough for most academic posters:

- No more fighting with LaTeX+Beamer or PowerPoint/LibreOffice.
- It works on computers, tablets, and mobile devices.
- Readers can adjust the font size trivially.
- It's much more accessible than PDFs.

![template logo](/img/logo.svg)

See it in action [on a real example](https://cpitclaudel.github.io/academic-poster-template/koika/poster.html) and [follow the tutorial](https://cpitclaudel.github.io/academic-poster-template/tutorial/poster.html) to create your own posters.

# Setting Up

- ``conda env create -f environment.yml``
- ``conda activate poster``
- ``npm install -g less``
- ``npm install -g puppeteer``
- modify poster.jinja2 and poster.less as desired
- ``make clean && make all``

# Sources
This repo builds off the original repo [link text itself](https://github.com/cpitclaudel/academic-poster-template) and [this fork](https://github.com/observingClouds/academic-poster-template) that adds the javascript for pdf and png of generation of the poster