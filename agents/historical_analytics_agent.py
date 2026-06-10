import csv

import os

from datetime import datetime


class HistoricalAnalyticsAgent:

    def save_run(

        self,

        pass_rate,

        confidence_score,

        probability_score,

        review_rate,

        high_risk_count

    ):

        filename = "reports/run_history.csv"

        file_exists = os.path.isfile(

            filename

        )

        with open(

            filename,

            "a",

            newline="",

            encoding="utf-8"

        ) as file:

            writer = csv.writer(

                file

            )

            if not file_exists:

                writer.writerow(

                    [

                        "timestamp",

                        "pass_rate",

                        "confidence_score",

                        "probability_score",

                        "review_rate",

                        "high_risk_count"

                    ]

                )

            writer.writerow(

                [

                    datetime.now(),

                    pass_rate,

                    confidence_score,

                    probability_score,

                    review_rate,

                    high_risk_count

                ]

            )

        print(

            "\nHISTORICAL ANALYTICS AGENT"

        )

        print(

            "\nRun History Updated"

        )

    def load_history(

        self

    ):

        filename = "reports/run_history.csv"

        if not os.path.exists(

            filename

        ):

            return {

                "total_runs": 0,

                "best_pass_rate": 0,

                "worst_pass_rate": 0,

                "average_pass_rate": 0,

                "latest_timestamp": None

            }

        with open(

            filename,

            "r",

            encoding="utf-8"

        ) as file:

            reader = csv.DictReader(

                file

            )

            rows = list(

                reader

            )

        if len(rows) == 0:

            return {

                "total_runs": 0,

                "best_pass_rate": 0,

                "worst_pass_rate": 0,

                "average_pass_rate": 0,

                "latest_timestamp": None

            }

        pass_rates = [

            float(

                row["pass_rate"]

            )

            for row in rows

        ]

        return {

            "total_runs": len(rows),

            "best_pass_rate": max(

                pass_rates

            ),

            "worst_pass_rate": min(

                pass_rates

            ),

            "average_pass_rate": (

                sum(pass_rates)

                / len(pass_rates)

            ),

            "latest_timestamp": rows[-1][

                "timestamp"

            ]

        }