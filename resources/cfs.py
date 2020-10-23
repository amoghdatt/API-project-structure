from flask_restful import Resource
from flask import Response
from cfs.schemas import accept_schema
from cfs.service import cfs_service as cfs
from cfs.service import decision_service as ds

class CFS(Resource):

    def get(self):
        return {"message":cfs.bv_category}

    def post(self) -> Response:
        decision = ds.get_decision(cfs.bv_category)
        return Response(accept_schema.dump(),
                        status=200,
                        mimetype='application/json')

