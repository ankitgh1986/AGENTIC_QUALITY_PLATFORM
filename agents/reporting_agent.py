from agents.trend_analysis_agent import (
    TrendAnalysisAgent
)

from agents.historical_analytics_agent import (
    HistoricalAnalyticsAgent
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

        failed = sum(

            1

            for result in results

            if result.result == "FAIL"

        )

        review_required = sum(

            1

            for result in results

            if result.result == "REVIEW_REQUIRED"

        )

        pass_rate = (

            passed / total * 100

        )

        fail_rate = (

            failed / total * 100

        )

        intelligent_review_rate = (

            review_required / total * 100

        )

        average_semantic_score = (

            sum(

                result.semantic_score

                for result in results

            ) / total

        )

        average_judge_a_score = (

            sum(

                result.judge_a_score

                for result in results

            ) / total

        )

        average_judge_b_score = (

            sum(

                result.judge_b_score

                for result in results

            ) / total

        )

        average_consensus_score = (

            sum(

                result.consensus_score

                for result in results

            ) / total

        )

        average_agreement = (

            sum(

                result.consensus_agreement

                for result in results

            ) / total

        )

        average_confidence_score = (

            sum(

                result.confidence_score

                for result in results

            ) / total

        )

        average_probability_score = (

            sum(

                result.probability_score

                for result in results

            ) / total

        )

        pending_reviews = sum(

            1

            for result in results

            if result.review_required

        )

        review_rate = (

            pending_reviews / total * 100

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

        high_probability = sum(

            1

            for result in results

            if result.probability_likelihood == "HIGH"

        )

        medium_probability = sum(

            1

            for result in results

            if result.probability_likelihood == "MEDIUM"

        )

        low_probability = sum(

            1

            for result in results

            if result.probability_likelihood == "LOW"

        )

        high_security_risk = sum(

            1

            for result in results

            if result.security_risk == "HIGH"

        )

        prompt_injections = sum(

            1

            for result in results

            if result.attack_type == "PROMPT_INJECTION"

        )

        trend_agent = (

            TrendAnalysisAgent()

        )

        trend_result = (

            trend_agent.analyze(

                pass_rate

            )

        )

        historical_agent = (

            HistoricalAnalyticsAgent()

        )

        historical_agent.save_run(

            pass_rate,

            average_confidence_score,

            average_probability_score,

            review_rate,

            high_risk

        )

        history = (

            historical_agent.load_history()

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

            f"Review Required: {review_required}"

        )

        print(

            f"\nPass Rate: {pass_rate:.2f}%"

        )

        print(

            f"Fail Rate: {fail_rate:.2f}%"

        )

        print(

            f"Review Required Rate: {intelligent_review_rate:.2f}%"

        )

        print(

            f"\nAverage Semantic Score: {average_semantic_score:.2f}"

        )

        print(

            f"Average Judge A Score: {average_judge_a_score:.2f}/10"

        )

        print(

            f"Average Judge B Score: {average_judge_b_score:.2f}/10"

        )

        print(

            f"Average Consensus Score: {average_consensus_score:.2f}/10"

        )

        print(

            f"Average Agreement: {average_agreement:.2f}%"

        )

        print(

            f"Average Confidence Score: {average_confidence_score:.2f}%"

        )

        print(

            f"Average Probability Score: {average_probability_score:.2f}%"

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

            "\nCONSENSUS METRICS"

        )

        print(

            f"\nAverage Judge Agreement: {average_agreement:.2f}%"

        )

        print(

            f"Average Consensus Score: {average_consensus_score:.2f}/10"

        )

        print(

            "\nSECURITY ANALYSIS"

        )

        print(

            f"\nHigh Security Risk Scenarios: {high_security_risk}"

        )

        print(

            f"Prompt Injection Attempts: {prompt_injections}"

        )

        print(

            "\nREVIEW QUEUE"

        )

        print(

            f"\nPending Reviews: {pending_reviews}"

        )

        print(

            f"Review Queue Rate: {review_rate:.2f}%"

        )

        print(

            "\nPROBABILITY DISTRIBUTION"

        )

        print(

            f"\nHIGH: {high_probability}"

        )

        print(

            f"MEDIUM: {medium_probability}"

        )

        print(

            f"LOW: {low_probability}"

        )

        print(

            "\nHISTORICAL ANALYTICS"

        )

        print(

            f"\nTotal Historical Runs: {history['total_runs']}"

        )

        print(

            f"Best Pass Rate: {history['best_pass_rate']:.2f}%"

        )

        print(

            f"Worst Pass Rate: {history['worst_pass_rate']:.2f}%"

        )

        print(

            f"Historical Average Pass Rate: {history['average_pass_rate']:.2f}%"

        )

        print(

            f"Latest Run Timestamp: {history['latest_timestamp']}"

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