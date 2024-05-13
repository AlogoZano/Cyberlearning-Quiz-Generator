from apiclient import discovery
from httplib2 import Http
from oauth2client.service_account import (
    ServiceAccountCredentials
)
import json
from tiro_parabolico import preguntas, opciones, respuestas_correctas



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
        "title": "Tiro parabólico",
        "documentTitle": "Cuestionario Tiro Parabólico",
    }
}

NEW_QUESTION = {
    "requests": [{
        "createItem":{
            "item": {
                "title": preguntas[0],
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": opciones[0][0]},
                                {"value": opciones[0][1]},
                                {"value": opciones[0][2]},
                                {"value": opciones[0][3]}
                            ],
                            "shuffle": False
                        }
                    }
                },

            },
            "location": {
                "index": 0
            }
        },
    },{
        "createItem":{
            "item": {
                "title": preguntas[1],
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": opciones[1][0]},
                                {"value": opciones[1][1]},
                                {"value": opciones[1][2]},
                                {"value": opciones[1][3]}
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
    },{
        "createItem":{
            "item": {
                "title": preguntas[2],
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": opciones[2][0]},
                                {"value": opciones[2][1]},
                                {"value": opciones[2][2]},
                                {"value": opciones[2][3]}
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
    },{
        "createItem":{
            "item": {
                "title": preguntas[3],
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": opciones[3][0]},
                                {"value": opciones[3][1]},
                                {"value": opciones[3][2]},
                                {"value": opciones[3][3]}
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
    },{
        "createItem":{
            "item": {
                "title": preguntas[4],
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": opciones[4][0]},
                                {"value": opciones[4][1]},
                                {"value": opciones[4][2]},
                                {"value": opciones[4][3]}
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
    },{
        "createItem":{
            "item": {
                "title": preguntas[5],
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": opciones[5][0]},
                                {"value": opciones[5][1]},
                                {"value": opciones[5][2]},
                                {"value": opciones[5][3]}
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
    },{
        "createItem":{
            "item": {
                "title": preguntas[6],
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": opciones[6][0]},
                                {"value": opciones[6][1]},
                                {"value": opciones[6][2]},
                                {"value": opciones[6][3]}
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
    },{
        "createItem":{
            "item": {
                "title": preguntas[7],
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": opciones[7][0]},
                                {"value": opciones[7][1]},
                                {"value": opciones[7][2]},
                                {"value": opciones[7][3]}
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
    },{
        "createItem":{
            "item": {
                "title": preguntas[8],
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": opciones[8][0]},
                                {"value": opciones[8][1]},
                                {"value": opciones[8][2]},
                                {"value": opciones[8][3]}
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
    },{
        "createItem":{
            "item": {
                "title": preguntas[9],
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": opciones[9][0]},
                                {"value": opciones[9][1]},
                                {"value": opciones[9][2]},
                                {"value": opciones[9][3]}
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
    },{
        "createItem":{
            "item": {
                "title": preguntas[10],
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": opciones[10][0]},
                                {"value": opciones[10][1]},
                                {"value": opciones[10][2]},
                                {"value": opciones[10][3]}
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
    },{
        "createItem":{
            "item": {
                "title": preguntas[11],
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": opciones[11][0]},
                                {"value": opciones[11][1]},
                                {"value": opciones[11][2]},
                                {"value": opciones[11][3]}
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
    },{
        "createItem":{
            "item": {
                "title": preguntas[12],
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": opciones[12][0]},
                                {"value": opciones[12][1]},
                                {"value": opciones[12][2]},
                                {"value": opciones[12][3]}
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
    },{
        "createItem":{
            "item": {
                "title": preguntas[13],
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": opciones[13][0]},
                                {"value": opciones[13][1]},
                                {"value": opciones[13][2]},
                                {"value": opciones[13][3]}
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
    },{
        "createItem":{
            "item": {
                "title": preguntas[14],
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": opciones[14][0]},
                                {"value": opciones[14][1]},
                                {"value": opciones[14][2]},
                                {"value": opciones[14][3]}
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
    },{
        "createItem":{
            "item": {
                "title": preguntas[15],
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": opciones[15][0]},
                                {"value": opciones[15][1]},
                                {"value": opciones[15][2]},
                                {"value": opciones[15][3]}
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
    },{
        "createItem":{
            "item": {
                "title": preguntas[16],
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": opciones[16][0]},
                                {"value": opciones[16][1]},
                                {"value": opciones[16][2]},
                                {"value": opciones[16][3]}
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
    },{
        "createItem":{
            "item": {
                "title": preguntas[17],
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": opciones[17][0]},
                                {"value": opciones[17][1]},
                                {"value": opciones[17][2]},
                                {"value": opciones[17][3]}
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
    },{
        "createItem":{
            "item": {
                "title": preguntas[18],
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": opciones[18][0]},
                                {"value": opciones[18][1]},
                                {"value": opciones[18][2]},
                                {"value": opciones[18][3]}
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
    },{
        "createItem":{
            "item": {
                "title": preguntas[19],
                "questionItem": {
                    "question": {
                        "required": True,
                        "choiceQuestion": {
                            "type": "RADIO",
                            "options": [
                                {"value": opciones[19][0]},
                                {"value": opciones[19][1]},
                                {"value": opciones[19][2]},
                                {"value": opciones[19][3]}
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
    }
    
    ]
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