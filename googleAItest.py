import google.generativeai as palm

API_KEY = 'AIzaSyDmuAwxQ4u7a0-Y_nBd_9-57JP_FMO7Pzc'

palm.configure(api_key=API_KEY)

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

with open('jobDescription.txt', 'r') as file:
    jobDescription = file.read()
with open('resumeFormatted.txt', 'r') as file:
    resumeFormatted = file.read()

prompt = jobDescription + '\n' + resumeFormatted + '\n' + 'Rate this resume based on the job description and be harsh and specific'
completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
)

print(completion.result)