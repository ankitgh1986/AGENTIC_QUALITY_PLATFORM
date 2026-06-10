class PromptSecurityAgent:

    def evaluate(

        self,

        prompt

    ):

        print(

            "\nPROMPT SECURITY AGENT"

        )

        prompt = prompt.lower()

        security_risk = "LOW"

        attack_type = "NONE"

        suspicious_patterns = [

            "ignore previous instructions",

            "bypass",

            "skip validation",

            "hidden information",

            "internal details"

        ]

        for pattern in suspicious_patterns:

            if pattern in prompt:

                security_risk = "HIGH"

                attack_type = "PROMPT_INJECTION"

                break

        print(

            f"\nSecurity Risk: {security_risk}"

        )

        print(

            f"\nAttack Type: {attack_type}"

        )

        return {

            "risk": security_risk,

            "attack_type": attack_type

        }