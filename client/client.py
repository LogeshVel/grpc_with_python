import logging
import grpc

import four_grpc_modes_pb2_grpc as my_grpc
import four_grpc_modes_pb2 as my_pb

logging.basicConfig(format='%(asctime)s:%(name)s : %(message)s', level=logging.DEBUG)
log = logging.getLogger(__name__)

socket = 'localhost:50051'
channel = grpc.insecure_channel(socket)
client = my_grpc.FourModesStub(channel)
log.info(f"Connected to the Server : {socket}")


def make_unary_request(request_string: str):
    log.info("Making Unary Request")
    pb_req = my_pb.Request(request_purpose=request_string)
    log.info(f"Request - {pb_req}")
    u_res = client.UnaryAPI(pb_req)
    log.info(f"Response - {u_res}")


def make_server_streaming_request(request_string: str):
    log.info("making Server Streaming Request")
    pb_req = my_pb.Request(request_purpose=request_string)
    log.info(f"Request - {pb_req}")
    # for response in client.ServerStreamingAPI(pb_req):
    #     log.info(f"Response - {response}")
    ### Both works
    res = client.ServerStreamingAPI(pb_req)
    for r in res:
        log.info(f"Response - {r}")


def make_client_streaming_request(request_string_list: list):
    log.info("Making Client Streaming request")
    pb_req_list = []
    for req_str in request_string_list:
        pb_req_list.append(my_pb.Request(request_purpose=req_str))
    log.info(f"Request - {pb_req_list}")
    cs_res = client.ClientStreamingAPI(pb_req_list.__iter__())
    log.info(f"Response - {cs_res}")


def make_bidirectional_stream_request(request_string_list: list):
    log.info("Making Bi-Directional Streaming request")
    pb_req_list = []
    for req_str in request_string_list:
        pb_req_list.append(my_pb.Request(request_purpose=req_str))
    log.info(f"Request - {pb_req_list}")
    for bi_res in client.BiDirectionalStreamingAPI(pb_req_list.__iter__()):
        log.info(f"Response - {bi_res}")


make_unary_request("Unary request!")

make_server_streaming_request("Need stream response")

make_client_streaming_request(["Client stream 1", "client stream 2", "Client Stream 3"])

make_bidirectional_stream_request(["Bi-Directional req stream 1", "Bi-Directional req  stream 2"])
