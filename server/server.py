from concurrent import futures
import logging
import grpc

import four_grpc_modes_pb2_grpc as my_grpc
import four_grpc_modes_pb2 as my_pb

logging.basicConfig(format='%(asctime)s:%(name)s : %(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)


class Four_Modes(my_grpc.FourModesServicer):
    def UnaryAPI(self, request, context):
        log.info("Unary API")
        log.info(f"Requests - {request}")
        # print(dir(request))
        # ['ByteSize', 'Clear', 'ClearExtension', 'ClearField', 'CopyFrom', 'DESCRIPTOR', 'DiscardUnknownFields', 'Extensions', 'FindInitializationErrors', 'FromString', 'HasExtension', 'HasField', 'IsInitialized', 'ListFields', 'MergeFrom', 'MergeFromString', 'ParseFromString', 'RegisterExtension', 'SerializePartialToString', 'SerializeToString', 'SetInParent', 'UnknownFields', 'WhichOneof', '_CheckCalledFromGeneratedFile', '_SetListener', '__class__', '__deepcopy__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__unicode__', '_extensions_by_name', '_extensions_by_number', 'request_purpose']
        res = my_pb.Response(response="Unary Response is here!")
        log.info(f"Response - {res}")
        return res

    def ServerStreamingAPI(self, request, context):
        log.info("ServerStreaming API")
        log.info(f"Request - {request}")
        for i in range(10):
            res = my_pb.Response(response=f"Stream Response : {i + 1}")
            log.info(f"Response - {res}")
            yield res

    def ClientStreamingAPI(self, request_iterator, context):
        log.info("Client Streaming API")
        for r in request_iterator:
            log.info(f"Request - {r}")

        res = my_pb.Response(response="Response for your stream requests")
        log.info(f"Response - {res}")
        return res

    def BiDirectionalStreamingAPI(self, request_iterator, context):
        log.info("Bi-Directional Streaming API")
        for r in request_iterator:
            log.info(f"Request - {r}")
            res = my_pb.Response(response=f"Response for your stream requests : {r.request_purpose}")
            log.info(f"Response - {res}")
            yield res



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    my_grpc.add_FourModesServicer_to_server(Four_Modes(), server)
    socket = 'localhost:50051'
    server.add_insecure_port(socket)
    server.start()
    log.debug(f"Started the server and Listening at {socket}")
    server.wait_for_termination()
    # The server start() method is non-blocking. 
    # A new thread will be instantiated to handle requests. 
    # The thread calling server.start() will often not have any other work to do in the meantime. 
    # In this case, you can call server.wait_for_termination() to cleanly block 
    # the calling thread until the server terminates.


if __name__ == '__main__':
    serve()
