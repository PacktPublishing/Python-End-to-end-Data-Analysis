.SUFFIXES: .py .png

TARGETS = \
	annotate.png \
	axis.png \
	bar.png \
	better.png \
	contour.png \
	df.png \
	histogram.png \
	intro.png \
	legends.png \
	line.png \
	linestyle.png \
	matlab.png \
	morelegends.png \
	nox.png \
	pandasplot.png \
	scatter.png \
	series.png \
	subplot.png \
	subs.png \

all: $(TARGETS)

.py.png:
	python $<

clean:
	rm -f *.png
