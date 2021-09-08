
# welcome_assignment_answers
# Input - All eight questions given in the assignment.
# Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    if question ==  "In Slack, what is the secret passphrase posted in the #cyberfellows-computernetworking-fall2021 channel posted by a TA?":
        answer = "mTLS"
        return (answer)
    elif question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
        return (answer)
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No" #maybe a Yes, if its a theoretical question
        return (answer)
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "No" #maybe a Yes
        return (answer)
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
        return (answer)
    elif question == "What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code":
        answer = "42b76fe51778764973077a5a94056724"
        return (answer)
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "Yes"
        return (answer)
    elif question == "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number":
        answer = "7"
        return (answer)
    elif question == "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number":
        answer = "4"
        return(answer)

