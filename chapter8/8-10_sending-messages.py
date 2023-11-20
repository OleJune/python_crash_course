def send_messages(original_list, new_list):
	"""Move each text message to a new_list after printing the message."""
	while original_list:
		message = original_list.pop()
		print(message)
		new_list.append(message)

text_messages = ['Good morning!', 'Good afternoon!', 'Good evening!']
sent_messages = []

send_messages(text_messages, sent_messages)
print(f"\nOriginal list:\n{text_messages}")
print(f"\nNew list:\n{sent_messages}")

