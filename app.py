import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = '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'
openai.Model.list()


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]

        # response = openai.Completion.create(
            # model="text-davinci-003",
        #     model="gpt-3.5-turbo",
        #     prompt=generate_prompt(animal),
        #     temperature=0.4,
        #     max_tokens=1000,
        #     n = 1,
        # )

        question = generate_prompt(animal)
        # response = openai.ChatCompletion.create(
        #     # model="text-davinci-003",
        #     model="gpt-3.5-turbo",
        #     prompt=generate_prompt(animal),
        #     # prompt=[{"role": "system", "content": "You are a helpful Graduate application consultant assistant."},
        #     # {"role": "user", "content": "我是一名学生，本科大学是暨南大学国际商务专业。我的gpa是3.51/5.0，雅思7分，单项最低分6.0。我有一次国企实习，一次德勤实习，一些奖项，社团活动。我想申请研究生，请你为我提供一个适合我的申请的学校列表。"},
        #     # {"role": "assistant", "content": "1.格拉斯哥大学 MSc International Strategic Marketing 2.伯明翰大学 MSc Marketing 3.杜伦大学 MSc Marketing 4.布里斯托大学 MSc Marketing"},
        #     # {"role": "user", "content": "我是一名学生，本科大学是西交利物浦大学。我的均分是71，雅思6.5分，单项最低分6.0。我有一次银行软件开发实习，一次互联网小公司数据科学方向实习，一些奖项，社团活动。我想申请研究生，请你为我提供一个适合我的申请的学校列表。"},
        #     # {"role": "assistant", "content": "1.University of edinburgh MSc Informatcs 2.University college London 数字人文 3.University of Manchester cs 4.UCLA cs .University of Southampton cs"},
        #     # {"role": "user", "content": question}],
        #     temperature=0.4,
        #     max_tokens=1000,
        # )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "请你扮演对我的留学规划顾问。"},
            {"role": "user", "content": "我是一名学生，本科大学是暨南大学国际商务专业。我的gpa是3.51/5.0，雅思7分，单项最低分6.0。我有一次国企实习，一次德勤实习，一些奖项，社团活动。我想申请研究生，请你为我提供一个适合我的申请的学校列表。"},
            {"role": "assistant", "content": "1.格拉斯哥大学 MSc International Strategic Marketing 2.伯明翰大学 MSc Marketing 3.杜伦大学 MSc Marketing 4.布里斯托大学 MSc Marketing"},
            {"role": "user", "content": "我是一名学生，本科大学是西交利物浦大学。我的均分是71，雅思6.5分，单项最低分6.0。我有一次银行软件开发实习，一次互联网小公司数据科学方向实习，一些奖项，社团活动。我想申请研究生，请你为我提供一个适合我的申请的学校列表。"},
            {"role": "assistant", "content": "1.University of edinburgh MSc Informatcs 2.University college London 数字人文 3.University of Manchester cs 4.UCLA cs .University of Southampton cs"},
            {"role": "user", "content": question}],
            temperature=0.4,
            max_tokens=500,
        )

        print(response)
        # print(response.choices[0].message.content)
        return redirect(url_for("index", result=response.choices[0].message.content))

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
    # sch_sco = sch_sco.split('_')
    # major = sch_sco[0]
    # school = sch_sco[1]
    # score = sch_sco[2]
    # return """我想申请海外研究生，请你扮演我的留学中介。我的背景是{}
    # 以下是一些研究生申请案例，包括背景bg和申请结果，请你根据我提供信息，提供和我能力背景匹配的，适合我申请的海外学校和这个学校的具体专业。
    # 如果我成绩好，请给我排名靠前的学校；如果我成绩差，请给我排名靠后易于申请的专业。返回5条结果，每条结果包括学校，专业，和被录取的概率这三项信息。
    # 1. bg: 暨南大学，国际商务，gpa3.51/5.0，雅思7分，单项6.0，有一次国企实习，一次德勤实习，一些奖项，社团活动
    #     录取结果: 录了格拉斯哥的MSc International Strategic Marketing；伯明翰的MSc Marketing，杜伦的MSc Marketing，布里斯托大学发了拒信
    # 2. bg: shcool: Xi'an Jiaotong Liverpool University; score:70; 雅思6.5 两段水实习 
    #     录取结果: [1.University of edinburgh 信息学 offer 2.University college London 数字人文 offer 3.University of Manchester cs offer 4.UCLA cs 被拒5.University of Southampton cs offer]
    # 3. bg: 双非双一流中药学85 gap中 雅思6.5 
    #     录取结果: 利兹药物发现：九月初-十月中offer 格拉临床药理：十月初-无消息默拒？ 华威生物管理：10/12-11/10offer KCL药物分析：11/4-11/22offer 曼大医学微生物：11/8-12/5offer 爱丁堡药物转化/生物化学分别九月秒拒十二月秒拒 hku食品：11/1-12/6offer药学：一月中-无消息 cuhk hkust cityu 生物相关九月十月开放就申请-无消息默拒 polyu bme：11/1-12月中面试-一月offer nus制药11月底-1月中补材料-2月中补材料-2/27offer-应该是最后去向
    # 4. bg: 985(非顶尖)，网络安全本科，GPA88，申请时无雅思托福，一段昆士兰大学暑期科研并二作发了顶会，还有一篇国内二作和国内论文(论文署名顺序排名靠后)，信息安全大赛国三，参加大创和美赛(结果不好)
    #     录取结果：UCL DS: 被拒绝，悉尼大学: offer，格拉斯哥大学: offer，南安普顿cs: offer 
    # 返回英文结果""".format(sch_sco)
    return """ 我的背景是双非一本，网络安全本科，GPA70，申请时无雅思托福，参加大创和美赛(结果不好)。
    我想申请英国的研究生，请你为我提供一个适合我的申请的学校列表。返回适合我申请的学校，专业，和录取概率这三项信息。"""