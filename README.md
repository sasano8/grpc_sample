# grpc sample

grpcサーバとnginxの構成サンプル。


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

# grpc ４つの通信方式

- Unary RPCs（SimpleRPC): リクエストを送信し、結果を返すだけの最も一般的なRPC
- Server streaming RPC: サーバはクライアントに値を配信し続ける
- Client streaming RPC: サーバはクライアントから値を受け取りづつけます。
- Bidirectional streaming RPC: 相互（クライアント -> サーバ -> クライアント ...）に値を受け取り続けます。


```
service Notification {
  rpc Notification (NotificationRequest) returns (NotificationReply) {}
}

service Notification {
  rpc Notification (NotificationRequest) returns (stream NotificationReply) {}
}

service Notification {
  rpc Notification (stream NotificationRequest) returns (NotificationReply) {}
}

service Notification {
  rpc Notification (stream NotificationRequest) returns (stream NotificationReply) {}
}
```

# grpc gateway

RESTfulHTTPAPIをgRPCに変換するリバースプロキシサーバーを生成する。

- https://github.com/grpc-ecosystem/grpc-gateway