import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = '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'


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
            max_tokens=100,
            n = 1,
        )
        # print(type(response.choices))
        # print(len(response.choices))
        # print(response.choices)
        # for res in response.choices:
        #     print(res.text)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


# def generate_prompt(animal):
#     return """ three names for an animal that is a superhero.

# Animal: CatSuggest
# Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
# Animal: Dog
# Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
# Animal: {}
# Names:""".format(
#         animal.capitalize()
#     )

def generate_prompt(sch_sco):
    sch_sco = sch_sco.split('_')
    major = sch_sco[0]
    school = sch_sco[1]
    score = sch_sco[2]
    return """I am a student major in {}. My school is {}, and my average score is {},  
    could you generate a list of majors and a list of 5 Universities that match my background for my master application""".format(major, school, score)
