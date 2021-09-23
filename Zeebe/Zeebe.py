import time
import os

from robot.api.deco import library, keyword

import grpc
from zeebe_grpc import gateway_pb2, gateway_pb2_grpc


@library(scope='GLOBAL')
class Zeebe:
    WORKER_ID = f'robotframework-camundalibrary-{time.time()}'

    DEFAULT_LOCK_DURATION = None

    def __init__(self, camunda_engine_url: str = 'http://localhost:8080'):
        if camunda_engine_url:
            self.set_camunda_url(camunda_engine_url)
        self.reset_task_lock_duration()

    @keyword("Rest Lock Duration")
    def reset_lock_duration(self):
        self.DEFAULT_LOCK_DURATION = 60000

    @keyword("Deploy")
    def deploy(self, path_model: str, deployment_name: str = ""):
        with grpc.insecure_channel("localhost:26500") as channel:
            stub = gateway_pb2_grpc.GatewayStub(channel)

            if not deployment_name:
                deployment_name = os.path.basename(path_model)

            # deploy a process definition
            with open(path_model, "rb") as process_definition_file:
                process_definition = process_definition_file.read()
                process = gateway_pb2.ProcessRequestObject(
                    name=deployment_name,
                    definition=process_definition
                )

            stub.DeployProcess(
                gateway_pb2.DeployProcessRequest(
                    processes=[process]
                )
            )