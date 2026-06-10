class ReviewQueueAgent:

    def evaluate(

        self,

        consensus_result

    ):

        print(

            "\nREVIEW QUEUE AGENT"

        )

        if (

            consensus_result["agreement"]

            < 100

        ):

            review_required = True

            status = (
                "PENDING_REVIEW"
            )

        else:

            review_required = False

            status = (
                "NOT_REQUIRED"
            )

        print(

            f"\nReview Required: {review_required}"

        )

        print(

            f"\nReview Status: {status}"

        )

        return {

            "required":
            review_required,

            "status":
            status

        }