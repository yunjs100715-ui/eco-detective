
import tkinter as tk
import random

# =========================
# Eco Detective 3.0
# 환경 과학 퀴즈 게임
# =========================

BG = "#EAF7EE"
DARK = "#174A35"
GREEN = "#278653"
LIGHT = "#D6F0DD"
WHITE = "#FFFFFF"
YELLOW = "#FFF0B3"
RED = "#FCE1DF"
TEXT = "#24372C"
MUTED = "#648071"

LEVELS = {
    "중급": {
        "points": 10,
        "desc": "환경 과학의 핵심 개념을 알아보자!",
        "questions": [
            {
                "q": "호수에 비료 성분이 많이 유입되면 어떤 문제가 생길 수 있을까?",
                "choices": [
                    "물속 산소가 무조건 증가한다",
                    "조류가 지나치게 번식해 산소가 부족해질 수 있다",
                    "호수의 물이 즉시 증발한다",
                    "모든 물고기의 크기가 커진다"
                ],
                "answer": 1,
                "explain": "질소와 인이 과도하게 유입되면 조류가 급증할 수 있어. 조류가 분해되는 과정에서 산소가 소비되면 물고기가 살기 어려워져."
            },
            {
                "q": "눈과 얼음이 녹으면 지구가 더 따뜻해질 수 있는 이유는?",
                "choices": [
                    "바다가 햇빛을 전혀 받지 않아서",
                    "눈과 얼음이 지구의 중력을 없애서",
                    "밝은 표면이 줄어 햇빛을 더 많이 흡수해서",
                    "대기 중 산소가 사라져서"
                ],
                "answer": 2,
                "explain": "눈과 얼음은 햇빛을 잘 반사해. 이들이 줄어들면 어두운 바다나 땅이 더 많은 에너지를 흡수해 온난화가 심해질 수 있어. 이를 얼음-알베도 피드백이라고 해."
            },
            {
                "q": "외래종이 생태계에 미치는 영향으로 가장 적절한 것은?",
                "choices": [
                    "언제나 생물 다양성이 증가한다",
                    "토종 생물과 경쟁하거나 먹이 관계를 바꿀 수 있다",
                    "모든 외래종은 해롭다",
                    "생태계에는 어떤 영향도 주지 않는다"
                ],
                "answer": 1,
                "explain": "외래종이 항상 해로운 것은 아니지만, 일부는 토종 생물과 경쟁하거나 포식해 생태계 균형을 무너뜨릴 수 있어."
            },
            {
                "q": "전기 사용으로 발생하는 온실가스 배출량을 추정할 때 필요한 것은?",
                "choices": [
                    "전기 사용량과 전력의 배출계수",
                    "전기 요금 고지서의 색깔",
                    "건물의 층수만",
                    "사용자의 나이"
                ],
                "answer": 0,
                "explain": "전력 사용량에 전력 배출계수를 곱하면 전기 사용에 따른 온실가스 배출량을 추정할 수 있어."
            },
            {
                "q": "생물 다양성이 중요한 이유로 가장 적절한 것은?",
                "choices": [
                    "모든 생물의 크기를 같게 만든다",
                    "생태계의 기능과 안정성에 도움을 줄 수 있다",
                    "자연재해를 완전히 없앤다",
                    "모든 종이 같은 먹이를 먹게 한다"
                ],
                "answer": 1,
                "explain": "다양한 생물은 수분, 분해, 먹이 관계 등 여러 생태계 기능에 기여해. 다양성이 높으면 환경 변화에 대응할 가능성도 커질 수 있어."
            },
            {
                "q": "도시의 땅을 아스팔트와 콘크리트로 덮으면 생길 수 있는 문제는?",
                "choices": [
                    "빗물이 땅속으로 더 잘 스며든다",
                    "도시의 기온이 항상 내려간다",
                    "빗물 침투가 줄고 지표 유출이 늘어난다",
                    "강수량이 즉시 두 배가 된다"
                ],
                "answer": 2,
                "explain": "불투수면은 빗물이 땅속으로 스며드는 것을 막아. 그 결과 빗물이 빠르게 흘러가 침수 위험이 커질 수 있어."
            },
            {
                "q": "먹이사슬에서 수은 같은 일부 오염물질의 농도가 상위 포식자에게 높아지는 현상은?",
                "choices": [
                    "광합성",
                    "생물 농축",
                    "증발",
                    "질소 고정"
                ],
                "answer": 1,
                "explain": "분해되거나 배출되기 어려운 오염물질은 먹이사슬을 따라 이동하면서 상위 단계 생물에 높은 농도로 축적될 수 있어."
            },
            {
                "q": "태양광 발전의 특징으로 가장 적절한 것은?",
                "choices": [
                    "밤에도 항상 같은 양의 전기를 생산한다",
                    "날씨와 일조량의 영향을 받는다",
                    "연료를 태워서만 전기를 만든다",
                    "발전 과정에서 온실가스가 전혀 발생하지 않는다"
                ],
                "answer": 1,
                "explain": "태양광 발전량은 일조량과 날씨에 영향을 받아. 발전 설비의 제조와 설치 등 전체 과정에서도 환경 영향이 발생할 수 있어."
            },
            {
                "q": "숲이 기후 변화 완화에 기여하는 주요 방법은?",
                "choices": [
                    "대기 중 이산화탄소를 흡수해 탄소를 저장한다",
                    "지구의 자전을 멈춘다",
                    "모든 온실가스를 즉시 없앤다",
                    "햇빛을 완전히 차단한다"
                ],
                "answer": 0,
                "explain": "나무는 광합성으로 이산화탄소를 흡수하고 탄소를 몸체와 토양에 저장해. 다만 숲의 보전과 관리도 중요해."
            },
            {
                "q": "환경 정책의 효과를 평가하는 가장 좋은 방법은?",
                "choices": [
                    "정책 담당자의 인상만 듣는다",
                    "정책 시행 전후의 관련 자료를 비교하고 다른 요인도 살핀다",
                    "하루의 날씨만 확인한다",
                    "성공 사례 하나만으로 모든 효과를 판단한다"
                ],
                "answer": 1,
                "explain": "정책 전후의 자료를 비교하되, 계절이나 경제 상황처럼 결과에 영향을 줄 수 있는 다른 요인도 고려해야 해."
            }
        ]
    },

    "고급": {
        "points": 20,
        "desc": "수치 계산과 과학적 분석에 도전하자!",
        "questions": [
            {
                "q": "전기 2,000kWh를 사용했고 배출계수가 0.4kg CO2e/kWh라면 배출량은?",
                "choices": [
                    "80kg CO2e",
                    "400kg CO2e",
                    "800kg CO2e",
                    "8,000kg CO2e"
                ],
                "answer": 2,
                "explain": "배출량 = 사용량 × 배출계수 = 2,000 × 0.4 = 800kg CO2e야."
            },
            {
                "q": "온실가스 배출량이 100톤에서 75톤으로 줄었다. 감소율은?",
                "choices": [
                    "15%",
                    "25%",
                    "75%",
                    "125%"
                ],
                "answer": 1,
                "explain": "감소율 = (100-75) ÷ 100 × 100 = 25%야."
            },
            {
                "q": "어떤 지역의 재생에너지 비율이 20%에서 30%로 올랐다. 올바른 설명은?",
                "choices": [
                    "10%포인트 상승했다",
                    "10% 감소했다",
                    "50%포인트 상승했다",
                    "비율이 변하지 않았다"
                ],
                "answer": 0,
                "explain": "30%-20%=10%포인트 상승이야. 기존 20%를 기준으로 한 상대적 증가율은 50%야."
            },
            {
                "q": "제품 A와 B의 환경 영향을 공정하게 비교하려면 무엇이 중요할까?",
                "choices": [
                    "제품의 포장 색깔만 비교한다",
                    "서로 다른 기능을 가진 제품을 무조건 비교한다",
                    "같은 기능을 제공하는 기준 단위를 정한다",
                    "제조 과정만 보고 사용과 폐기는 무시한다"
                ],
                "answer": 2,
                "explain": "전과정평가에서는 같은 기능을 제공하는 기준 단위, 즉 기능 단위를 정해야 공정한 비교가 가능해."
            },
            {
                "q": "아이스크림 판매량과 익사 사고가 함께 증가했다. 가장 과학적인 해석은?",
                "choices": [
                    "아이스크림이 익사 사고를 직접 일으킨다",
                    "익사 사고가 아이스크림 판매를 일으킨다",
                    "더운 날씨가 두 현상에 모두 영향을 줄 수 있다",
                    "두 현상은 반드시 관련이 없다"
                ],
                "answer": 2,
                "explain": "두 현상이 함께 변한다고 해서 인과관계가 증명되는 것은 아니야. 더운 날씨처럼 두 현상에 영향을 주는 제3의 요인이 있을 수 있어."
            },
            {
                "q": "제품 한 개당 배출량이 5kg에서 4kg으로 줄었다. 생산량이 2배가 되면 총배출량은 어떻게 될까?",
                "choices": [
                    "반드시 0이 된다",
                    "총배출량은 이전의 절반이다",
                    "총배출량은 이전과 같다",
                    "총배출량은 이전의 1.6배다"
                ],
                "answer": 3,
                "explain": "이전 총량은 5×생산량, 새로운 총량은 4×2×생산량이야. 8÷5=1.6이므로 총배출량은 이전의 1.6배야."
            },
            {
                "q": "오염물질의 농도는 낮아졌지만 하천으로 흐르는 물의 양은 크게 증가했다. 무엇을 추가로 확인해야 할까?",
                "choices": [
                    "오염물질의 총유출량",
                    "하천 이름의 길이",
                    "주변 건물의 색깔",
                    "측정 장비의 제조국만"
                ],
                "answer": 0,
                "explain": "농도만으로 전체 오염 규모를 판단할 수 없어. 농도와 유량을 함께 고려해 오염물질의 총유출량을 확인해야 해."
            },
            {
                "q": "두 도시의 에너지 효율을 비교할 때 공정성을 높이는 방법은?",
                "choices": [
                    "전체 사용량만 비교한다",
                    "인구나 생산량 같은 활동 규모를 고려한다",
                    "큰 도시가 항상 비효율적이라고 판단한다",
                    "자료가 없는 도시를 더 효율적이라고 본다"
                ],
                "answer": 1,
                "explain": "도시의 규모가 다르면 전체 에너지 사용량만으로 효율을 판단하기 어려워. 인구나 생산량 등 기준을 맞춰 비교해야 해."
            },
            {
                "q": "재생에너지 비율이 증가했지만 전체 전력 생산량도 크게 늘었다. 무엇이 맞을까?",
                "choices": [
                    "재생에너지 생산량은 무조건 감소했다",
                    "화석연료 발전량은 반드시 0이다",
                    "비율만으로 재생에너지의 절대 생산량을 알 수 없다",
                    "전력 수요가 변하지 않았다는 뜻이다"
                ],
                "answer": 2,
                "explain": "비율은 전체 중 차지하는 몫이야. 실제 생산량을 알려면 전체 전력 생산량과 비율을 함께 확인해야 해."
            },
            {
                "q": "환경 정책 A는 비용 100만 원으로 배출량 10톤을 줄이고, B는 비용 150만 원으로 20톤을 줄였다. 톤당 비용이 더 낮은 정책은?",
                "choices": [
                    "정책 A",
                    "정책 B",
                    "두 정책의 톤당 비용은 같다",
                    "정보가 충분하므로 비교할 수 없다"
                ],
                "answer": 1,
                "explain": "A는 톤당 10만 원, B는 톤당 7만 5천 원이야. 이 단순 계산에서는 B의 톤당 감축 비용이 더 낮아."
            }
        ]
    },

    "전문가": {
        "points": 30,
        "desc": "자료 해석과 복합적인 환경 문제를 해결하자!",
        "questions": [
            {
                "q": "전과정평가(LCA)에서 기능 단위를 설정하는 주된 목적은?",
                "choices": [
                    "제품의 브랜드 가치를 계산하기 위해",
                    "비교 대상이 제공하는 기능을 같은 기준으로 맞추기 위해",
                    "제조 단계만 분석하기 위해",
                    "불리한 환경 자료를 제외하기 위해"
                ],
                "answer": 1,
                "explain": "기능 단위는 제품이나 서비스가 제공하는 기능을 정량화한 기준이야. 이 기준을 맞춰야 서로 다른 제품의 환경 영향을 의미 있게 비교할 수 있어."
            },
            {
                "q": "나무를 많이 심었지만 원래 있던 자연 초지가 사라졌다. 이때 필요한 판단은?",
                "choices": [
                    "나무 수가 늘었으니 생물 다양성도 무조건 증가한다",
                    "초지는 생태적 가치가 없으므로 무시한다",
                    "탄소 저장량뿐 아니라 서식지와 생물 다양성 변화도 평가한다",
                    "식생의 종류는 환경 평가와 관계없다"
                ],
                "answer": 2,
                "explain": "나무 심기가 항상 생물 다양성에 유리한 것은 아니야. 원래 생태계의 특성과 서식지 손실 등 여러 영향을 함께 평가해야 해."
            },
            {
                "q": "모델이 연간 배출량을 100톤으로 추정했지만 불확실성 범위가 ±20톤이다. 가장 적절한 해석은?",
                "choices": [
                    "실제 배출량은 정확히 100톤이다",
                    "불확실성 범위는 항상 오류를 뜻한다",
                    "추정치와 함께 불확실성도 고려해야 한다",
                    "추정치는 아무런 의미가 없다"
                ],
                "answer": 2,
                "explain": "100±20톤은 추정치에 불확실성이 있다는 뜻이야. 이 범위가 무엇을 의미하는지는 모델의 가정과 계산 방법에 따라 해석해야 해."
            },
            {
                "q": "한 지역에서 산림 보호 정책을 시행했지만 벌목이 인근 지역으로 옮겨갔다. 이를 평가할 때 고려할 개념은?",
                "choices": [
                    "탄소의 원자번호",
                    "누출 효과",
                    "알베도의 정의만",
                    "표본의 색깔"
                ],
                "answer": 1,
                "explain": "누출 효과는 한 지역의 활동을 줄였지만 다른 지역에서 비슷한 활동이 증가해 전체 감축 효과가 줄어드는 현상이야."
            },
            {
                "q": "호수 표층의 수온 상승과 용존산소 감소가 동시에 관찰됐다. 가장 타당한 접근은?",
                "choices": [
                    "수온 상승만으로 모든 원인이 확정됐다고 본다",
                    "산소 측정을 중단한다",
                    "수온 외에 영양염류, 수심, 계절 등 다른 요인도 조사한다",
                    "두 자료가 함께 변했으므로 인과관계가 완전히 증명됐다고 본다"
                ],
                "answer": 2,
                "explain": "따뜻한 물은 산소를 덜 녹일 수 있고, 수층의 혼합에도 영향을 줄 수 있어. 하지만 다른 요인도 작용하므로 추가 자료가 필요해."
            },
            {
                "q": "정책 시행 후 배출량이 감소했지만, 정책이 없었어도 감소했을 가능성이 있다. 무엇이 필요할까?",
                "choices": [
                    "정책 시행 후 자료만 사용한다",
                    "정책이 없었을 때의 결과를 추정할 비교 기준을 마련한다",
                    "정책 시행 전 자료를 삭제한다",
                    "배출량과 관계없는 자료만 모은다"
                ],
                "answer": 1,
                "explain": "정책의 효과를 평가하려면 정책이 없었을 경우의 결과, 즉 반사실적 상황을 추정하는 것이 중요해. 비교 지역이나 적절한 통계 방법을 활용할 수 있어."
            },
            {
                "q": "기후 변화 위험을 평가할 때 가장 적절한 접근은?",
                "choices": [
                    "위험은 발생 가능성만으로 결정된다고 본다",
                    "위험은 피해 규모만으로 결정된다고 본다",
                    "위험의 발생 가능성, 피해 규모, 노출과 취약성을 함께 살핀다",
                    "과거에 재해가 없었다면 미래 위험도 없다고 본다"
                ],
                "answer": 2,
                "explain": "위험 평가는 발생 가능성뿐 아니라 노출된 사람과 시설, 피해 규모, 취약성 및 대응 능력 등을 함께 고려해야 해."
            },
            {
                "q": "사업 A가 배출량 100톤을 줄이고 20톤을 추가로 발생시켰다. 다른 영향을 제외한 순감축량은?",
                "choices": [
                    "20톤",
                    "80톤",
                    "100톤",
                    "120톤"
                ],
                "answer": 1,
                "explain": "순감축량은 감축량에서 추가 배출량을 뺀 값이야. 100-20=80톤이야."
            },
            {
                "q": "대기오염을 줄이는 정책이 온실가스 배출을 늘릴 가능성이 있다. 가장 적절한 판단은?",
                "choices": [
                    "한 종류의 오염만 확인하고 즉시 성공으로 판단한다",
                    "환경 문제들은 서로 관련이 없다고 가정한다",
                    "대기오염과 온실가스를 함께 측정해 상충 효과를 평가한다",
                    "온실가스 자료는 항상 무시한다"
                ],
                "answer": 2,
                "explain": "정책은 한 환경 문제를 해결하면서 다른 문제를 악화시킬 수도 있어. 여러 환경 지표를 함께 살펴 부작용과 전체 효과를 평가해야 해."
            },
            {
                "q": "도시 녹화 사업의 효과를 과학적으로 조사하는 방법으로 가장 적절한 것은?",
                "choices": [
                    "사업 이후 녹지 한 곳만 관찰한다",
                    "가장 시원했던 날의 온도만 사용한다",
                    "사업 지역과 비교 지역을 여러 시점에서 측정하고 주변 조건도 고려한다",
                    "결과가 예상과 다르면 자료를 삭제한다"
                ],
                "answer": 2,
                "explain": "사업 전후의 자료와 비교 지역을 활용하면 계절이나 날씨 같은 요인의 영향을 구분하는 데 도움이 돼. 측정 위치와 방법도 일관되게 유지해야 해."
            }
        ]
    }
}


