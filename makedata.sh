docker run --rm -v ${pwd}:/root -w /root python:3.7-alpine pip install -q -i https://pypi.tuna.tsinghua.edu.cn/simple \
pyyaml && python makedata.py