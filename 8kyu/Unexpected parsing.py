# Unexpected parsing
#
# https://www.codewars.com/kata/54fdaa4a50f167b5c000005f
#
# Here is a piece of code:
#
# def get_status(is_busy):
#     status = "busy" if is_busy else "available"
#     return status
# Expected Behaviour
# Function should return a dictionary/Object/Hash with "status" as a key, whose value can : "busy" or "available" depending on the truth value of the argument is_busy.
#
# But as you will see after clicking RUN or ATTEMPT this code has several bugs, please fix them.

def get_status(is_busy):
    obj = {}
    obj["status"] = "busy" if is_busy else "available"
    return obj

# Best practice:
#
# def get_status(is_busy):
#     status = "busy" if is_busy else "available"
#     return {"status" : status}
#
# Clever solution:
#
# def get_status(is_busy): return {'status': ("busy" if is_busy else "available")}


