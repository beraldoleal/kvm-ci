#!/bin/env python3
"""Basic AWS EC2 Client, testing baremetal instances."""

import boto3


class CIClient:
    def __init__(self):
        self.client = self.connect()

    def connect(self):
        return boto3.client('ec2')

    def start_instances(self, ids):
        return self.client.start_instances(InstanceIds=ids)

    def stop_instances(self, ids, force=False):
        return self.client.stop_instances(InstanceIds=ids,
                                          Force=force)

    def terminate_instances(self, ids):
        return self.client.terminate_instances(InstanceIds=ids)


if __name__ == "__main__":
    ci = CIClient()
    result = ci.terminate_instances(['YOUR INSTANCE ID HERE'])
    print(result)
