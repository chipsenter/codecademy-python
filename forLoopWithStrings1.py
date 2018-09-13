"""Create a function that concatenates strings.

Define a function called join_strings accepts an argument called words. It will be a list.
Inside the function, create a variable called result and set it to "", an empty string.
Iterate through the words list and concatenate each word to result.
Finally, return the result.
Don't add spaces between the joined strings!"""


n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
  result = ""
  for word in words:
    result += word
  return result


print join_strings(n)