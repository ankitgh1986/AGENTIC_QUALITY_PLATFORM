class ConfidenceAgent:

    def calculate(

        self,

        semantic_score,

        judge_score

    ):

        print(

            "\nCONFIDENCE AGENT"

        )

        confidence_score = (

            (
                semantic_score * 10
            )

            +

            judge_score

        ) / 20 * 100

        if confidence_score >= 80:

            confidence_level = "HIGH"

        elif confidence_score >= 50:

            confidence_level = "MEDIUM"

        else:

            confidence_level = "LOW"

        print(

            f"\nConfidence Score: {confidence_score:.2f}%"

        )

        print(

            f"\nConfidence Level: {confidence_level}"

        )

        return {

            "score": confidence_score,

            "level": confidence_level

        }