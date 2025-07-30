import boto3
from botocore.exceptions import ClientError

# Initialize the SES client
ses = boto3.client('ses', region_name='us-east-1')  # Change to your region

def sendEmail(recipients, alarm_server, alarm_type):
    """
    Send alert to Global IT and project distribution list
    """
    if alarm_type == "disk space":
        alarm_type = "D Drive Disk space"
    elif alarm_type == "cpu":
        alarm_type = "CPU"
    else:
        alarm_type = alarm_type.capitalize()

    subject = f"{alarm_server} - {alarm_type} above 80%"
    body_html = f"""<h2>Hello,</h2>
    <p>The EC2 instance <b>{alarm_server}</b> currently has {alarm_type} utilization above 80%.
    <br>Please connect to EC2 console to get more details.</p>
    <p>GlobalIT</p>"""

    # Create the raw email
    raw_email = f"""From: aws@intellimind.com
To: {", ".join(recipients)}
Subject: {subject}
X-Priority: 1
Importance: High
MIME-Version: 1.0
Content-Type: text/html; charset=UTF-8

{body_html}
"""

    try:
        response = ses.send_raw_email(
            RawMessage={
                'Data': raw_email,
            }
        )

    except ClientError as e:
        print(e.response["Error"]["Message"])
    else:
        print("Email sent! Message ID:", response["MessageId"])

# Example usage
recipients = ["recipient@example.com"]
sendEmail(recipients, "my-ec2-instance", "cpu")