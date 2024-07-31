# 필요한 패키지
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os

# 환경 변수 로드 및 Flask 애플리케이션 인스턴스 생성
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

app = Flask(__name__)


# 초기 대화 이력 설정
conversation_history = [
    {"role": "system", "content": """너는 기초부터 차근차근 알려주는 일본어 회화 선생님 '花' 입니다. 
     일본의 실생활에서 사용하는 대화문이나 표현을 잘 알려주며, 너무 복잡하거나 긴 문장은 사용하지 말아야 해.              
     너가 대화를 이끌어 나가면서 여러가지 질문을 사용자에게 하며, 사용자가 물어보는 것도 피드백을 바로바로 잘 해줘야 해.
     아 그리고, 일본어 문장을 보여줄 때, 한국어 해설/한국어 발음 구문도 같이 보여줬으면 좋겠어.
     
     """},   
]

# Html 렌더링
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    global conversation_history

    # 사용자 대화 내용 기록
    user_message = request.json['message']
    conversation_history.append({"role": "user", "content": user_message})

    # API 호출 및 응답 생성
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=conversation_history,
        temperature=1.0,
        max_tokens=300
    )

    # API 대화 내용 기록
    assistant_message = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": assistant_message})

    return jsonify({"response": assistant_message})

if __name__ == '__main__':
    app.run(debug=True)
