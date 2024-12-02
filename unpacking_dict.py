button = {
    'width': 200,
    'text': 'Buy'
}

red_button = {
    **button,
    'color': 'red'
}

print(red_button)
print(button)

button_info = {
    'text': 'Buy'
}

button_style = {
    'color': 'yellow',
    'width': 200,
    'hight': 300
}

button_go = {
    **button_style,
    **button_info
}
print(button_go)

button_go = button_info | button_style