import decimal
from datetime import datetime
from json import JSONEncoder
from uuid import UUID

import json


class Result(JSONEncoder):

    def __init__(self, *args, **kwargs):
        self.message = None
        self.data = None
        self.success = True
        self.error = None

        if len(args) > 0:
            self.message = args[0]
            if len(args) > 1:
                self.data = args[1]
            if len(args) > 2:
                self.success = args[2]
            if len(args) > 3:
                self.error = args[3]

        if len(kwargs) > 0:
            if 'message' in kwargs:
                self.message = kwargs['message']
            if 'data' in kwargs:
                self.data = kwargs['data']
            if 'success' in kwargs:
                self.success = kwargs['success']
            if 'error' in kwargs:
                self.error = kwargs['error'].replace("'", "", 1)

    def to_json(self):
        try:
            return_json = json.dumps(self, default=JsonEncoder, indent=1, ensure_ascii=False)
            return return_json
        except Exception as exc:
            return json.dumps("{'message: 'Erro na conversão do Json', "
                              "success=false, "
                              "data=null, "
                              "error=%s}" % exc.__str__())


def JsonEncoder(o):
    if o is None:
        return ""
    if isinstance(o, datetime):
        return o.__str__()
    if isinstance(o, decimal.Decimal):
        return float(o)
    if isinstance(o, UUID):
        return str(o)
    if hasattr(o, 'args'):
        return str(o.args)
    return o.__dict__

