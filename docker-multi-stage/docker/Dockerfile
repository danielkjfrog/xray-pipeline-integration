FROM python:2.7 as builder

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

ADD src /src

WORKDIR /src

RUN pip install --editable .

ENTRYPOINT [ "hello" ]


FROM alpine:latest  

RUN apk --no-cache add ca-certificates

WORKDIR /root/

COPY --from=builder /usr/local/bin/hello /usr/local/bin/hello

CMD ["hello"]
