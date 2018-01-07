TARGET=notes
PREFIX=/usr/local/bin/
SOURCES=notes.py

all:
	@echo "No build step required; type 'make install' or 'make uninstall' to continue"

make_file:
	touch ~/.daily_log

install: make_file
	install $(SOURCES) $(PREFIX)$(TARGET)

uninstall:
	rm -rf $(PREFIX)$(TARGET)
