import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from constants import RECIPIENTS  # Import the RECIPIENTS list

# Initialize a session using Amazon SES
ses_client = boto3.client('ses', region_name='us-east-1')

# Specify the sender's email address
SENDER = "sender@example.com"
AWS_REGION = "us-east-1"

# The subject line for the email
SUBJECT = "Amazon SES Test"

# The email body for recipients with non-HTML email clients
BODY_TEXT = ("Amazon SES Test\r\n"
             "This email was sent with Amazon SES using the "
             "AWS SDK for Python (Boto3)."
             )

# The HTML body of the email
BODY_HTML = """<html>
<head></head>
<body>
  <h1>Amazon SES Test</h1>
  <p>This email was sent with
    <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
    <a href='https://boto3.amazonaws.com/v1/documentation/api/latest/index.html'>AWS SDK for Python (Boto3)</a>.</p>
</body>
</html>
           """

# The character encoding for the email
CHARSET = "UTF-8"

# Iterate over the recipient list and send an email to each
for email in RECIPIENTS:
    try:
        # Provide the contents of the email
        response = ses_client.send_email(
            Destination={
                'ToAddresses': [email],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
        print(f"Email sent to {email}! Message ID: {response['MessageId']}")
    except NoCredentialsError:
        print("Credentials not available")
    except PartialCredentialsError:
        print("Incomplete credentials provided")
    except Exception as e:
        print(f"Error sending email to {email}: {e}")
