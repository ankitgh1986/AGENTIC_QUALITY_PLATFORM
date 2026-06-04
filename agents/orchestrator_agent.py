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

from agents.risk_agent import (
    RiskAgent
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

        api_response = (

            self.api_agent.execute(

                intent

            )

        )

        llm_response = (

            self.llm_agent.execute(

                intent

            )

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

        risk_result = (

            self.risk_agent.assess(

                validation_result

            )

        )

        print(

            f"\nRisk Level: {risk_result['risk']}"

        )

        print(

            f"\nFailure Type: {validation_result['failure_type']}"

        )

        print(

            f"\nFinal Result: {validation_result['validation']}"

        )

        return {

            "scenario_id":
            scenario["id"],

            "intent":
            intent,

            "api_response":
            api_response,

            "llm_response":
            llm_response,

            "result":
            validation_result["validation"],

            "semantic_score":
            validation_result["semantic_score"],

            "judge_score":
            judge_result["score"],

            "judge_verdict":
            judge_result["verdict"],

            "judge_reason":
            judge_result["reason"],

            "risk":
            risk_result["risk"],

            "failure_type":
            validation_result["failure_type"]

        }