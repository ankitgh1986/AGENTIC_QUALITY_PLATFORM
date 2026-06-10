class IntelligentEvaluationAgent:

    def evaluate(

        self,

        semantic_score,

        consensus_score,

        confidence_score,

        probability_score,

        security_risk,

        review_required

    ):

        print(

            "\nINTELLIGENT EVALUATION AGENT"

        )

        if security_risk == "HIGH":

            final_decision = "REVIEW_REQUIRED"

            reason = (

                "Security review required."

            )

        elif review_required:

            final_decision = (

                "REVIEW_REQUIRED"

            )

            reason = (

                "Human review required."

            )

        else:

            composite_score = (

                (
                    semantic_score * 100
                )

                + (
                    consensus_score * 10
                )

                + confidence_score

                + probability_score

            ) / 4

            if composite_score >= 75:

                final_decision = "PASS"

                reason = (

                    "Quality checks passed."

                )

            elif composite_score >= 60:

                final_decision = (

                    "REVIEW_REQUIRED"

                )

                reason = (

                    "Borderline quality."

                )

            else:

                final_decision = "FAIL"

                reason = (

                    "Quality below threshold."

                )

        print(

            f"\nFinal Decision: {final_decision}"

        )

        print(

            f"\nReason: {reason}"

        )

        return {

            "decision":
            final_decision,

            "reason":
            reason

        }