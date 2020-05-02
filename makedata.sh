docker run --rm -v $(pwd):/dst -w /dst python:3.7-alpine sh -c \
"pip install -q -i https://pypi.tuna.tsinghua.edu.cn/simple pyyaml && python makedata.py"