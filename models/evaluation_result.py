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

        self.judge_a_score = 0

        self.judge_a_verdict = None

        self.judge_b_score = 0

        self.judge_b_verdict = None

        self.consensus_score = 0.0

        self.consensus_agreement = 0

        self.consensus_verdict = None

        self.confidence_score = 0.0

        self.confidence_level = None

        self.probability_score = 0.0

        self.probability_likelihood = None

        self.probability_verdict = None

        self.risk = None

        self.failure_type = None