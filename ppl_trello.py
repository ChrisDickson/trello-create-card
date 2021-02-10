import requests
import json
import os

base_url = "https://api.trello.com/1/"

# These need to be changed to change the board
board_id = ""
key = ""
token = ""

'''
Some assumptions:
1. The user only wants to add cards to a single board.
2. The board being used already exists.
3. The list being used already exists.
4. The user has permission to add cards to the board (no authentication).
5. Labels need only be of a single colour.
6. A new label should be added every time.
7. No need to sanitize inputs beyond removing quotes and whitespace, Trello will handle anything else.
'''


def get_card_details():
    '''
    Input: None

    Returns: label   - String - label to be used for the card to be created
            comment - String - comment to be added to the card to be created
    '''
    label = input("Please enter the label for the card: ").replace("\"", "").replace("\'","").strip()
    comment = input("Please enter the comments for the card: ").replace("\"", "").replace("\'","").strip()
    return(label, comment)

# for security reasons, in production code keys and token should not be commited to git
# for best coding practices, it should not be hard coded

def get_list_details():
    '''
    Input: none
    Returns: list_id - String - ID of selected Trello List
    '''
    url = base_url+"boards/"+board_id+"/lists"
    request_type = "GET"
    query = {
        "key": key,
        "token": token
   }

    response = make_api_request(url, request_type, query)
    json_data = json.loads(response.text)
    list_dict = {}
    if len(json_data) > 0:
        for x in range(len(json_data)):
            if "name" and "id" in json_data[x]:
                list_dict[json_data[x]["name"]] = json_data[x]["id"]
            else:
                # A given list might not contain a name and ID due to errors on the other end
                # If so, skip to next
                # If none contained both a name and ID, no 
                continue
    if len(list_dict) > 0:
        list_name = input(f"Please select the name of the list to add the card to from the following list - {list(list_dict.keys())}: ").replace("\"", "").replace("\'","").strip()
        if list_name in list_dict:
            list_id = list_dict.get(list_name)
            return(list_id)
        else:
            print("List name given does not exist - exiting. ")
            os._exit(0)
    else:
        print("No useable lists were found - exiting. ")
        os._exit(0)


def create_trello_card(list_id, label_id, comment):
    '''
    Input:  list_id - String - id of List card should be added to
            label_id - String - id of Label to be added to the card
            comment - comment - comment to be added to the card
    Returns: response - Response - HTTP response object from requests library
    '''
    url = base_url+"cards"
    request_type = "POST"
    query = {
        "key": key,
        "token": token,
        "idList": list_id,
        "idLabels": [label_id],
        "name": comment
    }

    response = make_api_request(url,request_type, query)
    return(response)


def add_label(label):
    '''
    Input: label - String - name of label to be created
    Returns: json_data["id"] - String - ID of label that was created
    '''
    url = base_url+"labels"
    request_type = "POST"
    query = {
        "key": key,
        "token": token,
        "name": label,
        "color": 'blue',
        "idBoard": board_id
    }

    response = make_api_request(url,request_type, query)
    json_data = json.loads(response.text)
    return(json_data["id"])


def make_api_request(url, request_type, query):
    '''
    Input:   url            - String    - the url of the API endpoint to hit
             request_type   - String    - the type of HTTP request to use (GET or POST)
             query          - String    - list of query parameters
    Returns: response       - Response  - HTTP response object
    '''
    headers = {
        "Accept":"application/json"
    }

    response = requests.request(
        request_type,
        url,
        params=query
    )

    return(response)


list_id = get_list_details()
label, comment = get_card_details()
label_id = add_label(label)
create_trello_card(list_id, label_id, comment)
