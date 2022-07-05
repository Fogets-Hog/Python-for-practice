is_ready = False

# if is_ready:
#  state_msg = "Ready"
# else:
#  state_msg = "Not ready yet"
state_msg = is_ready and "Ready" or "Not ready yet"
print (state_msg)