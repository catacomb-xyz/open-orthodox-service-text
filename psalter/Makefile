all:
	git show -s --format=%as > date.tex
	git rev-parse --short HEAD > hash.tex
	xelatex -halt-on-error psalter.tex

hardbreak:
	xelatex -halt-on-error psalter-hardbreak.tex

clean:
	rm -rf psalter.aux psalter.log psalter.pdf
	rm -rf psalter-hardbreak.aux psalter-hardbreak.log psalter-hardbreak.pdf
