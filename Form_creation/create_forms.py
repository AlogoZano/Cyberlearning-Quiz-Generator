from apiclient import discovery
from httplib2 import Http
from oauth2client.service_account import (
    ServiceAccountCredentials
)

from googleapiclient.discovery import build
import json



SCOPES = "https://www.googleapis.com/auth/forms.body"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

creds = ServiceAccountCredentials.from_json_keyfile_name(
    'credentials.json',
    SCOPES
)

http = creds.authorize(Http())

form_service = discovery.build(
    'forms',
    'v1',
    http=http,
    discoveryServiceUrl=DISCOVERY_DOC,
    static_discovery=False

)

NEW_FORM = {
    "info": {
        "title": "2D Kinematics: Projectile Motion",
    }
}

NEW_QUESTION = {
    "requests": [{
        "createItem":{
            "item": {
                "title": "Which of the following statements best describes the trajectory of a projectile launched horizontally?",
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": "The height of the projectile always increases"},
                                {"value": "The horizontal velocity of the projectile remains constant."},
                                {"value": "The vertical acceleration of the projectile is equal to gravity."},
                                {"value": "The vertical velocity of the projectile is always zero."}
                            ],
                            "shuffle": False
                        }
                    }
                },
                
            },
            "location": {
                "index": 0
            }
        }
    }]
}


result = form_service.forms().create(
    body=NEW_FORM
).execute()

question_setting = form_service.forms(    
).batchUpdate(
    formId=result["formId"],
    body=NEW_QUESTION
).execute()

get_result = form_service.forms().get(
    formId=result["formId"]
).execute()

print(json.dumps(get_result, indent=4))