from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from dotenv import load_dotenv

load_dotenv()

anthropic = Anthropic()

#read csv
csv_path = "generated_greenhouse_data.csv"
with open(csv_path, 'r') as f:
    csv_data = f.read()

prompt = (
    "An analysis of the following greenhouse data for tomatoes in winter: \n"
    f"{csv_data}\n"
    "Please provide insights on data trends and recommendations."
    "The data includes cumulative irrigation per day (Cum_irr) temperature (tair), humidity (rhair), drainage EC (EC_drain_PC), drainage pH (pH_drain_PC), and light levels (Tot_PAR) over a week. "
    "Ideal values for humidity is 60-70%, temperature is 18-22°C, drainage EC is 2.5-3.5 mS/cm, drainage pH is 5.5-6.5, and light levels should be above 200 μmol/m2/s during the day. "
    "Client is the greenhouse owner."
    "Describe trends in each factor using one sentence each and provide two recommendations based on correlating factors. Pay attention to how EC interacts with other metrics to give the best recommendation."
    "When mentioning time, convert to month/day and time in 24 hour format. "
    "Keep total response under 1000 tokens"
)

message = anthropic.messages.create(
    model="claude-opus-4-6",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(message.content[0].text)

with open("greenhouse_report.txt", "w", encoding="utf-8") as report_file:
    report_file.write("\n\nRecommendations:\n")
    report_file.write(message.content[0].text)
    