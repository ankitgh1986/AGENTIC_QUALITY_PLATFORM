class SemanticValidatorAgent:

    def validate(

        self,

        intent,

        response,

        similarity_score,

        api_response=None

    ):

        print(

            "\nSEMANTIC VALIDATOR"

        )

        response = response.lower()

        validation = "PASS"

        failure_type = "NONE"

        semantic_score = similarity_score

        if intent == "customer_care":

            if "999" in response:

                validation = "FAIL"

                failure_type = "HALLUCINATION"

        elif intent == "bill_payment":

            if "recharge" in response:

                validation = "FAIL"

                failure_type = "INTENT_DRIFT"

        elif intent == "roaming":

            if "not available" in response:

                validation = "FAIL"

                failure_type = "CONTRADICTION"

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