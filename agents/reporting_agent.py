from agents.trend_analysis_agent import (
    TrendAnalysisAgent
)


class ReportingAgent:

    def generate(

        self,

        results

    ):

        total = len(results)

        passed = sum(

            1

            for result in results

            if result.result == "PASS"

        )

        failed = total - passed

        pass_rate = (

            passed / total * 100

        )

        average_semantic_score = (

            sum(

                result.semantic_score

                for result in results

            ) / total

        )

        average_judge_score = (

            sum(

                result.judge_score

                for result in results

            ) / total

        )

        hallucinations = sum(

            1

            for result in results

            if result.failure_type == "HALLUCINATION"

        )

        intent_drift = sum(

            1

            for result in results

            if result.failure_type == "INTENT_DRIFT"

        )

        contradictions = sum(

            1

            for result in results

            if result.failure_type == "CONTRADICTION"

        )

        high_risk = sum(

            1

            for result in results

            if result.risk == "HIGH"

        )

        trend_agent = (

            TrendAnalysisAgent()

        )

        trend_result = (

            trend_agent.analyze(

                pass_rate

            )

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

        print(

            "\nTREND ANALYSIS"

        )

        if (

            trend_result["previous"]

            is None

        ):

            print(

                "\nBaseline Run Established"

            )

        else:

            print(

                f"\nPrevious Pass Rate: {trend_result['previous']:.2f}%"

            )

            print(

                f"Current Pass Rate: {trend_result['current']:.2f}%"

            )

            print(

                f"Trend: {trend_result['trend']}"

            )

            print(

                f"Change: {trend_result['change']:.2f}%"

            )

        recommendation = (

            "GO"

            if pass_rate >= 90

            else "NO GO"

        )

        print(

            f"\nRecommendation: {recommendation}"

        )