// 초기값 설정
let grades = [1, 2, 3]; // 학년 순서
let startTimes = [40, 45, 50]; // 각 학년의 시작 시간
const interval = 3000; // 3초마다 갱신  (7 * 24 * 60 * 60 * 1000; 일주일 마다 갱신 코드)

// 급식 순서 생성 함수
function generateMealOrder() {
    const mealOrderDiv = document.getElementById("mealOrder");
    mealOrderDiv.innerHTML = ""; // 이전 내용 초기화

    for (let i = 0; i < 3; i++) { // 1학년부터 3학년까지
        const mealTime = document.createElement("p");
        mealTime.textContent = ` ${grades[i]}학년: ${startTimes[i]}분`; // 학년과 시작 시간 표시
        mealOrderDiv.appendChild(mealTime);

        // 시간 변경
        startTimes[i] -= 5;
        if (startTimes[i] < 40) {
            startTimes[i] = 50;
        }
    }
}

// 페이지 로드시 초기 순서 생성
generateMealOrder();

// 3초마다 순서 갱신
setInterval(generateMealOrder, interval);