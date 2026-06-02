from test_data.telecom_scenarios import TELECOM_SCENARIOS

class ScenarioAgent:
    def generate(
        self
    ):
        print(
            "\nSCENARIO AGENT"
        )
        print(
            f"\nLoaded {len(TELECOM_SCENARIOS)} senarios" 
            )
        
        return TELECOM_SCENARIOS