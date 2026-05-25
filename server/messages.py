def create_message(sender,text):
    message={
        "sender":sender,
        "text":text
    }
    print("Message created:",message)
    return message

def get_message(messages_list,sender):
    for message in messages_list:
        if message["sender"]==sender:
            return message
        return None
            
def update_message(messages_list,sender,new_text):
    for message in messages_list:
        if message["sender"]==sender:
            message["text"]=new_text
            return message
        return None
    
def delete_message(messages_list,sender):
    for message in messages_list:
        if message["sender"]==sender:
            messages_list.remove(message)
            return True
        return False

messages=[]
messages.append(create_message("Himanshu","American Dream!"))
messages.append(create_message("Sarah","We did it!"))
print("Find Sarah:",get_message(messages,"Sarah"))
update_message(messages,"Himanshu","Alright!")
print("Update:",get_message(messages,"Himanshu"))
delete_message(messages,"Sarah")
print("After delete",messages)


            


