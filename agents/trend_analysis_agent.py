import os
import csv


class TrendAnalysisAgent:

    def analyze(

        self,

        current_pass_rate,

        filename="reports/history.csv"

    ):

        print(

            "\nTREND ANALYSIS AGENT"

        )

        previous_pass_rate = None

        if os.path.exists(

            filename

        ):

            with open(

                filename,

                "r",

                encoding="utf-8"

            ) as file:

                reader = list(

                    csv.reader(

                        file

                    )

                )

                if len(

                    reader

                ) > 1:

                    previous_pass_rate = float(

                        reader[-1][1]

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

            if os.path.getsize(

                filename

            ) == 0:

                writer.writerow(

                    [

                        "run",

                        "pass_rate"

                    ]

                )

            run_number = 1

            if previous_pass_rate is not None:

                run_number = len(

                    reader

                )

            writer.writerow(

                [

                    run_number,

                    current_pass_rate

                ]

            )

        if previous_pass_rate is None:

            return {

                "previous": None,

                "current": current_pass_rate,

                "trend": "BASELINE",

                "change": 0

            }

        change = (

            current_pass_rate

            - previous_pass_rate

        )

        if change > 0:

            trend = "IMPROVING"

        elif change < 0:

            trend = "DECLINING"

        else:

            trend = "STABLE"

        return {

            "previous": previous_pass_rate,

            "current": current_pass_rate,

            "trend": trend,

            "change": change

        }