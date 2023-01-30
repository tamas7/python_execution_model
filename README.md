# Python Execution Model and Unit Tests

When is specific code actually executed and how is understanding the execution model helps in writing unit tests.

In this imaginary scenario we are working in a serverless application in AWS that is composed of Lambda Functions and Lambda Layers.
Any of these can call out to AWS services using the `boto3` SDK. In our unit tests we'd like to patch these calls, so they don't actually create real connections.

We will walk through some frequently seen scenarios and how to tackle them.


## Scenarios

The `boto3` client/resource is initialised:
1. in the module scope of a Lambda Function
2. in the `lambda_handler` function of a Lambda Function
3. in the module scope of a Lambda Layer
4. as a class variable in a Lambda Layer
5. as an instance variable in a Lambda Layer

