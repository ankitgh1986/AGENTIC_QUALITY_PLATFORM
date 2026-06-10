import csv


class CSVExportAgent:

    def export(

        self,

        results,

        filename="reports/results.csv"

    ):

        with open(

            filename,

            "w",

            newline="",

            encoding="utf-8"

        ) as file:

            writer = csv.writer(

                file

            )

            writer.writerow(

                [

                    "Scenario ID",

                    "Intent",

                    "Result",

                    "Semantic Score",

                    "Judge A Score",

                    "Judge A Verdict",

                    "Judge B Score",

                    "Judge B Verdict",

                    "Consensus Score",

                    "Consensus Agreement",

                    "Consensus Verdict",

                    "Confidence Score",

                    "Confidence Level",

                    "Probability Score",

                    "Probability Likelihood",

                    "Probability Verdict",

                    "Risk",

                    "Failure Type"

                ]

            )

            for result in results:

                writer.writerow(

                    [

                        result.scenario_id,

                        result.intent,

                        result.result,

                        result.semantic_score,

                        result.judge_a_score,

                        result.judge_a_verdict,

                        result.judge_b_score,

                        result.judge_b_verdict,

                        result.consensus_score,

                        result.consensus_agreement,

                        result.consensus_verdict,

                        result.confidence_score,

                        result.confidence_level,

                        result.probability_score,

                        result.probability_likelihood,

                        result.probability_verdict,

                        result.risk,

                        result.failure_type

                    ]

                )

        print(

            f"\nCSV Exported: {filename}"

        )