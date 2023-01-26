from flask import request
from flask_restplus import Namespace, Resource, fields,abort,reqparse
from rpn_api.core.rpn import Rpn
import logging
import json

rpn = Rpn()

# namespace
rpn_api = Namespace('rpn', description='rpn methods')
# api resource model
rpn_model = rpn_api.model('RpnSchema', {
    'total': fields.String(required=True, description='The inputs name')
})

def rpn_required():
    rpn_required = rpn_api.clone('RpnRequiredSchema',rpn_model)
    return rpn_required
rpn_required = rpn_required()


@rpn_api.route('/',endpoint='rpn')
class RpnResource(Resource):

    @rpn_api.doc('rpn_operation')
    @rpn_api.expect(rpn_required)
    @rpn_api.marshal_with(rpn_model, code=200,skip_none=True)
    def post(self):
        ''' New operation '''
        operands = rpn_api.payload
        rpn.push(operands['total'])
        operands['total']=rpn.get_status()
        return operands

    @rpn_api.doc('rpn_operation')
    @rpn_api.expect(rpn_required)
    @rpn_api.marshal_with(rpn_model, code=200,skip_none=True)
    def put(self):
        ''' Add an element to stack '''
        operands = rpn_api.payload
        return rpn.push(operands['total'])


    @rpn_api.doc('get_stack')
    def get(self):
        ''' Read stack '''
        return rpn.get_stacks()

    @rpn_api.doc('clean_stack')
    @rpn_api.response(204,'Stack clean') 
    def delete(self):
        ''' Clean stack '''
        rpn.clear()
        return rpn.clear()