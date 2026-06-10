class JudgeBAgent:

    def evaluate(

        self,

        validation_result

    ):

        print(

            "\nJUDGE B AGENT"

        )

        failure_type = (

            validation_result["failure_type"]

        )

        if (

            validation_result["validation"]

            == "PASS"

        ):

            score = 8

            verdict = "PASS"

            reason = (

                "Response mostly matches expected behavior."

            )

        else:

            if failure_type == "INTENT_DRIFT":

                score = 6

                verdict = "PASS"

                reason = (

                    "Potentially acceptable response."

                )

            else:

                score = 3

                verdict = "FAIL"

                reason = (

                    "Potential quality issue detected."

                )

        print(

            f"\nJudge B Score: {score}/10"

        )

        print(

            f"\nJudge B Verdict: {verdict}"

        )

        print(

            f"\nJudge B Reason: {reason}"

        )

        return {

            "score": score,

            "verdict": verdict,

            "reason": reason

        }