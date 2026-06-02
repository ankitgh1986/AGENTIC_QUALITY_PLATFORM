class SemanticValidatorAgent:

    def validate(

        self,

        intent,

        response,

        api_response=None

    ):

        print(

            "\nSEMANTIC VALIDATOR"

        )

        response = response.lower()

        result = "PASS"

        # Customer Care Hallucination

        if intent == "customer_care":

            if "999" in response:

                result = "FAIL"

        # Bill Payment Intent Drift

        elif intent == "bill_payment":

            if "recharge" in response:

                result = "FAIL"

        # Roaming Contradiction

        elif intent == "roaming":

            if "not available" in response:

                result = "FAIL"

        print(

            f"\nValidation: {result}"

        )

        return result