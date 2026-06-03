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

                    "Risk",

                    "Failure Type"

                ]

            )

            for result in results:

                writer.writerow(

                    [

                        result["scenario_id"],

                        result["intent"],

                        result["result"],

                        result["semantic_score"],

                        result["risk"],

                        result["failure_type"]

                    ]

                )

        print(

            f"\nCSV Exported: {filename}"

        )