import boto3
from botocore.exceptions import ClientError, EndpointConnectionError

def stop_instance_safely(instance_id, region='us-east-1'):
    # Initialize the client
    ec2 = boto3.client('ec2', region_name=region)

    try:
        print(f"Initiating stop for instance: {instance_id}...")
        
        # Using DryRun=True first is a best practice to check permissions
        # without actually stopping the instance.
        ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)

    except ClientError as e:
        # Check if the error was just because DryRun was successful
        if 'DryRunOperation' in str(e):
            try:
                # This is the actual execution
                response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
                print(f"Successfully stopped. Current State: {response['StoppingInstances'][0]['CurrentState']['Name']}")
            except ClientError as final_error:
                print(f"Actual stop failed: {final_error}")
        else:
            # Handle actual errors (Invalid Instance ID, Auth Failure, etc.)
            print(f"Permission or Request Error: {e}")
            
    except EndpointConnectionError:
        print("Network Error: Could not connect to the AWS endpoint. Check your internet/VPN.")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Replace with your actual instance ID
    ID_TO_STOP = 'i-0abcd1234efgh5678'
    stop_instance_safely(ID_TO_STOP)