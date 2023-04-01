import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1680266862089 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={"paths": ["s3://inputdatapeople/"], "recurse": True},
    transformation_ctx="AmazonS3_node1680266862089",
)

# Script generated for node Change Schema
ChangeSchema_node1680266981480 = ApplyMapping.apply(
    frame=AmazonS3_node1680266862089,
    mappings=[
        ("age", "int", "age", "int"),
        ("job", "string", "job", "string"),
        ("default", "string", "default", "string"),
        ("balance", "int", "balance", "int"),
        ("housing", "string", "housing", "string"),
        ("loan", "string", "loan", "string"),
        ("contact", "string", "contact", "string"),
        ("day", "int", "day", "int"),
        ("month", "string", "month", "string"),
        ("duration", "int", "duration", "int"),
        ("campaign", "int", "campaign", "int"),
        ("pdays", "int", "pdays", "int"),
        ("previous", "int", "previous", "int"),
        ("poutcome", "string", "poutcome", "string"),
        ("term_deposit", "string", "term_deposit", "string"),
    ],
    transformation_ctx="ChangeSchema_node1680266981480",
)

# Script generated for node Amazon S3
AmazonS3_node1680267047299 = glueContext.write_dynamic_frame.from_options(
    frame=ChangeSchema_node1680266981480,
    connection_type="s3",
    format="json",
    connection_options={"path": "s3://outputdatapeople", "partitionKeys": []},
    transformation_ctx="AmazonS3_node1680267047299",
)

job.commit()
