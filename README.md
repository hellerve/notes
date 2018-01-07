# notes

A simple note-taking utility, inspired by [this beautiful article by Peter
Lyons](https://peterlyons.com/leveling-up#your-work-journal).
It will write all of your musings to a file called `~/.daily_log`. Currently
no project-specific note-taking is possible or planned.

## Installation

`notes` unpythonically chooses to be installed via `make`. The relevant command
is `make install`. It will set you up. `notes` is written in Python, and a
Python interpreter is required on your `$PATH`. Python 2 and 3 should both
work.

## Usage

`notes` has three major modes: `edit`, `show`, and `dump`.

The `edit` mode will be entered by typing `notes edit`, which will open your
favorite editor as determined by the `$EDITOR` path variable—defaulting to
`vi`, noone’s favorite editor. In it, you can write notes to your hearts
content. After you’re done, save the file and exit. The contents of that file
will be appended to the log, with an added date.

`dump` mode—the other writing mode—will be entered by typing `notes
<anything not starting with edit or dump>`. It will take any arguments supplied
and dump them into your log file verbatim. This means you can use it like so:

```bash
$ notes i restarted the server and found out it has trouble rebooting on its own
```

The prefixed date helps you localize it.

The `show` mode will just dump the file as-is. Protip: use `less` or a similar
utility to make sense of this mess.

<hr/>

Have fun!
