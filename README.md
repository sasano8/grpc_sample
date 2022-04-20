
https://grpc.io/docs/languages/python/basics/

```
pyenv install 3.8.12
pyenv local 3.8.12
poetry install
```

```
# cd examples/protos
python -m grpc_tools.protoc --python_out=grpc_sample/grpc --grpc_python_out=grpc_sample/grpc -I protos protos/route_guide.proto
```


1. serverを立てる
2. nginxでhttp1.1のリバースプロキシを立てる
3. nginxでhttp2.0のリバースプロキシを立てる

