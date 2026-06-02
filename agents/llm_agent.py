from test_data.telecom_llm_responses import (
    TELECOM_LLM_RESPONSES
)


class LLMAgent:

    def execute(

        self,

        intent

    ):

        print(

            "\nLLM AGENT"

        )

        response = TELECOM_LLM_RESPONSES.get(

            intent,

            "Unable to answer this query."

        )

        print(

            f"\nIntent: {intent}"

        )

        print(

            f"\nLLM Response: {response}"

        )

        return response