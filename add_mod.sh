docker run --rm -v $(pwd):/dst -w /dst python:3.7-alpine sh -c \
"python ./src/add_mod.py $*"