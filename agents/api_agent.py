from test_data.telecom_api_responses import TELECOM_API_RESPONSES


class APIAgent:

    def execute(

        self,

        intent

    ):

        print(

            "\nAPI AGENT"

        )

        response = TELECOM_API_RESPONSES.get(

            intent,

            {

                "status": 404,

                "message": "Intent not found"

            }

        )

        print(

            f"\nIntent: {intent}"

        )

        print(

            f"\nAPI Response: {response}"

        )

        return response