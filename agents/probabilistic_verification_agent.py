class ProbabilisticVerificationAgent:

    def verify(

        self,

        semantic_score,

        judge_score,

        confidence_score

    ):

        print(

            "\nPROBABILISTIC VERIFICATION AGENT"

        )

        probability = (

            (semantic_score * 100 * 0.40)

            +

            (judge_score * 10 * 0.30)

            +

            (confidence_score * 0.30)

        )

        if probability >= 80:

            likelihood = "HIGH"

            verdict = (
                "LIKELY_CORRECT"
            )

        elif probability >= 50:

            likelihood = "MEDIUM"

            verdict = (
                "UNCERTAIN"
            )

        else:

            likelihood = "LOW"

            verdict = (
                "LIKELY_INCORRECT"
            )

        print(

            f"\nProbability Correct: {probability:.2f}%"

        )

        print(

            f"\nLikelihood: {likelihood}"

        )

        print(

            f"\nVerification Verdict: {verdict}"

        )

        return {

            "probability":
            probability,

            "likelihood":
            likelihood,

            "verdict":
            verdict

        }