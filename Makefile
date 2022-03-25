clean:
	-rm *.css
	-rm -fr *.{html,css}

all: poster.css poster.html poster.pdf

poster: poster.css poster.html poster.pdf

poster.css: poster.less
	lessc --strict-units=on $< $@

poster.html: poster.jinja2 poster.css
	python ./test.py $< $@

poster.pdf: poster.html
	node export.js

.SECONDARY:
