from agents.api_agent import APIAgent

from agents.llm_agent import LLMAgent

from agents.semantic_similarity_agent import (
    SemanticSimilarityAgent
)

from agents.semantic_validator_agent import (
    SemanticValidatorAgent
)

from agents.judge_a_agent import (
    JudgeAAgent
)

from agents.judge_b_agent import (
    JudgeBAgent
)

from agents.consensus_agent import (
    ConsensusAgent
)

from agents.confidence_agent import (
    ConfidenceAgent
)

from agents.probabilistic_verification_agent import (
    ProbabilisticVerificationAgent
)

from agents.risk_agent import (
    RiskAgent
)

from models.evaluation_result import (
    EvaluationResult
)


class OrchestratorAgent:

    def __init__(

        self

    ):

        self.api_agent = APIAgent()

        self.llm_agent = LLMAgent()

        self.similarity_agent = (
            SemanticSimilarityAgent()
        )

        self.validator = (
            SemanticValidatorAgent()
        )

        self.judge_a_agent = (
            JudgeAAgent()
        )

        self.judge_b_agent = (
            JudgeBAgent()
        )

        self.consensus_agent = (
            ConsensusAgent()
        )

        self.confidence_agent = (
            ConfidenceAgent()
        )

        self.probability_agent = (
            ProbabilisticVerificationAgent()
        )

        self.risk_agent = (
            RiskAgent()
        )

    def execute(

        self,

        scenario

    ):

        print(

            "\n======================"

        )

        print(

            f"SCENARIO: {scenario['id']}"

        )

        print(

            "======================"

        )

        intent = scenario["intent"]

        prompt = scenario["prompt"]

        print(

            f"\nPrompt: {prompt}"

        )

        result = EvaluationResult(

            scenario["id"],

            intent

        )

        api_response = (

            self.api_agent.execute(

                intent

            )

        )

        result.api_response = (
            api_response
        )

        llm_response = (

            self.llm_agent.execute(

                intent

            )

        )

        result.llm_response = (
            llm_response
        )

        similarity_score = (

            self.similarity_agent.calculate(

                api_response["message"],

                llm_response

            )

        )

        validation_result = (

            self.validator.validate(

                intent,

                llm_response,

                similarity_score,

                api_response

            )

        )

        judge_a_result = (

            self.judge_a_agent.evaluate(

                validation_result

            )

        )

        judge_b_result = (

            self.judge_b_agent.evaluate(

                validation_result

            )

        )

        consensus_result = (

            self.consensus_agent.evaluate(

                judge_a_result,

                judge_b_result

            )

        )

        confidence_result = (

            self.confidence_agent.calculate(

                validation_result["semantic_score"],

                consensus_result["score"]

            )

        )

        probability_result = (

            self.probability_agent.verify(

                validation_result["semantic_score"],

                consensus_result["score"],

                confidence_result["score"]

            )

        )

        risk_result = (

            self.risk_agent.assess(

                validation_result

            )

        )

        result.result = (
            validation_result["validation"]
        )

        result.semantic_score = (
            validation_result["semantic_score"]
        )

        result.failure_type = (
            validation_result["failure_type"]
        )

        result.judge_a_score = (
            judge_a_result["score"]
        )

        result.judge_a_verdict = (
            judge_a_result["verdict"]
        )

        result.judge_b_score = (
            judge_b_result["score"]
        )

        result.judge_b_verdict = (
            judge_b_result["verdict"]
        )

        result.consensus_score = (
            consensus_result["score"]
        )

        result.consensus_agreement = (
            consensus_result["agreement"]
        )

        result.consensus_verdict = (
            consensus_result["verdict"]
        )

        result.confidence_score = (
            confidence_result["score"]
        )

        result.confidence_level = (
            confidence_result["level"]
        )

        result.probability_score = (
            probability_result["probability"]
        )

        result.probability_likelihood = (
            probability_result["likelihood"]
        )

        result.probability_verdict = (
            probability_result["verdict"]
        )

        result.risk = (
            risk_result["risk"]
        )

        print(

            f"\nRisk Level: {result.risk}"

        )

        print(

            f"\nFailure Type: {result.failure_type}"

        )

        print(

            f"\nFinal Result: {result.result}"

        )

        return result