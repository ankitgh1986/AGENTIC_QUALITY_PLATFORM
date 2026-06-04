class LLMJudgeAgent:

    def evaluate(

        self,

        validation_result

    ):

        print(

            "\nLLM JUDGE AGENT"

        )

        if (

            validation_result["validation"]

            == "PASS"

        ):

            score = 9

            verdict = "PASS"

            reason = (

                "Response aligns with expected intent."

            )

        else:

            score = 2

            verdict = "FAIL"

            failure_type = (

                validation_result["failure_type"]

            )

            if failure_type == "HALLUCINATION":

                reason = (

                    "Response contains unsupported information."

                )

            elif failure_type == "INTENT_DRIFT":

                reason = (

                    "Response addresses a different intent."

                )

            elif failure_type == "CONTRADICTION":

                reason = (

                    "Response contradicts expected information."

                )

            else:

                reason = (

                    "Quality issue detected."

                )

        print(

            f"\nJudge Score: {score}/10"

        )

        print(

            f"\nJudge Verdict: {verdict}"

        )

        print(

            f"\nJudge Reason: {reason}"

        )

        return {

            "score": score,

            "verdict": verdict,

            "reason": reason

        }