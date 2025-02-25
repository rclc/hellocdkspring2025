import aws_cdk as cdk
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_s3_deployment as s3deployment

class HelloCdkStack(cdk.Stack):

    def __init__(self, scope: cdk.App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        bucket = s3.Bucket(self,"MyFirstBucketViaCDK",
                           block_public_access=s3.BlockPublicAccess.BLOCK_ACLS,
                           access_control=s3.BucketAccessControl.BUCKET_OWNER_FULL_CONTROL,
                           public_read_access=True,
                           website_index_document="index.html",
                           versioned=True,
                           removal_policy=cdk.RemovalPolicy.DESTROY,
                           auto_delete_objects=True)
        deployment = s3deployment.BucketDeployment(self,"DeployWebsite",
                                sources=[s3deployment.Source.asset('./hello_cdk/static-website.zip')],
                                destination_bucket=bucket)
        # example resource
        # queue = sqs.Queue(
        #     self, "HelloCdkQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
