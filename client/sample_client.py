import grpc
from proto import sample_pb2, sample_pb2_grpc

def hello_server(stub, name):
    messages = []
    messages.append(sample_pb2.HelloMessage(name=name, msg='Hello'))
    responses = stub.HelloServer(iter(messages))
    for response in responses:
        print('Received message {}'.format(response.reply_msg))

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = sample_pb2_grpc.SampleServiceStub(channel)
        print('--Please input your name--')
        while True:
            name = input("What's your name? > ")
            hello_server(stub, name)

