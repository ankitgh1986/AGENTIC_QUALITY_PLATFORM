class EvaluationResult:

    def __init__(

        self,

        scenario_id,

        intent

    ):

        self.scenario_id = scenario_id

        self.intent = intent

        self.api_response = None

        self.llm_response = None

        self.result = None

        self.semantic_score = 0.0

        self.judge_score = 0

        self.judge_verdict = None

        self.judge_reason = None

        self.risk = None

        self.failure_type = None