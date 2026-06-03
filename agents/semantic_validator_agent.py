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

        validation = "PASS"

        failure_type = "NONE"

        semantic_score = 1.00

        # Customer Care Hallucination

        if intent == "customer_care":

            if "999" in response:

                validation = "FAIL"

                failure_type = "HALLUCINATION"

                semantic_score = 0.20

        # Bill Payment Intent Drift

        elif intent == "bill_payment":

            if "recharge" in response:

                validation = "FAIL"

                failure_type = "INTENT_DRIFT"

                semantic_score = 0.30

        # Roaming Contradiction

        elif intent == "roaming":

            if "not available" in response:

                validation = "FAIL"

                failure_type = "CONTRADICTION"

                semantic_score = 0.10

        print(

            f"\nValidation: {validation}"

        )

        print(

            f"\nSemantic Score: {semantic_score:.2f}"

        )

        return {

            "validation": validation,

            "failure_type": failure_type,

            "semantic_score": semantic_score

        }