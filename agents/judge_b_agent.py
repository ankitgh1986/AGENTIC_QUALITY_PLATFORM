class JudgeBAgent:

    def evaluate(

        self,

        validation_result

    ):

        print(

            "\nJUDGE B AGENT"

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

        return {

            "score": score,

            "verdict": verdict,

            "reason": reason

        }