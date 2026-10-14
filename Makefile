PYTHON = python
QUARTO = quarto

.PHONY: all clean

all: data/serena_matches.csv figures/serena_age_plot.png report.html report.pdf

data/SerenaWilliamsCareer.js: scripts/download_data.py
	$(PYTHON) scripts/download_data.py

data/serena_matches.csv: data/SerenaWilliamsCareer.js scripts/clean_data.py
	$(PYTHON) scripts/clean_data.py

figures/serena_age_plot.png: data/serena_matches.csv scripts/plot_serena.py
	$(PYTHON) scripts/plot_serena.py

report.html: report.md figures/serena_age_plot.png
	$(QUARTO) render report.md --to html

report.pdf: report.md figures/serena_age_plot.png
	$(QUARTO) render report.md --to pdf

clean:
	$(PYTHON) -c "from pathlib import Path; [p.unlink() for p in [Path('data/serena_matches.csv'), Path('figures/serena_age_plot.png'), Path('report.html'), Path('report.pdf')] if p.exists()]"