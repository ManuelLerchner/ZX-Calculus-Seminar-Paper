# Makefile for LaTeX project

# The name of the main .tex file (without the .tex extension)
MAIN = zx_calculus

# Commands to run LaTeX
LATEX = pdflatex
BIBTEX = bibtex

# Run pdflatex and bibtex multiple times to resolve references
all:
	$(LATEX) $(MAIN).tex
	$(BIBTEX) $(MAIN).aux
	$(LATEX) $(MAIN).tex
	$(LATEX) $(MAIN).tex

# Clean up intermediate files
clean:
	rm -f *.log *.aux *.bbl *.blg *.toc *.out *.pdf