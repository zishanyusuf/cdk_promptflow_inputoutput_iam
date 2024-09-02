import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_promptflow_inputoutput_iam.cdk_promptflow_inputoutput_iam_stack import CdkPromptflowInputoutputIamStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_promptflow_inputoutput_iam/cdk_promptflow_inputoutput_iam_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkPromptflowInputoutputIamStack(app, "cdk-promptflow-inputoutput-iam")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
