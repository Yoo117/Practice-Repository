// 일본어 음성 인식 객체 생성
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = 'ja-JP'
recognition.interimResults = false;
let recognizing = false;
let recognitionPaused = false;

// 음성 인식 토글버튼
function toggleRecognition() {
    const toggleBtn = document.querySelector('#toggleBtn')

    if (recognizing) {
        recognition.stop();
        recognizing = false;
        toggleBtn.textContent = "Voice off";
        toggleBtn.classList.remove("active");
    } else{
        recognition.start();
        recognizing = true;
        toggleBtn.textContent = "Voice on";
        toggleBtn.classList.add("active");
    }
}

// 음성 인식 결과 처리
recognition.onresult = function(event) {
    const userInput = event.results[0][0].transcript;
    document.querySelector("#userInput").value = userInput;
    sendMessage();
};

// 음성 인식 종료 처리
recognition.onend = function() {
    if (recognizing && !recognitionPaused) {
        recognition.start();
    }
};

// 음성 인식 에러 처리
recognition.onerror = function(event) {
    console.error("Speech recognition error:", event.error);
};

// 음성 발성 후 인식 재개
function resumeRecognition() {
    if (recognitionPaused) {
        recognition.start();
        recognitionPaused = false;
    }
}

// API 메세지 음성화 
function speakJapanese(text) {
    const japaneseText = text.replace(/[^\p{Script=Hiragana}\p{Script=Katakana}\p{Script=Han}\s]/gu, '');
    const speechSynthesis = window.speechSynthesis;
    const utterance = new SpeechSynthesisUtterance(japaneseText);
    utterance.lang = 'ja-JP';

    if (recognizing) {
        recognition.stop();
        recognitionPaused = true;
    }

    utterance.onend = resumeRecognition;
    speechSynthesis.speak(utterance);
}

// 대화 로그 자동 스크롤 함수
function scrollToBottom() {
    const chatLog = document.querySelector("#chatLog");
    chatLog.scrollTop = chatLog.scrollHeight;
}

// Enter 키 이벤트 리스너 추가
document.addEventListener("DOMContentLoaded", function() {
    document.querySelector("#userInput").addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });
});

// 고정 버튼과 주의사항 콘텐츠
const noticeButton = document.querySelector('#noticeButton')
const noticeContent = document.querySelector('#noticeContent')

// 버튼 클릭 이벤트
noticeButton.addEventListener('click', () => {
    const currentDisplay = window.getComputedStyle(noticeContent).display;
    
    if (currentDisplay === 'none') {
        noticeContent.style.display = 'block';
    } else {
        noticeContent.style.display = 'none';
    }
});

// 사용자-API 대화 메인 
function sendMessage() {
    const userInput = document.querySelector("#userInput").value;
    if (!userInput) return;

    // 사용자 메세지 표시
    const userMessage = document.createElement("div");
    userMessage.className = "chat-message user-message";
    userMessage.textContent = userInput;
    document.querySelector("#chatLog").appendChild(userMessage);

    scrollToBottom();

    // 사용자 메세지를 백엔드에 전달
    fetch("/send_message", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // API 메세지 표시
        const assistantMessage = document.createElement("div");
        assistantMessage.className = "chat-message assistant-message";
        assistantMessage.textContent = data.response;
        document.querySelector("#chatLog").appendChild(assistantMessage);

        speakJapanese(data.response);
        scrollToBottom();
    });

    // HTTP 요청 후 input 창 초기화
    document.querySelector("#userInput").value = "";
}