class EcoDetective:
    def __init__(self, root):
        self.root = root
        self.root.title("Eco Detective 3.0")
        self.root.geometry("820x760")
        self.root.minsize(700, 650)
        self.root.configure(bg=BG)

        self.level = None
        self.questions = []
        self.index = 0
        self.score = 0
        self.correct = 0
        self.answered = False

        self.show_start()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def label(self, parent, text, size=12, color=TEXT,
              bg=BG, bold=False, **kwargs):
        font = ("Malgun Gothic", size,
                "bold" if bold else "normal")
        return tk.Label(
            parent,
            text=text,
            font=font,
            fg=color,
            bg=bg,
            **kwargs
        )

    def button(self, parent, text, command,
               bg=GREEN, fg=WHITE, **kwargs):
        return tk.Button(
            parent,
            text=text,
            command=command,
            font=("Malgun Gothic", 12, "bold"),
            bg=bg,
            fg=fg,
            activebackground=LIGHT,
            activeforeground=DARK,
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=10,
            **kwargs
        )

    def show_start(self):
        self.clear()

        outer = tk.Frame(self.root, bg=BG, padx=28, pady=20)
        outer.pack(fill="both", expand=True)

        self.label(
            outer, "🌍", 42, DARK, bg=BG
        ).pack(pady=(8, 0))

        self.label(
            outer, "ECO DETECTIVE", 28, DARK,
            bg=BG, bold=True
        ).pack()

        self.label(
            outer, "환경 문제를 추리하고 지구를 지켜라!",
            13, MUTED, bg=BG
        ).pack(pady=(5, 18))

        card = tk.Frame(
            outer, bg=WHITE, padx=24, pady=18,
            highlightbackground=LIGHT, highlightthickness=2
        )
        card.pack(fill="x", pady=8)

        self.label(
            card, "🌱 당신은 환경 탐정입니다", 17,
            DARK, WHITE, bold=True
        ).pack(pady=(0, 8))

        self.label(
            card,
            "문제를 풀고 해설을 읽으며 환경 과학 지식을 쌓아 보세요.\n"
            "난이도마다 10문제가 출제됩니다.",
            11, TEXT, WHITE, justify="center",
            wraplength=620
        ).pack()

        self.label(
            outer, "난이도를 선택하세요",
            15, DARK, BG, bold=True
        ).pack(pady=(18, 10))

        for name, info in LEVELS.items():
            text = (
                f"{name}  |  문제당 {info['points']}점\n"
                f"{info['desc']}"
            )
            self.button(
                outer, text,
                lambda n=name: self.start_game(n),
                bg=GREEN if name == "중급" else (
                    "#246D48" if name == "고급" else DARK
                )
            ).pack(fill="x", pady=5)

        self.label(
            outer,
            "중급 최대 100점  ·  고급 최대 200점  ·  전문가 최대 300점",
            10, MUTED, BG
        ).pack(pady=(12, 0))

    def start_game(self, level):
        self.level = level
        self.questions = LEVELS[level]["questions"].copy()
        random.shuffle(self.questions)
        self.index = 0
        self.score = 0
        self.correct = 0
        self.answered = False
        self.show_question()

    def show_question(self):
        self.clear()
        self.answered = False

        outer = tk.Frame(self.root, bg=BG, padx=24, pady=18)
        outer.pack(fill="both", expand=True)

        top = tk.Frame(outer, bg=BG)
        top.pack(fill="x")

        self.label(
            top, f"🌿 ECO DETECTIVE  |  {self.level}",
            16, DARK, BG, bold=True
        ).pack(side="left")

        self.label(
            top, f"{self.index + 1} / {len(self.questions)}",
            12, MUTED, BG
        ).pack(side="right")

        progress_bg = tk.Frame(outer, bg=LIGHT, height=10)
        progress_bg.pack(fill="x", pady=(12, 20))
        progress_bg.pack_propagate(False)

        progress_fill = tk.Frame(progress_bg, bg=GREEN)
        progress_fill.place(
            relx=0, rely=0,
            relwidth=(self.index + 1) / len(self.questions),
            relheight=1
        )

        info = LEVELS[self.level]
        self.label(
            outer,
            f"현재 점수: {self.score}점  |  정답: {self.correct}개",
            11, MUTED, BG
        ).pack(anchor="w", pady=(0, 12))

        card = tk.Frame(
            outer, bg=WHITE, padx=22, pady=22,
            highlightbackground=LIGHT, highlightthickness=2
        )
        card.pack(fill="x", pady=(0, 14))

        self.label(
            card, f"QUESTION {self.index + 1:02d}",
            11, GREEN, WHITE, bold=True
        ).pack(anchor="w")

        question = self.questions[self.index]
        self.label(
            card, question["q"], 16, DARK, WHITE,
            bold=True, wraplength=680,
            justify="left"
        ).pack(anchor="w", pady=(12, 4))

        self.choice_buttons = []
        self.feedback = None

        for i, choice in enumerate(question["choices"]):
            btn = self.button(
                outer,
                f"{i + 1}.  {choice}",
                lambda n=i: self.check_answer(n),
                bg=WHITE, fg=TEXT,
                anchor="w", justify="left",
                wraplength=650
            )
            btn.pack(fill="x", pady=5)
            self.choice_buttons.append(btn)

        self.feedback_frame = tk.Frame(outer, bg=BG)
        self.feedback_frame.pack(fill="x", pady=(10, 0))

        self.next_button = self.button(
            outer, "다음 문제 →", self.next_question
        )
        self.next_button.pack(fill="x", pady=(10, 0))
        self.next_button.pack_forget()

        self.button(
            outer, "난이도 선택으로 돌아가기",
            self.show_start, bg=LIGHT, fg=DARK
        ).pack(fill="x", pady=(8, 0))

    def check_answer(self, selected):
        if self.answered:
            return

        self.answered = True
        question = self.questions[self.index]
        correct_answer = question["answer"]
        points = LEVELS[self.level]["points"]

        for btn in self.choice_buttons:
            btn.config(state="disabled")

        self.choice_buttons[correct_answer].config(
            bg="#BDE8C9", fg=DARK
        )

        if selected == correct_answer:
            self.correct += 1
            self.score += points
            title = f"정답! +{points}점 🎉"
            color = GREEN
            bg = "#E2F6E7"
        else:
            self.choice_buttons[selected].config(
                bg="#F8D9D6", fg="#8B2923"
            )
            title = "아쉽지만 오답이에요."
            color = "#A33A32"
            bg = RED

        self.feedback_frame.config(bg=bg)

        self.label(
            self.feedback_frame, title, 13,
            color, bg, bold=True
        ).pack(anchor="w", padx=12, pady=(10, 4))

        self.label(
            self.feedback_frame,
            "해설: " + question["explain"],
            11, TEXT, bg,
            wraplength=680, justify="left"
        ).pack(anchor="w", padx=12, pady=(0, 10))

        self.next_button.pack(fill="x", pady=(10, 0))

        if self.index == len(self.questions) - 1:
            self.next_button.config(text="최종 결과 보기 →")

    def next_question(self):
        if not self.answered:
            return

        if self.index < len(self.questions) - 1:
            self.index += 1
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        self.clear()

        total = len(self.questions)
        max_score = total * LEVELS[self.level]["points"]
        accuracy = self.correct / total * 100

        if accuracy == 100:
            rank = "환경 지킴이 마스터 🏆"
            message = "완벽해요! 환경 탐정의 실력이 대단해요."
        elif accuracy >= 80:
            rank = "최고의 환경 탐정 🌟"
            message = "훌륭해요! 환경 과학을 잘 이해하고 있어요."
        elif accuracy >= 60:
            rank = "유능한 환경 탐정 🌿"
            message = "좋아요! 해설을 복습하면 더 성장할 수 있어요."
        elif accuracy >= 40:
            rank = "성장 중인 탐정 🌱"
            message = "다시 도전하며 새로운 지식을 쌓아 봐요."
        else:
            rank = "새싹 탐정 🍀"
            message = "괜찮아요! 배우는 과정도 중요한 성과예요."

        outer = tk.Frame(self.root, bg=BG, padx=28, pady=24)
        outer.pack(fill="both", expand=True)

        self.label(
            outer, "🎉", 48, DARK, BG
        ).pack(pady=(10, 0))

        self.label(
            outer, "MISSION COMPLETE!",
            23, DARK, BG, bold=True
        ).pack(pady=(0, 16))

        card = tk.Frame(
            outer, bg=WHITE, padx=24, pady=24,
            highlightbackground=LIGHT, highlightthickness=2
        )
        card.pack(fill="x", pady=8)

        self.label(
            card, rank, 19, DARK, WHITE, bold=True
        ).pack(pady=(0, 12))

        self.label(
            card, f"{self.score}점", 36, GREEN,
            WHITE, bold=True
        ).pack()

        self.label(
            card, f"최대 점수: {max_score}점",
            11, MUTED, WHITE
        ).pack(pady=(2, 14))

        stats = tk.Frame(card, bg=WHITE)
        stats.pack(fill="x", pady=5)

        for value, caption in [
            (f"{self.correct}/{total}", "정답 수"),
            (f"{accuracy:.0f}%", "정답률"),
            (self.level, "난이도")
        ]:
            item = tk.Frame(stats, bg=LIGHT, padx=12, pady=12)
            item.pack(side="left", fill="both", expand=True, padx=4)

            self.label(
                item, value, 17, DARK, LIGHT, bold=True
            ).pack()

            self.label(
                item, caption, 10, MUTED, LIGHT
            ).pack(pady=(3, 0))

        self.label(
            outer, message, 12, TEXT, BG,
            wraplength=650
        ).pack(pady=14)

        self.button(
            outer, "같은 난이도로 다시 도전하기",
            lambda: self.start_game(self.level)
        ).pack(fill="x", pady=5)

        self.button(
            outer, "다른 난이도 선택하기",
            self.show_start, bg=LIGHT, fg=DARK
        ).pack(fill="x", pady=5)

        self.label(
            outer, "Eco Detective 3.0 | Learn for a greener future",
            10, MUTED, BG
        ).pack(pady=(14, 0))


if __name__ == "__main__":
    root = tk.Tk()
    app = EcoDetective(root)
    root.mainloop()
