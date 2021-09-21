from sqlalchemy.orm import query
from app import app, database
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import jsonify, request
from app.controller.taskmanager import createTask, getTask, getAllTasks,  updateTask, deleteTask

query = ObjectType("Query")
mutation = ObjectType("Mutation")

query.set_field("listAllTasks", getAllTasks)
query.set_field("getTask", getTask)
mutation.set_field("createTask", createTask)
mutation.set_field("updateTask", updateTask)
mutation.set_field("deleteTask", deleteTask)

type_defs = load_schema_from_path('schema_task.graphql')
schema = make_executable_schema(type_defs, query, mutation ,snake_case_fallback_resolvers)

@app.route('/graphql', methods=['GET'])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code



if __name__ == '__main__':
    app.run(debug=True)