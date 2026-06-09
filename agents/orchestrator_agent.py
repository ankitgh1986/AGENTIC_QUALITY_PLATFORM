from agents.api_agent import APIAgent

from agents.llm_agent import LLMAgent

from agents.semantic_similarity_agent import (
    SemanticSimilarityAgent
)

from agents.semantic_validator_agent import (
    SemanticValidatorAgent
)

from agents.llm_judge_agent import (
    LLMJudgeAgent
)

from agents.confidence_agent import (
    ConfidenceAgent
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

        self.judge_agent = (
            LLMJudgeAgent()
        )

        self.confidence_agent = (
            ConfidenceAgent()
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

        judge_result = (

            self.judge_agent.evaluate(

                validation_result

            )

        )

        confidence_result = (

            self.confidence_agent.calculate(

                validation_result["semantic_score"],

                judge_result["score"]

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

        result.judge_score = (
            judge_result["score"]
        )

        result.judge_verdict = (
            judge_result["verdict"]
        )

        result.judge_reason = (
            judge_result["reason"]
        )

        result.confidence_score = (
            confidence_result["score"]
        )

        result.confidence_level = (
            confidence_result["level"]
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