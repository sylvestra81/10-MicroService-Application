import boto3, json, sys
from datetime import datetime
import uuid

def put_item(service, tool, findings):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('VulnerabilityReports')

    table.put_item(Item={
        'ReportId': str(uuid.uuid4()),
        'ServiceName': service,
        'Tool': tool,
        'Timestamp': datetime.utcnow().isoformat(),
        'Summary': findings
    })

if __name__ == "__main__":
    service = sys.argv[1]
    tool = sys.argv[2]
    report_path = sys.argv[3]

    with open(report_path) as f:
        data = f.read()
        # Keep it simple – you can customize parsing later
        findings = data[:1000]  # Truncate or parse as needed

    put_item(service, tool, findings)
