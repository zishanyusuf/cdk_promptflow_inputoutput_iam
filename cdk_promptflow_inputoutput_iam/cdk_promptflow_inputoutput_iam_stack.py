from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_iam as iam,
    aws_bedrock as bedrock
)
from constructs import Construct

class CdkPromptflowInputoutputIamStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkPromptflowInputoutputIamQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        # Define the IAM policy for the Bedrock Flow
        bedrock_flow_policy = iam.PolicyStatement(
            actions=["bedrock:CreateFlow", "bedrock:UpdateFlow"],
            resources=["*"],
            effect=iam.Effect.ALLOW,
        )

        # Create the IAM role for the Bedrock Flow
        bedrock_flow_role = iam.Role(
            self,
            "BedrockFlowRole",
            assumed_by=iam.ServicePrincipal("bedrock.amazonaws.com"),
            role_name="BedrockInputOutputFlowRole",
            description="IAM role for Bedrock Flow",
            inline_policies={
                "BedrockFlowPolicy": iam.PolicyDocument(statements=[bedrock_flow_policy])
            },
        )

        cfn_flow = bedrock.CfnFlow(self, "MyCfnFlow",
                                   execution_role_arn=bedrock_flow_role.role_arn,
                                   #execution_role_arn="arn:aws:iam::471112580598:role/service-role/AmazonBedrockExecutionRoleForFlows_SL6VMJWYW9",
                                   name="demo_cdk_promptflow_input_output_iam",

                                   #Define nodes and connections here
                                   definition=bedrock.CfnFlow.FlowDefinitionProperty(
                                        #Adding conections and experimenting with it    
                                        connections=[bedrock.CfnFlow.FlowConnectionProperty(
                                            name="Input_Output_Connections",
                                            source="InputNode",
                                            target="OutputNode",
                                            type="Data",
                                            # the properties below are optional
                                            configuration=bedrock.CfnFlow.FlowConnectionConfigurationProperty(
                                                # conditional=bedrock.CfnFlow.FlowConditionalConnectionConfigurationProperty(
                                                #     condition="condition"
                                                #     ),
                                                    data=bedrock.CfnFlow.FlowDataConnectionConfigurationProperty(
                                                        source_output="document",
                                                        target_input="document"
                                                        )
                                                )
                                            )], 

                                        nodes=[
                                           bedrock.CfnFlow.FlowNodeProperty(
                                               name="InputNode",
                                               type="Input",
                                            #    inputs=[
                                            #        bedrock.CfnFlow.FlowNodeInputProperty(
                                            #            #expression="$.input.text",
                                            #            expression="$.data",
                                            #            name="document",
                                            #            type="String"
                                            #            )],
                                                outputs=[
                                                    bedrock.CfnFlow.FlowNodeOutputProperty(
                                                                   name="document",
                                                                   type="String"
                                                                   )
                                                ]),
                                            bedrock.CfnFlow.FlowNodeProperty(
                                                name="OutputNode",
                                                type="Output",
                                                inputs=[
                                                   bedrock.CfnFlow.FlowNodeInputProperty(
                                                       #expression="$.input.text",
                                                       expression="$.data",
                                                       name="document",
                                                       type="String"
                                                       )]
                                                #        ,
                                                # outputs=[
                                                #     bedrock.CfnFlow.FlowNodeOutputProperty(
                                                #         name="document",
                                                #         type="String"
                                                #         )]
                                            )
                                            ]),
                                          

                                    
                                    description="description",
                                    tags={
                                            "tags_key": "tags"
                                            },
                                    test_alias_tags={
                                        "test_alias_tags_key": "testAliasTags"
                                        }
)
