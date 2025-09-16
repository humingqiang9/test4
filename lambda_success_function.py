import json
import random
import string


def lambda_handler(event, context):
    """
    AWS Lambda function that returns a success message.
    
    Args:
        event (dict): AWS Lambda event object
        context (object): AWS Lambda context object
        
    Returns:
        dict: Response object with status code and message
    """
    
    # Generate a random success message ID
    message_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    
    # Return success response
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Success! Lambda function executed successfully.',
            'messageId': message_id,
            'status': 'SUCCESS'
        })
    }


# For local testing
if __name__ == "__main__":
    # Sample event and context for testing
    sample_event = {}
    sample_context = type('obj', (object,), {
        'function_name': 'test_function',
        'function_version': '$LATEST'
    })
    
    result = lambda_handler(sample_event, sample_context)
    print(result)