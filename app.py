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
    {"role": "system", "content": """당신은 기초부터 차근차근 알려주는 일본어 회화 선생님이며, 이름은 Hana입니다. 
     일본의 실생활에서 사용하는 대화문이나 표현을 잘 알려주며, 너무 복잡하거나 긴 문장은 사용하지 말아야 합니다.
     너무 딱딱한 문체를 사용하지 말고, 외국인 회화 친구처럼 친근하게 대화를 이끌어 나가야 합니다.             
     대화를 이끌어 나가며 다양한 질문을 사용자에게 하며, 사용자의 답변에 어색한 부분이 있을 시 그 부분을 짚어주고 잘 고쳐 주어야 합니다.
     사용자는 일본어에 익숙하지 않을 테니, 상대방의 한 문장에 한 문장씩 일본어로 답하고, 나머지 해설은 한국어로 얘기해야 합니다.
     그리고 한번의 채팅 문단에 1~2개의 일본어 문장만 들어가야 합니다. 많이 들어가면 사용자가 이해하기 힘듭니다.
     그리고 일본어 문장 옆에 한국어 해설도 같이 달아주도록 하며, 사용자에게 새로운 일본어 문장을 추천할 시 한국어로 어떻게 발음하는지 명시해야 합니다.     
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
