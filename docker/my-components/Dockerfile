ARG PYTHON_VERSION=3.6

FROM registry-vpc.cn-shanghai.aliyuncs.com/shuzhi/suanpan-python-sdk:${PYTHON_VERSION} as builder

ENV PYPI_MIRROR "https://mirrors.aliyun.com/pypi/simple"

RUN pip config set global.index-url ${PYPI_MIRROR}

RUN pip install --upgrade pip

RUN pip install --no-cache-dir pyarmor

WORKDIR /build

COPY . /build

RUN bash tools/compress.sh

FROM registry-vpc.cn-shanghai.aliyuncs.com/shuzhi/suanpan-python-sdk:${PYTHON_VERSION}

WORKDIR /demos

ENV PYPI_MIRROR "https://mirrors.aliyun.com/pypi/simple"

RUN pip config set global.index-url ${PYPI_MIRROR}

RUN pip install --upgrade pip

COPY requirements.txt /demos

RUN pip install -r requirements.txt

COPY --from=builder /build/dist /demos

ENTRYPOINT [ "/sbin/my_init", "--" ]

CMD [ "bash" ]
