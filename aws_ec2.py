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
        ec2.get_waiter('instance_stopped').wait(InstanceIds=[instance_id], WaiterConfig={'Delay': 45, 'MaxAttempts': 40})
        
        print(f"Instance {instance_id} has been stopped successfully.")

    except ClientError as e:
        print(f"ClientError occurred: entering except block with error: {e}")
        # Check if the error was just because DryRun was successful
        if 'DryRunOperation' in str(e):
            try:
                # This is the actual execution
                response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
                ec2.get_waiter('instance_stopped').wait(InstanceIds=[instance_id], WaiterConfig={'Delay': 45, 'MaxAttempts': 40})
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


def create_instance(instance_type='t2.micro', region='us-east-1'):
    ec2 = boto3.client('ec2', region_name=region)
    try:
        print(f"Creating instance of type {instance_type} in {region}...")
        response = ec2.run_instances(
            ImageId=select_ami_id(region),  # Replace with a valid AMI ID
            InstanceType=instance_type,
            MinCount=1,
            MaxCount=1
        )
        instance_id = response['Instances'][0]['InstanceId']
        #ec2.get_waiter('instance_running').wait(InstanceIds=[response['Instances'][0]['InstanceId']])
        # Get the specific waiter
        waiter = ec2.get_waiter('instance_running')
        print("Waiting for instance to start...")
        # Polls every 15 seconds by default
        waiter.wait(InstanceIds=[instance_id], WaiterConfig={'Delay': 45, 'MaxAttempts': 40})
        
        print(f"Instance created with ID: {instance_id}")
        print(response)
        return instance_id
    except ClientError as e:
        print(f"Failed to create instance: {e}")
    except EndpointConnectionError:
        print("Network Error: Could not connect to the AWS endpoint. Check your internet/VPN.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def select_ami_id(region):
    # This function would ideally query AWS for the latest AMI ID based on region and other criteria
    # For demonstration, we return a placeholder AMI ID
    ami_ids = {
        'us-east-1': 'ami-0ec10929233384c7f',
        'us-west-2': 'ami-0fedcba9876543210'
    }
    return ami_ids.get(region, 'ami-0abcdef1234567890')  # Default to a known AMI if region not found

def ec2_terminate_instance(region='us-east-1'):
    ec2 = boto3.resource('ec2', region_name=region)
    try:
        instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running', 'stopped']}])
        for instance in instances:
            print(instance.id, instance.instance_type)
            print(f"Terminating instance: {instance.id}...")
            response = instance.terminate()
            print(f"Termination initiated. Current State: {response['TerminatingInstances'][0]['CurrentState']['Name']}")
            ec2 = boto3.client('ec2', region_name=region)
            ec2.get_waiter('instance_terminated').wait(InstanceIds=[instance.id])
            print(f"Instance {instance.id} has been terminated.")
    except ClientError as e:
        print(f"Failed to terminate instance: {e}")
    except EndpointConnectionError:
        print("Network Error: Could not connect to the AWS endpoint. Check your internet/VPN.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}") 


if __name__ == "__main__":
    # Replace with your actual instance ID
    ID_TO_STOP = 'i-0abcd1234efgh5678'
    stop_instance_safely(create_instance())
    ec2_terminate_instance()