class RiskAgent:

    def assess(

        self,

        intent,

        result

    ):

        if result == "PASS":

            return {

                "risk": "LOW",

                "failure_type": "NONE"

            }

        if intent == "customer_care":

            return {

                "risk": "HIGH",

                "failure_type":
                "HALLUCINATION"

            }

        if intent == "bill_payment":

            return {

                "risk": "HIGH",

                "failure_type":
                "INTENT_DRIFT"

            }

        if intent == "roaming":

            return {

                "risk": "HIGH",

                "failure_type":
                "CONTRADICTION"

            }

        return {

            "risk": "MEDIUM",

            "failure_type":
            "UNKNOWN"

        }