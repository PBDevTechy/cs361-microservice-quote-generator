from flask import Flask, request, jsonify

app = Flask(__name__)

# home page
@app.route('/')
def home():
    return "QuoteBuild API is running..."

# starter 
@app.route('/generate-quote')
def generate_quote():
    return "Quote route working."

# run
if __name__ == 'main':
    app.run(debug=True)

# if project info exists
def project_info_ok(project_data):
    
    required_fields = [
        "client_name",
        "project_type",
        "project_size",
        "service_category",
        "estimated_budget"
    ]
    
    for field in required_fields:
        
        if field not in project_data or not project_data[field]:
            return  False
        
    return True

#estimate project pricing
def estimate_price(project_type, project_size):

    project_type = project_type.lower()
    project_size = project_size.lower()


    # residential projects
    if project_type == "residential":

        if project_size == "small":
            return "$5,000 - $10,000"

        elif project_size == "medium":
            return "$15,000 - $25,000"

        elif project_size == "large":
            return "$30,000 - $50,000"


    # commercial projects
    elif project_type == "commercial":

        if project_size == "small":
            return "$20,000 - $40,000"

        elif project_size == "medium":
            return "$50,000 - $80,000"

        elif project_size == "large":
            return "$100,000+"


    # interior design projects
    elif project_type == "interior design":

        if project_size == "small":
            return "$3,000 - $8,000"

        elif project_size == "medium":
            return "$10,000 - $20,000"

        elif project_size == "large":
            return "$25,000+"


    # renovation projects
    elif project_type == "renovation":

        if project_size == "small":
            return "$8,000 - $15,000"

        elif project_size == "medium":
            return "$20,000 - $40,000"

        elif project_size == "large":
            return "$50,000+"

    return "Custom quote needed"

# main quote route
@app.route('/generate-quote', methods=['POST'])
def estimate_project_cost():

    # get project data from request
    project_data = request.get_json()


    # check if info missing
    if not project_info_ok(project_data):

        return jsonify({
            "status": "error",
            "message": "Project information missing."
        }), 400


    # get values
    client_name = project_data["client_name"]
    project_type = project_data["project_type"]
    project_size = project_data["project_size"]
    service_category = project_data["service_category"]
    estimated_budget = project_data["estimated_budget"]


    # calculate estimate
    estimated_price = estimate_price(project_type, project_size)


    # create response
    quote_response = {

        "client_name": client_name,
        "project_type": project_type,
        "project_size": project_size,
        "service_category": service_category,
        "estimated_budget": estimated_budget,
        "estimated_price": estimated_price,
        "status": "success",
        "notes": "Final quote can change depend on project details."

    }

    return jsonify(quote_response)


# run app
if __name__ == '__main__':
    app.run(debug=True)