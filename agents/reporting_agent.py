class ReportingAgent:

    def generate(

        self,

        results

    ):

        total = len(results)

        passed = sum(

            1

            for result in results

            if result["result"] == "PASS"

        )

        failed = total - passed

        pass_rate = (

            passed / total * 100

        )

        average_semantic_score = (

            sum(

                result["semantic_score"]

                for result in results

            ) / total

        )

        average_judge_score = (

            sum(

                result["judge_score"]

                for result in results

            ) / total

        )

        hallucinations = sum(

            1

            for result in results

            if result["failure_type"] == "HALLUCINATION"

        )

        intent_drift = sum(

            1

            for result in results

            if result["failure_type"] == "INTENT_DRIFT"

        )

        contradictions = sum(

            1

            for result in results

            if result["failure_type"] == "CONTRADICTION"

        )

        high_risk = sum(

            1

            for result in results

            if result["risk"] == "HIGH"

        )

        print(

            "\n======================"

        )

        print(

            "AI QUALITY REPORT"

        )

        print(

            "======================"

        )

        print(

            f"\nTotal Scenarios: {total}"

        )

        print(

            f"Passed: {passed}"

        )

        print(

            f"Failed: {failed}"

        )

        print(

            f"Pass Rate: {pass_rate:.2f}%"

        )

        print(

            f"Average Semantic Score: {average_semantic_score:.2f}"

        )

        print(

            f"Average Judge Score: {average_judge_score:.2f}/10"

        )

        print(

            "\nFAILURE BREAKDOWN"

        )

        print(

            f"\nHallucinations: {hallucinations}"

        )

        print(

            f"Intent Drift: {intent_drift}"

        )

        print(

            f"Contradictions: {contradictions}"

        )

        print(

            f"\nHigh Risk Issues: {high_risk}"

        )

        recommendation = (

            "GO"

            if pass_rate >= 90

            else "NO GO"

        )

        print(

            f"\nRecommendation: {recommendation}"

        )