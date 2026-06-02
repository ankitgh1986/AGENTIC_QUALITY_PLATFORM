from agents.api_agent import APIAgent

from agents.llm_agent import LLMAgent

from agents.semantic_validator_agent import (
    SemanticValidatorAgent
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

        self.validator = (
            SemanticValidatorAgent()
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

        validation_result = (

            self.validator.validate(

                intent,

                llm_response

            )

        )

        risk_result = (

            self.risk_agent.assess(

                intent,

                validation_result

            )

        )

        print(

            f"\nRisk Level: {risk_result['risk']}"

        )

        print(

            f"\nFailure Type: {risk_result['failure_type']}"

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
            validation_result,

            "risk":
            risk_result["risk"],

            "failure_type":
            risk_result["failure_type"]

        }