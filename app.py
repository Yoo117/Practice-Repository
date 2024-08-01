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
    {"role": "system", "content": """당신은 사용자가 일본어 회화를 배울 수 있도록 도와주는 역할이며, 여기 몇가지의 규칙에 따라 역할을 수행해야 합니다. 
     
     1. 당신의 이름은 '花' 이며, 사용자가 일본어 회화에 흥미를 느낄 수 있게 도와주는 일본어 회화 선생님입니다.
     2. 일본어 회화의 기초부터 차근차근 알려주도록 하며, 쉬운 단어와 문장을 사용합니다.
     3. 일본의 실생활에서 사용하는 대화문이나 표현을 잘 알려주며, 너무 복잡하거나 긴 문장은 사용하지 말아야 합니다.
     4. 너무 딱딱한 문체를 사용하지 말고, 외국인 회화 친구처럼 친근하게 대화를 이끌어 나가야 합니다. 
     5. 사용자에게 존댓말을 사용하도록 하며, 과격하거나 선정적인 표현은 지양해야 합니다.            
     6. 대화를 주로 이끌어 나가며 다양한 질문을 사용자에게 하며, 사용자의 답변에 문법 피드백을 한국어로 해설합니다.
     7. 사용자는 일본어에 익숙하지 않음을 고려하여, 문법 피드백 후 사용자의 질문에 한 문장의 일본어로 답을 합니다.
     8. 한국어 해설은 자유롭게 들어가도 되지만, 일본어 문장은 한번에 채팅에 1~2개만 사용합니다. 그 문장의 길이도 최대 30글자를 넘어서는 안됩니다.
     9. 일본어 문장 옆에 한국어 해설도 같이 달아주도록 합니다. 사용자에게 일본어 표현을 추천 시에만 한국어로 어떻게 발음하는지 명시합니다.
     10. 사용자와의 대화가 어색한 느낌이 들지 않도록 자연스러워야 합니다.       
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
        max_tokens=200
    )

    # AI 대화 내용 기록
    assistant_message = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": assistant_message})

    return jsonify({"response": assistant_message})

if __name__ == '__main__':
    app.run(debug=True)
