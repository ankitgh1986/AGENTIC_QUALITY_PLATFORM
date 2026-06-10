class ConsensusAgent:

    def evaluate(

        self,

        judge_a,

        judge_b

    ):

        print(

            "\nCONSENSUS AGENT"

        )

        consensus_score = (

            judge_a["score"]

            +

            judge_b["score"]

        ) / 2

        if (

            judge_a["verdict"]

            == judge_b["verdict"]

        ):

            agreement = 100

            verdict = (

                judge_a["verdict"]

            )

        else:

            agreement = 50

            verdict = (

                "REVIEW_REQUIRED"

            )

        print(

            f"\nConsensus Score: {consensus_score:.2f}"

        )

        print(

            f"\nAgreement: {agreement}%"

        )

        print(

            f"\nConsensus Verdict: {verdict}"

        )

        return {

            "score": consensus_score,

            "agreement": agreement,

            "verdict": verdict

        }