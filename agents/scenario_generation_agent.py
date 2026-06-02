from test_data.telecom_intents import (
    TELECOM_INTENTS
)


class ScenarioGenerationAgent:

    def generate(

        self

    ):

        print(

            "\nSCENARIO GENERATION AGENT"

        )

        scenarios = []

        scenario_counter = 1

        for intent in TELECOM_INTENTS:

            generated = (

                self._generate_for_intent(

                    intent

                )

            )

            for prompt in generated:

                scenarios.append(

                    {

                        "id":
                        f"GEN_{scenario_counter:03}",

                        "intent":
                        intent,

                        "category":
                        "generated",

                        "prompt":
                        prompt

                    }

                )

                scenario_counter += 1

        print(

            f"\nGenerated {len(scenarios)} scenarios"

        )

        return scenarios

    def _generate_for_intent(

        self,

        intent

    ):

        intent_text = (

            intent.replace(

                "_",

                " "

            )

        )

        return [

            f"How do I perform {intent_text}?",

            f"Help me with {intent_text}.",

            f"Can you assist with {intent_text}?",

            f"What is the process for {intent_text}?",

            f"I need support for {intent_text}."

        ]