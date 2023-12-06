def greeting(name):
    def message(msg):
        return f'Hi, {name}. {msg}'
    return message

# msg_for_me = greeting('Kari')
# print(msg_for_me('Great job!'))


# currying 
msg_for_me = greeting('Kari')('Great job!')
print(msg_for_me)