# braze-python-sdk

The SDK is unofficial and is still under development.

## Example

### Create the SDK instance
```PYTHON
from json import dumps

from braze import Braze

YOUR_HOST = "https://..."
YOUR_TOKEN = "12345678-1234-1234-1234-123456789012"

braze = Braze(
    host=YOUR_HOST,
    token=YOUR_TOKEN
)
```

### Call /users/track endpoint
```PYTHON
track_response = braze.users.track(
    content={
        "attributes": [
            {
                "external_id": "hello-world",
                "first_name": "Hello world"
            }
        ]
    }
)

print(dumps(track_response, indent=True))
# Console output
# {
#   "attributes_processed": 1,
#   "message": "success"
# }
```

### Call /users/delete endpoint
```PYTHON
delete_response = braze.users.delete(
    content={
        "external_ids": [
            "hello-world"
        ]
    }
)

print(dumps(delete_response, indent=True))
# Console output
# {
#   "deleted": 1,
#   "message": "success"
# }
```