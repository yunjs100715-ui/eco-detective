
import tkinter as tk
import random

BG = "#F1F8E9"
GREEN = "#2E7D32"
WHITE = "#FFFFFF"
DARK = "#26382B"

QUESTIONS = [
    {
        "q": "재생 가능한 에너지는 무엇일까요?",
        "options": ["석탄", "태양광", "석유", "천연가스"],
        "answer": 1,
        "info": "태양광은 햇빛을 이용하는 재생에너지입니다."
    },
    {
        "q": "쓰지 않는 전등을 끄면 무엇이 줄어들까요?",
        "options": ["중력", "산소", "전기 소비", "강수량"],
        "answer": 2,
        "info": "전등을 끄면 전력 소비를 줄일 수 있습니다."
    },
    {
        "q": "음식물 쓰레기를 줄이는 이유는?",
        "options": [
            "자원 낭비와 온실가스를 줄이기 위해",
            "비를 내리게 하려고",
            "전기를 더 쓰려고",
            "플라스틱을 만들려고"
        ],
        "answer": 0,
        "info": "음식 생산과 폐기에는 물과 에너지가 필요합니다."
    },
    {
        "q": "환경 데이터를 분석할 때 중요한 것은?",
        "options": [
            "마음에 드는 숫자만 고르기",
            "출처와 측정 조건 확인하기",
            "자료를 무조건 믿기",
            "예상과 다른 자료 버리기"
        ],
        "answer": 1,
        "info": "좋은 분석은 데이터의 출처와 한계를 확인합니다."
    },
    {
        "q": "지구 온난화의 주요 원인 중 하나는?",
        "options": [
            "달의 모양",
            "밤과 낮의 반복",
            "계절의 변화",
            "온실가스 증가"
        ],
        "answer": 3,
        "info": "온실가스는 지구가 열을 가두는 데 영향을 줍니다."
    }
]


class EcoDetective:
    def __init__(self, root):
        self.root = root
        self.root.title("Eco Detective - 환경 탐정")
        self.root.geometry("650x520")
        self.root.configure(bg=BG)
        self.restart()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def make_label(self, text, size=13, color=DARK):
        return tk.Label(
            self.root,
            text=text,
            font=("Malgun Gothic", size, "bold"),
            bg=BG,
            fg=color,
            wraplength=560,
            justify="center"
        )

    def restart(self):
        self.questions = random.sample(QUESTIONS, len(QUESTIONS))
        self.index = 0
        self.score = 0
        self.correct = 0
        self.show_question()

    def show_question(self):
        self.clear()

        if self.index >= len(self.questions):
            self.show_result()
            return

        self.selected = False
        q = self.questions[self.index]

        self.make_label("🌍 ECO DETECTIVE", 24, GREEN).pack(pady=(20, 8))
        self.make_label(
            f"미션 {self.index + 1} / {len(self.questions)}"
            f"     점수: {self.score}"
        ).pack(pady=5)

        self.make_label(q["q"], 16).pack(pady=20)

        for i, option in enumerate(q["options"]):
            tk.Button(
                self.root,
                text=f"{i + 1}. {option}",
                font=("Malgun Gothic", 12),
                bg=WHITE,
                fg=DARK,
                relief="flat",
                cursor="hand2",
                command=lambda choice=i: self.check(choice)
            ).pack(fill="x", padx=65, pady=4)

        self.feedback = self.make_label("", 11, GREEN)
        self.feedback.pack(pady=12)

        self.next_btn = tk.Button(
            self.root,
            text="다음 미션 →",
            font=("Malgun Gothic", 12, "bold"),
            bg=GREEN,
            fg=WHITE,
            command=self.next_question,
            state="disabled"
        )
        self.next_btn.pack(pady=5)

    def check(self, choice):
        if self.selected:
            return

        self.selected = True
        q = self.questions[self.index]

        if choice == q["answer"]:
            self.score += 20
            self.correct += 1
            result = "정답입니다! +20점 🎉"
        else:
            result = f"아쉬워요! 정답: {q['options'][q['answer']]}"

        self.feedback.config(text=f"{result}\n💡 {q['info']}")

        # 답을 선택한 후에는 모든 선택 버튼을 비활성화
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button) and widget != self.next_btn:
                widget.config(state="disabled")

        self.next_btn.config(state="normal")

    def next_question(self):
        self.index += 1
        self.show_question()

    def show_result(self):
        self.clear()
        rate = round(self.correct / len(self.questions) * 100)

        if rate == 100:
            rank = "🌟 지구 지킴이 마스터!"
        elif rate >= 60:
            rank = "🌿 그린 탐정!"
        else:
            rank = "🌱 새싹 탐정!"

        self.make_label("MISSION COMPLETE!", 24, GREEN).pack(pady=35)
        self.make_label(rank, 20).pack(pady=12)
        self.make_label(
            f"최종 점수: {self.score}점\n"
            f"정답: {self.correct}/{len(self.questions)}\n"
            f"정답률: {rate}%"
        ).pack(pady=15)

        tk.Button(
            self.root,
            text="다시 도전하기",
            font=("Malgun Gothic", 12, "bold"),
            bg=GREEN,
            fg=WHITE,
            command=self.restart
        ).pack(pady=15)


if __name__ == "__main__":
    root = tk.Tk()
    app = EcoDetective(root)
    root.mainloop()
