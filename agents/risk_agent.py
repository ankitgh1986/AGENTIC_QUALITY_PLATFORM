class RiskAgent:

    def assess(

        self,

        validation_result

    ):

        failure_type = (

            validation_result["failure_type"]

        )

        if failure_type == "NONE":

            return {

                "risk": "LOW"

            }

        if failure_type in [

            "HALLUCINATION",

            "INTENT_DRIFT",

            "CONTRADICTION"

        ]:

            return {

                "risk": "HIGH"

            }

        return {

            "risk": "MEDIUM"

        }