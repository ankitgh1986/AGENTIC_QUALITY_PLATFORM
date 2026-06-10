class JudgeAAgent:

    def evaluate(

        self,

        validation_result

    ):

        print(

            "\nJUDGE A AGENT"

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

            reason = (

                "Quality issue detected."

            )

        print(

            f"\nJudge A Score: {score}/10"

        )

        print(

            f"\nJudge A Verdict: {verdict}"

        )

        return {

            "score": score,

            "verdict": verdict,

            "reason": reason

        }