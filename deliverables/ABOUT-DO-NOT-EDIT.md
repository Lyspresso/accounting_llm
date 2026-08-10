# Do not edit anything in this folder by hand.
Every file here is generated on Lydia's machine by `deliver.sh`, which
regenerates STATUS.md with a fresh `generated:` timestamp and copies the
set. If a file looks wrong, the fix happens in the pipeline, then
deliver.sh re-exports. STATUS.md is the live state; everything else is a
reference artifact. Editing here creates a lie that the next export
silently overwrites.
