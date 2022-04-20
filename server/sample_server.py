import time
from concurrent import futures
import grpc
from proto import sample_pb2, sample_pb2_grpc

class SampleServiceServicer(sample_pb2_grpc.SampleServiceServicer):

    def __init__(self):
        pass

    def HelloServer(self, request_iterator, context):
        for new_msg in request_iterator:
            reply_msgs = []
            print('Receive new message! [name: {}, msg: {}]'.format(new_msg.name, new_msg.msg))
            reply_msgs.append(sample_pb2.ReplyMessage(reply_msg='{} {}'.format(new_msg.msg, new_msg.name)))
            reply_msgs.append(sample_pb2.ReplyMessage(reply_msg='Nice to meet you!!!'))
            for message in reply_msgs:
                yield message

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sample_pb2_grpc.add_SampleServiceServicer_to_server(SampleServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Starting gRPC sample server...')
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)

