#### Time taken: < 1 hour

# Instructions For Use

1. Ensure the python environment contains the required libraries - this can be done using the `pip3 install -r requirements.txt` command
2. In a CLI, navigate to the folder containing ppl_trello.py
3. Execute the file using the command `python ppl_trello.py`
4. Enter the following information as prompted:
    a. The name of the Trello List to add the card to (select from the list shown)
    b. The label to assign to the card (a new label will be created)
    c. The comment to add to the card
5. The program will return the response code for the API call - 200 means success.

In order to change what board the card is added to, open the file in notepad and change:
1. board_id
2. key
3. token

# Next Steps

Next steps for development would be (assuming this would be used widescale by other people):
1. Allowing the selection of a Board from multiple Boards - Organisation ID can be used to get all boards, use format similar to Lists
    1.1. Enter name of Board to select that board
    1.2. Enter new word to create a new Board with that name
    1.3. Should probably not allow creation of Boards for every use
2. Allow the use of existing labels - could have format similat to List selection
    2.1. Type in existing Label to select that Label
    2.2. Type in new word to create that Label
3. Allow the user to set the colour of the label  
4. Allow the creation of new Lists
    4.1. Enter a new word to create a List under that name at List selection
5. Remove `key` and `token` from code - should be stored in an environemtn variable file that would not get pushed to github
    5.1. However, doing so would make it hard to change to allow testing for whoever looks at this assessment
    5.2. I just want to stress I would normally not push those values and would not consider it production ready, I only consider it even remotely safe to do so as they
        are my own personal `key` and `token`