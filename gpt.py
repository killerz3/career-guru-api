

import openai,json

openai.api_key = "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"
def gpt_career(class_current,subjects,mindset,interests):
  response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="\nclass: "+class_current+"\nsubjects: "+subjects+"\nmindset:"+mindset+"\ninclude colleges only from India \n"+"interests: "+interests+"The best career paths for you would be:\n",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
#   print(response)
  result=json.loads(str(response))
  print(result["choices"][0]["text"])
  return result["choices"][0]["text"]
  
# gpt("9th",'["maths","physics"]','["logical","analytical"]','["scifi movies,coding"]')

def gpt_ques(class_current,subjects,mindset,interests,question):
  response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="\nclass: "+class_current+"\nsubjects: "+subjects+"\nmindset:"+mindset+"\ngive a step by step process  or explain specifically\n"+"interests: "+interests+" "+question+"?",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
#   print(response)
  result=json.loads(str(response))
  print(result["choices"][0]["text"])
  return result["choices"][0]["text"]