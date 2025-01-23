import uuid
from datetime import datetime, timedelta

def generate_property_payload():
    return {
        "alias": f"TestsProperty-{uuid.uuid4()}",
        "countryCode": "US"
    }

def generate_booking_payload(property_id, start_date=None, end_date=None):
    start_date = start_date or datetime.now().strftime("%Y-%m-%d")
    end_date = end_date or (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
    return {
        "startDate": start_date,
        "endDate": end_date,
        "status": "SCHEDULED",
        "guest": {
            "firstName": "Yurii",
            "lastName": "Yurii",
            "dateOfBirth": "1992-09-23"
        },
        "propertyId": property_id
    }